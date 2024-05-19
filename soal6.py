def hitung_jumlah_kata(kalimat):
    kata_kalimat = kalimat.split()
    jumlah_kata = len(kata_kalimat)
    return jumlah_kata

kalimat = "Ini adalah contoh kalimat"
jumlah_kata = hitung_jumlah_kata(kalimat)
print(jumlah_kata)
