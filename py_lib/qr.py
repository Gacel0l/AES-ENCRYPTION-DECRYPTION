import argparse
import qrcode

def QrGen(data, name):
    img = qrcode.make(data)
    img.save(name)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generating QR codes')
    parser.add_argument('--data','-d', type=str, help='data to be placed in the QR code')
    parser.add_argument('--name','-n', type=str, help='result file name')
    args = parser.parse_args()

    if args.data and args.name:
        QrGen(args.data, args.name)
    else:
        print('Specify the data and file name with the -data and -name or -d -n arguments')