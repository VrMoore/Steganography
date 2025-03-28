# Import package and modules
import os
from modules import encode

# Global variable
MY_PATH = os.getcwd().replace(os.sep, '/')

class colors() : 
    # Give text styling in terminal

    WARNING = '\033[93m'
    ENDC = '\033[0m'
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    LIGHT_GRAY = "\033[0;37m"
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    LIGHT_WHITE = "\033[1;37m"
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"

class doEncode() :

    def __init__(self) :
        self.encode = encode.convertText()
        self.image_file_name = input('Image file name : ')
        self.user_secret_text = input('Input your text : ')  
        self.IMG_PATH = f"{MY_PATH}/Images/{self.image_file_name}"
        self.encode.embed_text(image_path=self.IMG_PATH, secret_text=self.user_secret_text)
        self.check_file_extension(file_name=self.image_file_name)

    def check_file_extension(self, file_name : str) :
        if self.image_file_name.endswith(('.jpg','.jpeg','.webp','.png','.gif','.tif','.tiff','.ico','.bmp')) :
            self.image_converter(file_name=file_name)
        else :
            print(f"{colors.RED}UNSUPPORTED FILE TYPE{colors.ENDC}\n{colors.YELLOW}Only support : .jpg, .jpeg, .png, .webp, .gif, .tif, .tiff, .ico{colors.ENDC}")

    def image_converter(self, file_name : str) :

        if os.path.exists(self.IMG_PATH) :
            self.encode.convert_image(image_path=self.IMG_PATH, file_name=self.image_file_name)
        else :
            return print(f"{colors.WARNING}The image does not exist in this path{colors.ENDC}")



class userInterfaces :

    def __init__(self) :
        print(f"""\n
            {'='*20}
            Welcome to StegAgent :)

            I will be your agent to slip a text between image binaries.
            {'='*20}\n
        """)
        
        self.ask_user()

    def ask_user(self) :
        
        users_ans = input('Do you want to continue? (y/n) : ')
        users_ans = users_ans.lower()

        if users_ans == 'y' :
            doEncode()
        elif users_ans == 'n':
            print('Good Bye :)')
        else :
            print(f'{colors.WARNING}Invalid input.{colors.ENDC}')

if __name__ == '__main__' :
    run = userInterfaces()
