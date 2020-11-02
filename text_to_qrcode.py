# Filename: text_to_qrcode.py
# Description: Takes a text file and produces a series of bitmaps
#
# Created by: Benjamin M. Singleton
# Created: 07-21-2016
# Modified:

import os, sys
import qrcode

OUTPUT_BASE_NAME = 'out'
CHARACTERS_PER_CODE = 2000
TARGET_PATH = os.getcwd()


def text_to_qr(text, target_filename):
    """
	Takes a string of text, CHARACTERS_PER_CODE letters or shorter, generates a
	QR code of it, and saves it as a bitmap with the given filename.
    :param text: The text to encode in a QR code.
    :type text: str
    :param target_filename: The name to save the bitmap under.
    :type target_filename: str
    :return: None
	:rtype: None
    """
    my_image = qrcode.make(text)
    my_image.save(target_filename)


def batch_text_to_qr(text_list):
    """
	Take a list of strings, generates a series of QR codes, and saves them as
	bitmaps.
    :param text_list: The list of strings to put in QR codes.
    :type text_list: list
    :return: None
	:rtype: None
    """
    for i in range(0, len(text_list)):
        text_to_qr(text_list[i], os.path.join(TARGET_PATH, OUTPUT_BASE_NAME + str(i) + '.bmp'))


def file_to_qr(filename):
    """
	Takes a given text file, transforms its contents into QR codes, and saves 
	them as bitmaps.
    :param filename: The filename of the file to process.
    :type filename: str
    :return: None
	:rtype: None
    """
    with open(filename, 'r') as f:
        contents = f.read()

    text_list = []
    while len(contents) > 0:
        text_list.append(contents[:CHARACTERS_PER_CODE])
        try:
            contents = contents[CHARACTERS_PER_CODE:]
        except:
            break

    print 'Created text_list of ' + str(len(text_list)) + ' sections.'
    return text_list

    
def main():
    my_text_list = file_to_qr('in.txt')
    batch_text_to_qr(my_text_list)


if __name__ == '__main__':
    main()

