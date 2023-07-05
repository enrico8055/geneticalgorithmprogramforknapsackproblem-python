# GA UNTUK OPTIMISASI ITEM APA SAJA YANG MEMBERIKAN VALUE TERTINGGI UNTUK PELANGGAN CAFE TANPA MELEBIHI MODAL
import numpy, copy, random
import matplotlib.pyplot as plt

daftarFittnessTerbaikPerGenerasi = []
daftarWeightTerbaikPerGenerasi = []

def main(modalMaximal, namaBarang, valueBarang, hargaBarang, jumlahGenerasi, mutationRate):
    # modal maximal
    wMax = modalMaximal
    # print("Maximum Weight : ", wMax, "\n")

    # value item
    vItem = numpy.array(valueBarang)
    # print("Value Item : ", vItem, "\n")

    # harga item
    wItem = numpy.array(hargaBarang)
    # print("Weight Item : ", wItem, "\n")

    # membuat populasi random awal 
    def buatPopulasi():
        populasi = []
        for i in range(0, len(vItem)):
            spesies = numpy.random.randint(low=0, high=2, size=len(vItem))
            populasi.append({"Spesies": spesies, "Fittness": 0 })
        return populasi
    populasi = buatPopulasi()
    # print("Populasi Awal : \n", populasi, "\n")

    for x in range(0,jumlahGenerasi):
        # hitung fittness
        #1 melambangkan item dipilih, 0 melambangkan item tidak dipilih
        #jika weight melebihi dari maximal weight atau max modal fitness value = 0
        def hitungFitness():
            for i, e in enumerate(populasi):
                fittness = 0
                weight = 0
                for j, f in enumerate(populasi[i]["Spesies"]):
                    if f == 1:
                        weight += wItem[j]
                        fittness += vItem[j]
                populasi[i]["Fittness"] = fittness
                if(wMax < weight):
                    populasi[i]["Fittness"] = 0
        hitungFitness()
        # print("Populasi Dengan Fittness : \n", populasi, "\n")

        # ambil 2 parent terbaik fitnessny dari populasi
        listFitness = []
        for x in populasi:
            listFitness.append(x['Fittness'])
        parent1 = populasi[listFitness.index(max(listFitness))] #ambil yang punya fitness paling tinggi
        populasi[listFitness.index(max(listFitness))] = {'Spesies':0, 'Fittness': -1} #buang yang paling tinggi karna sudah diambil

        listFitness2 = []
        for x in populasi:
            listFitness2.append(x['Fittness'])
        parent2 = populasi[listFitness2.index(max(listFitness2))] #ambil yang paling tinggi fitnessnya

        populasi[listFitness.index(max(listFitness))] = parent1 #kembalikan populasi ke awal

        # print("Parent1 : \n", parent1, "\n")
        # print("Parent2 : \n", parent2, "\n")
                    
        # crossover parent1 dan 2
        child1 = copy.copy(parent1)
        child2 = copy.copy(parent2)
        pemotong = int(len(vItem)/2)
        child1['Spesies'] = numpy.append(parent1['Spesies'][0:pemotong], parent2['Spesies'][pemotong:len(vItem)])
        child2['Spesies'] = numpy.append(parent2['Spesies'][0:pemotong], parent1['Spesies'][pemotong:len(vItem)])
        # print("Child1 : \n", child1, "\n")
        # print("Child2 : \n", child2, "\n")


        #mutation
        mutan1 = copy.copy(child1)
        mutan2 = copy.copy(child2)

        def buatMutan(mutan):
            for i, e in enumerate(mutan['Spesies']):
                if random.random() <= mutationRate:
                    mutan['Spesies'][i] = random.randint(0,1)
            return mutan
        mutan1 = buatMutan(mutan1)
        mutan2 = buatMutan(mutan2)
        # print("Mutan1 : \n", mutan1, "\n")
        # print("Mutan2 : \n", mutan2, "\n")

        #membetulkan fitness mutan
        def betulkanFitnessMutan(mutan):
            fittness = 0
            weight = 0
            for i , e in enumerate(mutan['Spesies']):
                if(mutan["Spesies"][i]) == 1:
                        weight += wItem[i]
                        fittness += vItem[i]
                mutan["Fittness"] = fittness
            if(wMax < weight):
                    mutan["Fittness"] = 0
        betulkanFitnessMutan(mutan1)
        betulkanFitnessMutan(mutan2)
        # print("Mutan1 Dengan Fittness : \n", mutan1, "\n")
        # print("Mutan2 Dengan Fittness : \n", mutan2, "\n")

        #regenerasi
        #buang 2 individu terburuk fitnessny
        listFitness = []
        for x in populasi:
            listFitness.append(x['Fittness'])
        del populasi[listFitness.index(min(listFitness))]

        listFitness = []
        for x in populasi:
            listFitness.append(x['Fittness'])
        del populasi[listFitness.index(min(listFitness))]
        # print("Populasi tanpa individu terburuk: \n", populasi, "\n")

        #masukkan individu baru(mutan ke populasi)
        populasi.append(mutan1)
        populasi.append(mutan2)
        # print("Populasi baru: \n", populasi, "\n")
        
        #ambil hasil terbaik
        listFitness = []
        weight = 0
        for x in populasi:
            listFitness.append(x['Fittness'])
        for i, x in enumerate(populasi[listFitness.index(max(listFitness))]['Spesies']):
            if x == 1:
                weight += wItem[i]
        
        # memasukkan nilai fittness dan weight terbaik per generasi untuk membuat plot perkembangan pergenerasi
        daftarFittnessTerbaikPerGenerasi.append(max(listFitness))
        daftarWeightTerbaikPerGenerasi.append(weight)
        
    #tampilkan hasil
    listBarang = []
    for i, x in enumerate(populasi[listFitness.index(max(listFitness))]['Spesies']):
        if x == 1:
            listBarang.append(namaBarang[i])
    print("\nBarang terpilih",",".join(listBarang))
    # print(populasi[listFitness.index(max(listFitness))]['Spesies'])
    print("Total Value: ", populasi[listFitness.index(max(listFitness))]['Fittness'])
    print("Total Harga: ", weight)

    # tampilkan chart perkembangan fittness value dari generasi ke generasi
    plt.plot(daftarFittnessTerbaikPerGenerasi)
    plt.ylabel("Fitness Value")
    plt.xlabel("Generation")
    plt.title("Top Fittness Per Generation")
    plt.grid()
    plt.show()

