def hitungDebit(volume, waktu):
    debit = volume / waktu
    
    return debit

def hitungVolume(debit, waktu):
    volume = debit * waktu
    
    return volume

# Main
print("1. Berapa cm3/ detik debit anutan pipa air tersebut?")
print("2. Berapa liter/detik debit air  yang keluar dari pipa tersebut?")
print("3. Berapa  banyak air yang bisa dipindahkan air terjun tersebut dalam waktu 10 menit?")
print("Masukan Pilihan :")
pilihan = int(input())
if pilihan == 1:
    volume = 125 * 1000
    waktu = 50 * 60
    print("Debit air adalah " + str(hitungDebit(volume, waktu)) + " cm3/detik")
if pilihan == 2:
    volume = 40 * 1000
    waktu = 4 * 3600
    print("Debit aii yang keluar dari pipa " + str(hitungDebit(volume, waktu)) + " liter/detik")
if pilihan == 3:
    debit = 80
    waktu = 10 * 60
    print("Volumenya adalah " + str(hitungVolume(debit, waktu)) + " m3")
