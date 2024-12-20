#NAMA : AISHA MABELINA
#NIM : 06500240026

import pandas as pd

file_path = "Negara.csv"  # Ganti dengan path file Anda
data = pd.read_csv(file_path)

# Menampilkan data frame
print("Berikut Data Frame:")
print(data)

# Menghitung mean dan standar deviasi per benua
mean_data = data.groupby('Benua')[['Luas', 'Populasi']].mean()
std_data = data.groupby('Benua')[['Luas', 'Populasi']].std()

# Menampilkan mean
print("\nBerikut Data Mean:")
print(mean_data)

# Menampilkan standar deviasi
print("\nBerikut Data Standard Deviation:")
print(std_data)
