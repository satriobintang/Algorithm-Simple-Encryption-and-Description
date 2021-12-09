import base64

text = input("Masukan Teks yang Akan di Enkripsi: ").encode('utf-8')

print("===========================================")
print("MESSAGE ECRIPTOR PROCESS")
print("===========================================")

base64_encryption = base64.b64encode(text)
print("Hasil Enkripsi       : ", base64_encryption)
print("Hasil Enkripsi utf-8 : ", base64_encryption.decode('utf-8'))


print("===========================================")
print("MESSAGE DESCRIPTION PROCESS")
print("===========================================")

base64_decryption = base64.decodebytes(base64_encryption)
print("Hasil Deskripsi       : ", base64_decryption)
print("Hasil Deskripsi utf-8 : ", base64_decryption.decode('utf-8'))
