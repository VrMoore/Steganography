# Convert Text into Binaries and embed it into given image
from PIL import Image
import os

class convertText :

    def __init__(self) :
        pass

    def convert_to_binary(self, user_secret_text : str) -> list:
        character_bin = []
        
        for i in user_secret_text :
            char_unicode = format(ord(i),'08b')
            character_bin.append(char_unicode)
        
        return character_bin

    def convert_image(self, image_path : str, file_name : str) -> None :
        image = Image.open(image_path)
        new_file_name = os.path.splitext(file_name)[0]

        if image.mode != 'RGB' :

            bg_image = Image.new('RGBA',size=image.size,color=(255,255,255,0))
            bg_image.paste(image, (0,0), image)
            bg_image = bg_image.convert('RGB')
            image = bg_image

        else :
            image = image.convert('RGB')

        image.save(f"{new_file_name}.bmp",'BMP')

    def embed_text(self, image_path : str, secret_text : str) :
        image = Image.open(image_path)
        print(image.size)
        print(image.load())