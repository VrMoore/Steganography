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

        self.text_length = self.get_length()
        self.text_decryption(cache_path=self.img_path, text_length=self.text_length)

    def get_length(self) :

        md_file = 'dump.md'
        md_file_path = f'{self.cache_path}/{md_file}'

        with open(file=md_file_path, mode='r') as file :
            content = file.readlines() 

        text_bin_len = content[1]
        text_bin_len = text_bin_len.rsplit('=', 1)[1]

        return int(text_bin_len)

    def text_decryption(self, cache_path : str, text_length : int) :
        image = Image.open(cache_path)

        # Get only blue channel
        blue_image = image.getchannel('B')
        pixels = blue_image.load()
        height, width = blue_image.size

        index : int = 0
        message : list = []

        # Iteratee from the left top
        for y in range(height) :
            for x in range(width) :

                if index >= text_length * 8 :
                    print("Message have been decoded")
                    break

                blue_pixels = pixels[x,y]

                decrypted_text = blue_pixels ^ 1

                decrypted_text_bin = f"{decrypted_text:08b}"

                message.append(decrypted_text_bin[-1])

                index += 1

            if index >= text_length * 8:
                break
            
        self.load_text(text_bin=message)

        print(message)

        return None

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
