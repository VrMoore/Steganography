# Convert Text into Binaries and embed it into given image
from PIL import Image
import os

class convertText :

    def __init__(self, file_name, secret_text) -> None:
        self.file_name = file_name
        self.secret_text = secret_text
        self.new_file_name = os.path.splitext(file_name)[0]
        self.save_result()

    def save_result(self) -> str:
        current_path = os.getcwd().replace(os.sep, '/')
        save_result_image_path = f"{current_path}/IMG RES"
        print(save_result_image_path)

        if os.path.isdir(save_result_image_path) :
            return save_result_image_path
        else :
            os.makedirs(save_result_image_path)
            return save_result_image_path

    def convert_to_binary(self, user_secret_text : str) -> list:
        character_bin = []
        
        for i in user_secret_text :
            char_unicode = format(ord(i),'08b')
            character_bin.append(char_unicode)
        
        return character_bin

    def convert_image(self, image_path : str) -> None :
        image = Image.open(image_path)

        if image.mode != 'RGB' :

            bg_image = Image.new('RGBA',size=image.size,color=(255,255,255,0))
            bg_image.paste(image, (0,0), image)
            bg_image = bg_image.convert('RGB')
            image = bg_image

        else :
            image = image.convert('RGB')

        image.save(f"{self.save_result()}/{self.file_name}.bmp",'BMP')

    def embed_text(self, image_path : str, secret_text : str) :
        image = Image.open(image_path)
        red_channel = image.getchannel('B')
        red_channel.save(f"{self.save_result()}/{self.file_name}--red-channel.bmp",'BMP')
                