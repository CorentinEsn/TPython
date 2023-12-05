import getpass
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

import hashlib
from tkinter import Tk, Label, Entry, Button, StringVar
import Chiffrement

# Hasher un fichier en un nouveau fichier crypter avec le mot de passe issus de la fonction getpass
def hash_file(filename):
    try:
        fichier_non_chiffre = input("Enter the name of the file: ")
        fichier_chiffre = fichier_non_chiffre + ".hashed"
        login = input("Enter your login: ")
        password = input("Enter your password: ")
        salted_password = Chiffrement.add_salt(password, login)
        hashed_password = hashlib.sha256(salted_password.encode()).hexdigest()
        with open(fichier_non_chiffre, "r") as file:
            with open(fichier_chiffre, "w") as hashed_file:
                for line in file:
                    hashed_file.write(Chiffrement.add_salt(hashlib.sha256(line.encode()).hexdigest(), hashed_password) + "\n")
    except FileNotFoundError:
        print(f"Le fichier '{filename}' n'a pas été trouvé.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
    finally:
        print("Opération terminée.")

# Déchiffrer un fichier crypter en un nouveau fichier non crypter avec le mot de passe issus de la fonction getpass
def unhash_file(filename):
    try:
        fichier_chiffre = input("Enter the name of the file: ")
        fichier_non_chiffre = fichier_chiffre + "_unhashed"
        login = input("Enter your login: ")
        password = input("Enter your password: ")
        salted_password = Chiffrement.add_salt(login,password)
        hashed_password = hashlib.sha256(salted_password.encode()).hexdigest()

        with open(fichier_chiffre, "r") as file:
            with open(fichier_non_chiffre, "w") as hashed_file:
                for line in file:
                    hashed_file.write(AES.new(hashed_password, AES.MODE_EAX).encrypt_and_digest(hashed_password) + "\n")
                    hashed_file.write(Chiffrement.remove_salt(line, hashed_password) + "\n")

    except FileNotFoundError:
        print(f"Le fichier '{filename}' n'a pas été trouvé.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
    finally:
        print("Opération terminée.")

#hash_file("fichier_non_chiffre.txt")
unhash_file("fichier_non_chiffre.txt_hashed")