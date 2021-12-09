import base64

text = input("Masukan Teks yang Akan di Enkripsi: ").encode('utf-8')

print("===========================================")
print("MESSAGE ECRIPTOR PROCESS")
print("===========================================")

base32_encryption = base64.b32encode(text)
print("Hasil Enkripsi       : ", base32_encryption)
print("Hasil Enkripsi utf-8 : ", base32_encryption.decode('utf-8'))


print("===========================================")
print("MESSAGE DESCRIPTION PROCESS")
print("===========================================")

base32_decryption = base64.b32decode(base32_encryption)
print("Hasil Deskripsi       : ", base32_decryption)
print("Hasil Deskripsi utf-8 : ", base32_decryption.decode('utf-8'))
