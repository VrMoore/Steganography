# Convert Text into Binaries and embed it into given image
from PIL import Image
import os

class convertText :

    def __init__(self) :
        self.user_secret_text = input('Input your text : ')
        self.convert_to_binary(user_secret_text=self.user_secret_text)

    def convert_to_binary(self, user_secret_text : str) -> list:
        character_bin = []
        
        for i in user_secret_text :
            char_unicode = format(ord(i),'08b')
            character_bin.append(char_unicode)
        
        return character_bin

    def convert_image(self, image_path, file_name) :
        image = Image.open(image_path)
        new_file_name = os.path.splitext(file_name)[0]

        if image.mode != 'RGB' :
            # Background remover doesnt work as intended

            bg_image = Image.new('RGBA',size=image.size,color=(255,255,255,0))
            bg_image.paste(image, (0,0), image)
            bg_image = bg_image.convert('RGB')
            image = bg_image

            image.save(f"{new_file_name}.bmp",'BMP')
        else :
            image = image.convert('RGB')
            image.save(f"{new_file_name}.bmp",'BMP')

    def embed_text(self) :
        pass