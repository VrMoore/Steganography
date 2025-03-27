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

    def embed_text(self, image_path, file_name) :
        image = Image.open(image_path)

        if image.mode != 'RGB' :
            image = image.convert('RGB')
            new_file_name = os.path.splitext(file_name)[0]
            image.save(f"{new_file_name}.jpeg",'JPEG')

        