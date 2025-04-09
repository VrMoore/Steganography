#  Import libraries
import os
from PIL import Image
from ast import literal_eval

class deconvertText() :

    def __init__(self, image_file_name : str, cache_path : str) -> None :
        self.image_file_name = image_file_name
        self.cache_path = cache_path

        self.image_cache = os.path.splitext(self.image_file_name)[0]
        self.img_path = f"{self.cache_path}/{self.image_cache}.bmp"

        self.text_length, self.original_keys = self.get_length()
        self.text_decryption(cache_path=self.img_path, text_length=self.text_length, original_keys=self.original_keys)

    def get_length(self) -> list[int, list] :

        md_file = 'dump.md'
        md_file_path = f'{self.cache_path}/{md_file}'

        with open(file=md_file_path, mode='r') as file :
            content = file.readlines() 

        # Get length of the secret text
        text_bin_len = content[1]
        text_bin_len = text_bin_len.rsplit('=', 1)[1]

        # Get original pixels (secret key)
        original_key = content[2]
        original_key = original_key.rsplit('=',1)[1]
        original_key = literal_eval(original_key)

        return [int(text_bin_len), original_key]

    def text_decryption(self, cache_path : str, text_length : int, original_keys : list) :
        image = Image.open(cache_path)

        # Get only blue channel
        blue_image = image.getchannel('B')
        pixels = blue_image.load()
        height, width = blue_image.size

        index = 0
        message_bits = []

        for y in range(height):
            for x in range(width):
                if index >= text_length:
                    print("Message has been decoded")
                    break

                blue_pixel = pixels[x, y]

                # Extract the LSB directly
                bit = blue_pixel & 1
                message_bits.append(str(bit))  # store as string for easier joining
                index += 1

            if index >= text_length:
                break

        self.load_text(text_bin=message_bits)


    def load_text(self, text_bin : list[int]) :
        text_bin_len = len(text_bin)
        original_text = []

        for i in range(0, text_bin_len, 8) :
            original_text.append(text_bin[i:i+8])

        message = ''

        for bit in original_text :
            char_bin = ''.join(bit)
            ascii_value = int(char_bin, 2)  #
            message += chr(ascii_value)
            print('===========',message,'=========')


        print(original_text)
