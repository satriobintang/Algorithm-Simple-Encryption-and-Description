import string

text = string.printable

def encrypt(isi):
    global text

    key = int(input("Masukan kunci [berupa angka] : "))
    cipher = ' '
    for i in isi:
        if i in text:
            k = text.find(i)
            k = (k + key)%100
            cipher = cipher+text[k]
        
        else:
            cipher = cipher + i
    
    return cipher

def decrypt(cipher):
    global text

    key = int(input('Masukan kunci [berupa angka] : '))

    isi = ' '
    for i in cipher:
        if i in text:
            k = text.find(i)
            k = (k - key)%100
            isi = isi+text[k]
        
        else:
            isi = isi + i 
    
    return isi

if __name__ == '__main__':
    print("==================================")
    print("Message Encryption and Description")
    print("==================================")

    mode = int(input('1. Enkripsi \n2. Deskripsi \nPilih : '))

    if mode == 1:
        isi = input("Masukan isi : ")
        print("Hasil Enkripsi :",encrypt(isi))
    
    elif mode == 2:
        cipher = input("Masukan Isi : ")
        print("Hasil Deskripsi :",decrypt(cipher))
    
    else:
        print("Pilih 1. Enkripsi atau 2. Deskripsi!!")
