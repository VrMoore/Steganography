#  Import libraries
from PIL import Image
import os

class deconvertText() :

    def __init__(self, image_file_name : str, cache_path : str) -> None :
        self.image_file_name = image_file_name
        self.cache_path = cache_path

        self.text_salt = self.get_text(cache_path=self.cache_path)
        self.text_decryption(cache_path=self.cache_path, salt=self.text_salt)

    def get_text(self, cache_path : str) -> list[int] :
        md_file = 'dump.md'
        md_file_path = f'{cache_path}/{md_file}'

        with open(file=md_file_path, mode='r') as file :
            content = file.readlines()

        image_salt : list = content[2]
        image_salt_data : list = image_salt.rsplit('=', 1)[1]

        return image_salt_data 

    def text_decryption(self, cache_path : str, salt : str) :
        pass

    def print_text(self) :
        pass