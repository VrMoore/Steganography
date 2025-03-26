# Import package and modules
from PIL import Image
import os
from modules import encode

# Global variable
MY_PATH = os.getcwd().replace(os.sep, '/')

class doEncode() :

    def __init__(self) :
        self.image_file_name = input('Image file name : ')

    def image_path(self) :
        IMG_PATH = f"{MY_PATH}/Images/{self.image_file_name}"
        embed_text_into_img = encode.convertText()
        embed_text_into_img.embed_text(image_path=IMG_PATH)


class userInterfaces :

    def __init__(self) :
        print(f"""\n
            {'='*20}
            Welcome to StegAgent :)

            I will be your agent to slip a text between image binaries.
            {'='*20}\n
        """)


    def ask_user(self) :
        users_ans = input('Do you want to continue? (y/n) : ')
        users_ans = users_ans.lower()

        while users_ans in ('y','n') :
            if users_ans == 'y' :
                do_convert = doEncode()
                break
            else :
                print('Stop.')
                break
        else :
            print('Invalid input.')

if __name__ == '__main__' :
    run = userInterfaces()
    run.ask_user()
