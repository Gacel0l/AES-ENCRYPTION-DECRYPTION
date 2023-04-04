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
    args = parser.parse_args()

    key = args.key.encode('utf-8')
    mode = args.mode
    in_file = args.file
    out_file = args.output

    if mode == 'encrypt':
        encrypt_file(key, in_file, out_file)
    else:
        decrypt_file(key, in_file, out_file)


if __name__ == '__main__':
    main()
