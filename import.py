import tugas

def main():
  bil1 = 17
  bil2 = 3
  
  jumlah = tugas.penjumlahan(bil1, bil2)
  print ("PENJUMLAHAN")
  print ("Hasil\t: ", jumlah)
  
  kurang = tugas.pengurangan(bil1, bil2)
  print ("PENGURANGAN")
  print ("Hasil\t: ", kurang)
  
  bagi = tugas.pembagian(bil1, bil2)
  print ("PEMBAGIAN")
  print ("Hasil\t: ", bagi)
  
  kali = tugas.perkalian(bil1, bil2)
  print ("PERKALIAN")
  print ("Hasil\t: ", kali)
  
if __name__ == "__main__":
  main()
