# Decrypted_code.py
from cryptography.fernet import Fernet


# 8/14/2025
# Decrypted Code
# AUX-441


def decrypt_file_inplace(file_path, fernet):
    try:
        with open(file_path, "rb") as f:

            data = f.read()
        decrypted = fernet.decrypt(data)
        with open(file_path, "wb") as f:
            f.write(decrypted)
        print(f"Decrypted in-place: {file_path}")
    except Exception as e:
        print(f"Failed to decrypt {file_path}: {e}")

def decrypt_files_parallel(file_list, fernet):

    from concurrent.futures import ThreadPoolExecutor
    with ThreadPoolExecutor() as executor:
        executor.map(lambda f: decrypt_file_inplace(f, fernet), file_list)

def start_decryption(file_list):

    while True:
        ans = input("Do you want to decrypt files? (yes/no): ").strip().lower()
        if ans == "no":
            print("Exiting decryption...")
            break
        elif ans == "yes":
            user_key = input("Enter the decryption key: ").strip()
            try:
                fernet_decrypt = Fernet(user_key.encode())
            except Exception:
                print("Invalid key format!")
                continue

            print("Starting decryption...")
            decrypt_files_parallel(file_list, fernet_decrypt)
            print("Decryption finished.")
            break




