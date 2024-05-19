def cek_palindrom(kata):
    kata_reversed = kata[::-1]
    if kata == kata_reversed:
        return f"{kata} adalah palindrom"
    else:
        return f"{kata} bukan palindrom"

kata = "level"
hasil_cek = cek_palindrom(kata)
print(hasil_cek)

