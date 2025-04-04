# Import package and modules
import os
from modules import encode
from modules import decode

# Global variable
MY_PATH = os.getcwd().replace(os.sep, '/')

class colors() : 
    """
        Give tyle style to terminal when print out.
    """

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
    """
        Handle encode.py interaction

        Check file extension of the given image before processing the data.
    """

    def __init__(self) -> None :
        """
            Initialize doEncode object

            Parameters : None

            ```
                Return : None
            ```
        """
        self.image_file_name = input('| Image file name : ')
        self.user_secret_text = input('| Input your text : ')  
        
        self.encode = encode.convertText(file_name=self.image_file_name, secret_text=self.user_secret_text)
        self.IMG_PATH = f"{MY_PATH}/Images/{self.image_file_name}"
        self.check_file_extension(file_name=self.image_file_name)

    def check_file_extension(self, file_name : str) -> None :
        """
            Check file extension given by user image file.

            Check file extension if it's supported by the apps. Pass file name to image_converter method which later to be converted by encode.py
            Image converter only support :  \r.jpg, .jpeg, .webp, .png, .gif, .tif, .tiff, .ico, .bmp 

            Parameters : 
            ------------
                file_name : str
                    Accept file name which will be checked the file extension and pass it to the image_converter method


            ```
                Return : None
            ```
        """

        # check file extensions
        if self.image_file_name.endswith(('.jpg','.jpeg','.webp','.png','.gif','.tif','.tiff','.ico','.bmp')) :
            self.encode.convert_image(image_path=self.IMG_PATH)
            self.image_converter(file_name=file_name)
        else :
            print(f"{colors.RED}UNSUPPORTED FILE TYPE{colors.ENDC}\n{colors.YELLOW}Only support : .jpg, .jpeg, .png, .webp, .gif, .tif, .tiff, .ico{colors.ENDC}")

    def image_converter(self, file_name : str) -> None :
        """
            Handle image conversion and cache path to save image result.

            Split file name to only get the name of the file without the extensions and make cache path to save the result.
        
            Parameters :
            ------------
                file_name : str
                    Get full file name and process it

            
            ```
                Return : None
            ```
        """

        # Get only the name of the file
        cache_image_file = os.path.splitext(file_name)[0]

        cache_path = f"{MY_PATH}/IMG RES/{cache_image_file}.bmp"

        if os.path.exists(self.IMG_PATH) :
            self.encode.embed_text(image_path=cache_path, secret_text=self.user_secret_text)
        else :
            print(f"{colors.WARNING}The image does not exist in this path{colors.ENDC}")

class doDecode() :

    def __init__(self) :
        pass

class userInterfaces :
    """
        Handles user interfaces
    """

    def __init__(self) :
        """
            Show welcome to the user
        """
        print(f"""\n
            {'='*20}
            Welcome to StegAgent :)

            I will be your agent to conceal a secret text between image binaries.

            1. Encode
            2. Decode
            
            Enter anything to EXIT
            {'='*20}\n
        """)
        
        self.ask_user()

    def ask_user(self) :
        """
            Ask user to continue or exit the app.
        """
        
        users_ans = input('Do you want to continue? (y/n) : ')
        users_ans = users_ans.lower()

        if users_ans == 'y' :
            self.user_choice()
        elif users_ans == 'n':
            print('Good Bye :)')
        else :
            print(f'{colors.WARNING}Invalid input.{colors.ENDC}')

    def user_choice(self) :
        """
            Ask user to choose between Encode, Decode or Exit.
        """

        while True :
            user_choice = input('\nI want to : ')
            user_choice.lower()

            if user_choice == '1' :
                doEncode()
            elif user_choice == '2' :
                doDecode()
            else :
                print('GoodBye :)')
                break

if __name__ == '__main__' :
    run = userInterfaces()
