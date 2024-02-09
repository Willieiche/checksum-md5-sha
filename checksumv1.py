import hashlib
def calculate_cecksum_sha512(filename):
    with open(filename, "rb") as file:
        hash512 = hashlib.sha512(file.read()).hexdigest()
        print("--------------------------------------------------------------------------------------------------------------------------")
        print(f"Der SHA-512 Hash ist: {hash512}")
        print("--------------------------------------------------------------------------------------------------------------------------")
        if (hash512 == filename2):
            print("--Sind Gleich--")
        else:
            print("--Sind Ungleich / Nicht Gleich--")
def calculate_cecksum_sha256(filename):
    with open(filename, "rb") as file:
        hashsha256 = hashlib.sha256(file.read()).hexdigest()
        print("--------------------------------------------------------------------------------------------------------------------------")
        print(f"Der SHA-256 Hash ist: {hashsha256}")
        print("--------------------------------------------------------------------------------------------------------------------------")
        if (hashsha256 == filename2):
            print("--Sind Gleich--")
        else:
            print("--Sind Ungleich / Nicht Gleich--")
def calculate_cecksum_sha1(filename):
    with open(filename, "rb") as file:
        hashsha1 = hashlib.sha1(file.read()).hexdigest()
        print("--------------------------------------------------------------------------------------------------------------------------")
        print(f"Der SHA-1 Hash ist: {hashsha1}")
        print("--------------------------------------------------------------------------------------------------------------------------")
        if (hashsha1 == filename2):
            print("--Sind Gleich--")
        else:
            print("--Sind Ungleich / Nicht Gleich--")
def calculate_cecksum_md5(filename):
    with open(filename, "rb") as file:
        hashmd5 = hashlib.md5(file.read()).hexdigest()
        print("--------------------------------------------------------------------------------------------------------------------------")
        print(f"Der MD5 Hash ist: {hashmd5}")
        print("--------------------------------------------------------------------------------------------------------------------------")
        if (hashmd5 == filename2):
            print("--Sind Gleich--")
        else:
            print("--Sind Ungleich / Nicht Gleich--")





Operation = 2

while Operation > 1:
    Operation = int(input("Möchtest du das Programm ausfürhren?: --1)Nein --2)Sha512 --3)Sha256 --4)Sha1 --5)Md5: "))
    if Operation == 1:
        break
    elif (Operation == 2):
        filename = input("Gebe den Pfad (Sha512): ")
        filename2 = input("Geben sie den Vorhanden SHA-512 ein: ")
        print(calculate_cecksum_sha512(filename))
    elif (Operation == 3):
        filename = input("Gebe den Pfad an (Sha256): ")
        filename2 = input("Geben sie den Vorhanden SHA-256 ein: ")
        print(calculate_cecksum_sha256(filename))
    elif (Operation == 4):
        filename = input("Gebe den Pfad an (Sha1): ")
        filename2 = input("Geben sie den Vorhanden SHA-1 ein: ")
        print(calculate_cecksum_sha1(filename))
    elif (Operation == 5):
        filename = input("Gebe den Pfad an (MD5): ")
        filename2 = input("Geben sie den Vorhanden MD5 ein: ")
        print(calculate_cecksum_md5(filename))
    else:
        print("Hash Variante nicht unterstüzt.")
    