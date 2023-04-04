import argparse
import os
from Crypto.Cipher import AES
from tqdm import tqdm

def get_file_size(file_path):
    """Returns the size of a file in bytes"""
    return os.stat(file_path).st_size

def encrypt_file(key, input_file_path, output_file_path):
    """Encrypts a file using the provided key and saves the result to the output file"""
    key = key.encode('utf-8')
    file_size = get_file_size(input_file_path)
    progress_bar = tqdm(total=file_size, unit='B', unit_scale=True, desc='Encrypting', position=0)
    with open(input_file_path, 'rb') as f:
        with open(output_file_path, 'wb') as out_f:
            cipher = AES.new(key, AES.MODE_EAX)
            # write nonce to output file
            out_f.write(cipher.nonce)
            tag = None
            while True:
                chunk = f.read(1024 * 1024)
                if not chunk:
                    break
                # encrypt chunk of data and write to output file
                ciphertext_chunk, tag = cipher.encrypt_and_digest(chunk)
                out_f.write(ciphertext_chunk)
                progress_bar.update(len(chunk))
            # write tag to output file
            out_f.write(tag)
            progress_bar.close()

def decrypt_file(key, input_file_path, output_file_path):
    """Decrypts a file using the provided key and saves the result to the output file"""
    key = key.encode()
    file_size = get_file_size(input_file_path)
    progress_bar = tqdm(total=file_size, unit='B', unit_scale=True, desc='Decrypting', position=0)
    with open(input_file_path, 'rb') as f:
        # read nonce from input file
        nonce = f.read(16)
        cipher = AES.new(key, AES.MODE_EAX)
        tag = f.read(16)
        with open(output_file_path, 'wb') as out_f:
            while True:
                chunk = f.read(1024 * 1024)
                if not chunk:
                    break
                # decrypt chunk of data and write to output file
                plaintext_chunk = cipher.decrypt(chunk)
                out_f.write(plaintext_chunk)
                progress_bar.update(len(chunk))
            try:
                cipher.verify(tag)
            except ValueError:
                print('\033[91m[-]\033[00m Decryption failed. The provided key may be incorrect.')
            progress_bar.close()

def main():
    parser = argparse.ArgumentParser(description="AES encryption/decryption script")
    parser.add_argument("-k", "--key", required=True, help="Key for encryption/decryption")
    parser.add_argument("mode", choices=["encrypt", "decrypt"], help="Encryption or decryption mode")
    parser.add_argument("-f", "--file", help="Input file location")
    parser.add_argument("-o", "--output", help="Output file location")

    args = parser.parse_args()

    if not args.file:
        args.file = input("File location? ")

    if not args.output:
        args.output = input("Output file name? ")

    if args.mode == "encrypt":
        encrypt_file(args.key, args.file, args.output)
        print(f"\033[94m[*]\033[00m The encrypted file saved in: \033[1m{args.output}\033[0m")
    else:
        decrypt_file(args.key, args.file, args.output)
        print(f"\033[94m[*]\033[00m The decrypted file saved in: \033[1m{args.output}\033[0m")

if __name__ == '__main__':
    print("supported AES key length: 16, 24, 32")
    main()
