from GeneticAlgorithmForCafeItemChoosing import main
import time

modalMaximal = 10000000
namaBarang = ["Lampu Hias", "Meja Makan", "Vas Bunga", "Sofa", "TV", "Bar", "Speaker", "Panggung Live Music", "Radio", "Tempat Bermain Anak2", "Toilet", "Meja Biliard"]
valuePerBarang = [10, 40, 7, 20, 5, 35, 40, 30, 3, 2, 40, 23]
hargaPerBarang = [1000000, 2000000, 4000000, 1500000, 4500000, 5000000, 2000000, 5000000, 1700000, 6000000, 2000000, 6000000]
jumlahGenerasi = 1000
mutationRate = 0.1

start_time = time.time()
main(modalMaximal, namaBarang, valuePerBarang, hargaPerBarang, jumlahGenerasi, mutationRate)
print("Time : %6f seconds" % (time.time() - start_time)) #print waktu yang dibutuhkan