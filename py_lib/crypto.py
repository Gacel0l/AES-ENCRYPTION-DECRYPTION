import argparse
import os
from Crypto.Cipher import AES


parser = argparse.ArgumentParser(description="AES encryption/decryption script")
parser.add_argument("-k", "--key", required=True, help="Key for encryption/decryption")
parser.add_argument("mode", choices=["encrypt", "decrypt"], help="Encryption or decryption mode")
parser.add_argument("-f", "--file", help="Input file location")
parser.add_argument("-o", "--output", help="Output file location")
args = parser.parse_args()

if not args.file:
    args.file = input("Podaj nazwę pliku wejściowego: ")

key = args.key.encode().ljust(16, b'\0')

with open(args.file, "rb") as f:
    plaintext = f.read()

if args.mode == "encrypt":
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(plaintext)
    nonce = cipher.nonce
    output_file = args.output or f"{os.path.splitext(args.file)[0]}.psf"
    with open(output_file, "wb") as f:
        [f.write(x) for x in (nonce, tag, ciphertext)]
    print(f"Zaszyfrowany plik zapisany w: {output_file}")
else:
    nonce, tag, ciphertext = [None]*3
    with open(args.file, "rb") as f:
        nonce, tag, ciphertext = [f.read(x) for x in (16, 16, -1)]
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    output_file = args.output or f"{os.path.splitext(args.file)[0]}_decrypted.dpsf"
    with open(output_file, "wb") as f:
        f.write(plaintext)
    print(f"Odszyfrowany plik zapisany w: {output_file}")
