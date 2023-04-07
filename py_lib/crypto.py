import argparse
import os
from pathlib import Path
from tqdm import tqdm
from Crypto.Cipher import AES


def encrypt_file(key, in_file, out_file):
    """Encrypts a file using AES encryption"""
    chunk_size = 64 * 1024
    iv = os.urandom(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    file_size = Path(in_file).stat().st_size

    with open(in_file, 'rb') as infile:
        with open(out_file, 'wb') as outfile:
            outfile.write(iv)

            with tqdm(total=file_size, unit='B', unit_scale=True, desc='Encrypting') as pbar:
                while True:
                    chunk = infile.read(chunk_size)
                    if len(chunk) == 0:
                        break
                    elif len(chunk) % 16 != 0:
                        chunk += b' ' * (16 - len(chunk) % 16)

                    outfile.write(cipher.encrypt(chunk))
                    pbar.update(len(chunk))


def decrypt_file(key, in_file, out_file):
    """Decrypts a file using AES decryption"""
    chunk_size = 64 * 1024

    with open(in_file, 'rb') as infile:
        iv = infile.read(16)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        file_size = Path(in_file).stat().st_size - 16

        with open(out_file, 'wb') as outfile:
            with tqdm(total=file_size, unit='B', unit_scale=True, desc='Decrypting') as pbar:
                while True:
                    chunk = infile.read(chunk_size)
                    if len(chunk) == 0:
                        break

                    outfile.write(cipher.decrypt(chunk))
                    pbar.update(len(chunk))

            outfile.truncate(file_size)


def main():
    parser = argparse.ArgumentParser(description="AES encryption/decryption script")
    parser.add_argument("-k", "--key", required=True, help="Key for encryption/decryption")
    parser.add_argument("mode", choices=["encrypt", "decrypt"], help="Encryption or decryption mode")
    parser.add_argument("-f", "--file", help="Input file location")
    parser.add_argument("-o", "--output", help="Output file location")
    parser.add_argument("-d", "--dir", help="Directory to encrypt/decrypt")
    parser.add_argument("-disk", help="Disk to encrypt/decrypt")
    args = parser.parse_args()

    key = args.key.encode('utf-8')
    mode = args.mode
    in_file = args.file
    out_file = args.output
    directory = args.dir
    disk = args.disk

    if disk:
        if os.path.isdir(disk):
            for root, dirs, files in os.walk(disk):
                for file in files:
                    file_path = os.path.join(root, file)
                    out_path = os.path.join(root, f"{os.path.splitext(file)[0]}_{mode}{os.path.splitext(file)[1]}")
                    if mode == 'encrypt':
                        encrypt_file(key, file_path, out_path)
                        os.remove(file_path)
                    else:
                        decrypt_file(key, file_path, out_path)
                        os.remove(file_path)
        else:
            print(f"Invalid disk: {disk}")
    else:
        if directory:
            for root, dirs, files in os.walk(directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    out_path = os.path.join(root, f"{os.path.splitext(file)[0]}_{mode}{os.path.splitext(file)[1]}")
                    if mode == 'encrypt':
                        encrypt_file(key, file_path, out_path)
                        os.remove(file_path)
                    else:
                        decrypt_file(key, file_path, out_path)
                        os.remove(file_path)
        else:
            if mode == 'encrypt':
                out_file = f"{os.path.splitext(in_file)[0]}_{mode}{os.path.splitext(in_file)[1]}"
                encrypt_file(key, in_file, out_file)
            else:
                out_file = f"{os.path.splitext(in_file)[0]}_{mode}{os.path.splitext(in_file)[1]}"
                decrypt_file(key, in_file, out_file)





if __name__ == '__main__':
    print("\n supported keys length: 16, 24, 32 \n")
    main()
