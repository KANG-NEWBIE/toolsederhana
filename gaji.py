import os
import sys
def pindah(label):
 global nomor
 nomor = label

def keluar():
 sys.exit()

def rumus():
 global anak, gapok, gajikotor, hitunglembur, hitunganak, persen, total
 anak = 200000
 hitunglembur = jumlem * lembur
 if jumanak > 3 :
  hitunganak = 3 * anak
 else :
  hitunganak = jumanak * anak
  gajikotor = gapok + hitunglembur + hitunganak
  persen = (gajikotor * 5) / 100
  total = gajikotor - persen

def cetak():
 print "========================================="
 print "      Aplikasi Penggajian Karyawan"
 print "========================================="
 print "| Nama : ", nama
 print "| NIP : ", nip
 print "| Jabatan : " , jabatan
 print "| Gaji Gaji Kotor adalah : Rp. ", gajikotor
 print "| Potongan 5% : Rp. ", persen
 print ""
 print "=>> Gaji Bersih adalah : Rp. ", total
 print ""

nomor = 0

while True :

 if nomor == 0 :
  print "----------------------------"
  print "Aplikasi Penggajian Karyawan"
  print "----------------------------"
  print ""
  nama = raw_input("Masukkan nama : ")
  nip = raw_input("Masukkan NIP : ")
  print "KET: golongan\n1 Direktur\n2 Manajer\n3 Supervisor\n4 Oprator"
  golongan = int(raw_input("Golongan : "))
  jumanak = int(raw_input("Jumlah Anak : "))
  jumlem = int(raw_input("Jumlah Lembur : "))
  if golongan == 1 :
   pindah(1)
  elif golongan == 2 :
   pindah(2)
  elif golongan == 3 :
   pindah(3)
  elif golongan == 4 :
   pindah(4)
  else :
   pindah(0)

 elif nomor == 1 :
  jabatan = "Direktur"
  gapok = 8000000
  lembur = 100000
  rumus()
  cetak()
  break

 elif nomor == 2 :
  jabatan = "Manajer"
  gapok = 6000000
  lembur = 80000
  rumus()
  cetak()
  break

 elif nomor == 3 :
  jabatan = "Superviser"
  gapok = 4000000
  lembur = 60000
  rumus()
  cetak()
  break

 elif nomor == 4 :
  jabatan = "Operator"
  gapok = 2000000
  lembur = 40000
  rumus()
  cetak()
  break

 else :
  keluar()
