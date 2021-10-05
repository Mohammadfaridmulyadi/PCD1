import matplotlib.pyplot as plt

nilai_siswa = ([20,15,17,80,30,35,37,38,40,75,60,95,82,45,60,87,28,67,87,70,90,87,80,66,70,75,77])
bin_width = 10
kelompok_interval = range(0,100 + bin_width,bin_width)
plt.hist(nilai_siswa,kelompok_interval)
plt.show()


