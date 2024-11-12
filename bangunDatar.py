import math

# Fungsi untuk mencari panjang Persegi Panjang jika yang diketahui hanya lebar, luas, atau keliling
def cari_panjang(lebar=None, luas=None, keliling=None):
    if lebar is not None and luas is not None:
        return round(luas / lebar, 2)
    elif keliling is not None and lebar is not None:
        return round((keliling / 2) - lebar, 2)
    elif keliling is not None and luas is not None:
        lebar = keliling / 2 - (luas / (keliling / 2))
        return round(lebar, 2)
    return "Data tidak lengkap"

# Fungsi untuk mencari lebar Persegi Panjang jika yang diketahui hanya panjang, luas, atau keliling
def cari_lebar(panjang=None, luas=None, keliling=None):
    if panjang is not None and luas is not None:
        return round(luas / panjang, 2)
    elif keliling is not None and panjang is not None:
        return round((keliling / 2) - panjang, 2)
    elif keliling is not None and luas is not None:
        panjang = keliling / 2 - (luas / (keliling / 2))
        return round(panjang, 2)
    return "Data tidak lengkap"

# Fungsi untuk mencari sisi Persegi jika yang diketahui hanya luas atau keliling
def cari_sisi_persegi(luas=None, keliling=None):
    if luas is not None:
        return round(math.sqrt(luas), 2)
    elif keliling is not None:
        return round(keliling / 4, 2)
    return "Data tidak lengkap"

# Fungsi untuk mencari radius Lingkaran jika yang diketahui hanya luas atau keliling
def cari_radius(luas=None, keliling=None):
    if luas is not None:
        return round(math.sqrt(luas / math.pi), 2)
    return "Data tidak lengkap"

# Fungsi untuk memastikan input adalah angka yang valid
def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Angka tidak boleh negatif.")
                continue
            return value
        except ValueError:
            print("Input tidak valid, harap masukkan angka.")

# Fungsi utama untuk memilih bentuk dan melakukan perhitungan
def main():
    while True:
        print("\nPilih bentuk yang ingin dihitung:")
        print("1. Persegi Panjang")
        print("2. Persegi")
        print("3. Lingkaran")
        print("4. Keluar")
        
        pilihan = input("Masukkan pilihan (1-4): ")
        
        if pilihan == '1':
            print("Menghitung Persegi Panjang")
            lebar = get_float_input("Masukkan lebar (0 jika tidak diketahui): ")
            panjang = get_float_input("Masukkan panjang (0 jika tidak diketahui): ")
            luas = get_float_input("Masukkan luas (0 jika tidak diketahui): ")
            keliling = get_float_input("Masukkan keliling (0 jika tidak diketahui): ")
            
            # Menentukan panjang atau lebar berdasarkan input
            if lebar == 0 and luas != 0 and keliling != 0:
                panjang_result = cari_panjang(lebar=None, luas=luas, keliling=keliling)
                print(f"Panjang Persegi Panjang: {panjang_result}")
            elif panjang == 0 and luas != 0 and keliling != 0:
                lebar_result = cari_lebar(panjang=None, luas=luas, keliling=keliling)
                print(f"Lebar Persegi Panjang: {lebar_result}")
            elif luas == 0 and lebar != 0 and keliling != 0:
                luas_result = round(lebar * keliling / 2, 2)
                print(f"Luas Persegi Panjang: {luas_result}")
            elif keliling == 0 and lebar != 0 and panjang != 0:
                keliling_result = round(2 * (lebar + panjang), 2)
                print(f"Keliling Persegi Panjang: {keliling_result}")
            else:
                print("Data tidak cukup atau tidak valid untuk perhitungan.")
            
        elif pilihan == '2':
            print("Menghitung Persegi")
            luas = get_float_input("Masukkan luas (0 jika tidak diketahui): ")
            keliling = get_float_input("Masukkan keliling (0 jika tidak diketahui): ")
            
            if luas == 0 and keliling != 0:
                sisi_result = cari_sisi_persegi(luas=None, keliling=keliling)
                print(f"Sisi Persegi: {sisi_result}")
            elif keliling == 0 and luas != 0:
                sisi_result = cari_sisi_persegi(luas=luas, keliling=None)
                print(f"Sisi Persegi: {sisi_result}")
            else:
                print("Data tidak cukup atau tidak valid untuk perhitungan.")
        
        elif pilihan == '3':
            print("Menghitung Lingkaran")
            luas = get_float_input("Masukkan luas (0 jika tidak diketahui): ")
            keliling = get_float_input("Masukkan keliling (0 jika tidak diketahui): ")
            
            if luas == 0 and keliling != 0:
                radius_result = cari_radius(luas=None, keliling=keliling)
                print(f"Radius Lingkaran: {radius_result}")
            elif keliling == 0 and luas != 0:
                radius_result = cari_radius(luas=luas, keliling=None)
                print(f"Radius Lingkaran: {radius_result}")
            else:
                print("Data tidak cukup atau tidak valid untuk perhitungan.")
        
        elif pilihan == '4':
            print("Terima kasih! Program dihentikan.")
            break
        
        else:
            print("Pilihan tidak valid!")

# Memanggil fungsi utama untuk menjalankan program
main()