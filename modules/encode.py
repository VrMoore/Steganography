# Convert Text into Binaries and embed it into given image
from PIL import Image
import os

class convertText :

    def __init__(self, file_name, secret_text) -> None:
        self.file_name = file_name
        self.secret_text = secret_text
        self.new_file_name = os.path.splitext(file_name)[0]

        self.current_path = os.getcwd().replace(os.sep, '/')
        self.save_result_image_path = f"{self.current_path}/IMG RES"
        self.save_result(image_path=self.save_result_image_path)

    def save_result(self, image_path) -> None:
        os.makedirs(name=image_path, exist_ok=True)

    def convert_to_ascii(self, user_secret_text : str) -> list[int]:
        character_bin = []
        
        for i in user_secret_text :
            char_unicode = ord(i)
            character_bin.append(char_unicode)
        
        encrypted_data = self.text_encryption(secret_text=character_bin)
        return encrypted_data

    def text_encryption(self, secret_text : list[int]) -> list[int]:
        secret_text_length = len(secret_text)

        salt = os.urandom(secret_text_length)
        salt = list(salt)

        encrypt = [x ^ salt[i] for i,x in enumerate(secret_text)]
        self.write_data(salt=salt)
        return encrypt

    def write_data(self, salt : list[int]) -> None :
        file_name = 'dump.md'
        file_name_path = f"{self.save_result_image_path}/dump.md"

        with open(file=file_name_path, mode='w') as file : 
            file.write(f"FILE_NAME = {self.new_file_name}.bmp\n")
            file.write(f"SECRET_TEXT = {self.secret_text}\n")
            file.write(F"SALT = {salt}")

    def convert_image(self, image_path : str) -> None :
        image = Image.open(image_path)

        if image.mode != 'RGB' :

            bg_image = Image.new('RGBA',size=image.size,color=(255,255,255,0))
            bg_image.paste(image, (0,0), image)
            bg_image = bg_image.convert('RGB')
            image = bg_image

        else :
            image = image.convert('RGB')

        image.save(f"{self.save_result_image_path}/{self.new_file_name}.bmp",'BMP')

    def embed_text(self, image_path : str,secret_text : str) :
        image = Image.open(image_path)

        red_channel, green_channel, blue_channel = image.split()

        blue_image = blue_channel.copy()
        pixels = blue_image.load()
        width, height  = blue_channel.size

        secret_text_data = self.convert_to_ascii(user_secret_text=secret_text) 
        index = 0
        message_length = len(secret_text_data)

        for y in range(height) :
            for x in range(width // 2) :
                if index >= message_length :
                    print('Successfully encoded')
                    break

                blue_pixels = pixels[x,y]
                blue_pixels = (blue_pixels & 0xFE) | (secret_text_data[index])
                pixels[x,y] = blue_pixels
                index += 1

            if index >= message_length :
                break               
            
        merge_image = Image.merge(mode='RGB', bands=(red_channel, green_channel, blue_channel))
        merge_image.save(f"{self.save_result_image_path}/{self.new_file_name}.bmp",'BMP')
                 