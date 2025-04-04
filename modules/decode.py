#  Import libraries
import os
from PIL import Image

class deconvertText() :

    def __init__(self, image_file_name : str, cache_path : str) -> None :
        self.image_file_name = image_file_name
        self.cache_path = cache_path

        self.image_cache = os.path.splitext(self.image_file_name)[0]
        self.img_path = f"{self.cache_path}/{self.image_cache}.bmp"

        self.text_salt = self.get_text(cache_path=self.cache_path)
        self.text_decryption(cache_path=self.img_path, salt=self.text_salt)

    def get_text(self, cache_path : str) -> list[int] :
        md_file = 'dump.md'
        md_file_path = f'{cache_path}/{md_file}'

        with open(file=md_file_path, mode='r') as file :
            content = file.readlines()
        
        image_salt : list = content[1]
        image_salt_data = image_salt.rsplit('=', 1)[1]

        salt = []

        for char in image_salt_data :
            character = ord(char)
            salt.append(character)

        # remove annonying \n in the last element
        del salt[-1]

        return salt

    def text_decryption(self, cache_path : str, salt : list[int]) :
        image = Image.open(cache_path)

        # Get only blue channel
        blue_image = image.getchannel('B')
        pixels = blue_image.load()
        height, width = blue_image.size

        index : int = 0
        message : list = []
        # Iterate only left part of the image, so it can run faster
        for y in range(height) :
            for x in range(width // 2) :

                if index >= len(salt) :
                    print("Message have been decoded")
                    break

                blue_pixels = pixels[x,y]
                print(salt[index])
                decrypted_text = (blue_pixels & 0xFE) | (salt[index])
                message.append(chr(decrypted_text))
                index += 1

            if index >= len(salt) :
                break
            
        print(''.join(message))

    def print_text(self) :
        pass