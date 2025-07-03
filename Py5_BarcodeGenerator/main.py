import barcode
from barcode.writer import ImageWriter
import os


def generate_barcode(data, filename):
    code128=barcode.get_barcode_class('code128')
    barcode_instance=code128(data, writer=ImageWriter())

    try:
        barcode_instance.save(filename)
        print(f'Barcode saved as {filename}.png')
    except Exception as e:
        print(f'Failed to save barcode:{e}')

def main():
    directory='Collection/barcode generator'
    if not os.path.exists(directory):
        os.makedirs(directory)


    data=input('Enter the data for the barcode: ')
    filename=os.path.join(directory, 'barcode')

    generate_barcode(data, filename)
if __name__=="__main__":
    main()