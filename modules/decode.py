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

        self.text_salt, self.text_bin = self.get_text(cache_path=self.cache_path)
        self.text_decryption(cache_path=self.img_path, salted=self.text_salt, ori_salt=self.text_bin)

    def get_text(self, cache_path : str) -> list :
        md_file = 'dump.md'
        md_file_path = f'{cache_path}/{md_file}'

        with open(file=md_file_path, mode='r') as file :
            content = file.readlines()
        
        text_bin : list = content[1]
        text_bin : list = text_bin.rsplit('=', 1)[1]

        text_bin =text_bin[:-1]

        image_salt : list = content[2]
        image_salt_data : list = image_salt.rsplit('=', 1)[1]

        # Turn into list data type
        image_salt_data = literal_eval(image_salt_data)

        return [image_salt_data, text_bin]

    def text_decryption(self, cache_path : str, salted : list[int], ori_salt : str) :
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

                if index >= len(ori_salt) :
                    print("Message have been decoded")
                    break

                blue_pixels = pixels[x,y]

                decrypted_text = blue_pixels & 1

                original_text_bin = decrypted_text ^ int(ori_salt[index])

                message.append(original_text_bin)
                
                # decrypted_text = (blue_pixels & 0xFE) | ((salt[index]) ^ (int(text_bin[index])))
                # print(decrypted_text, 'decrypted')  
                # message.append(chr(decrypted_text))
                index += 1

            if index >= len(ori_salt) :
                break
            
        self.load_text(text_bin=message)

        return None

    def load_text(self, text_bin : list[int]) :
        text_bin_len = len(text_bin)
        original_text = []

        for i in range(0, text_bin_len, 8) :
            original_text.append(text_bin[i:i+8])

        message = ''

        for byte in original_text :
            binary_str = ''.join(str(bit) for bit in byte)
            ascii_value = int(binary_str, 2)
            message += chr(ascii_value)

        print(message)