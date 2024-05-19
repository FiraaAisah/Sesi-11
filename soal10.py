def cek_anagram(kata1, kata2):
    kata1 = kata1.lower().replace(" ", "")
    kata2 = kata2.lower().replace(" ", "")
    
    urut_kata1 = sorted(kata1)
    urut_kata2 = sorted(kata2)
    return urut_kata1 == urut_kata2

kata1 = "listen"
kata2 = "silent"
hasil = cek_anagram(kata1, kata2)
print(hasil)
