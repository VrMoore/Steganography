"""
    Take secret text and image (within Images folder) from the user to perform steganography.
    To ensure security, convertText also make salt using os.urandom from the length of secret text.
    Iterate only in the blue channel of the left part of the image (height , width // 2).

    Save image with .bmp extension
"""

# Import Libraries
from PIL import Image
import os

class convertText :
    """"
        convertText is an object where it take desired image and text given by user where later be processed in convertText method.
    """

    def __init__(self, file_name : str, secret_text : str) -> None:
        """
            Initializes of convertText object.

            Parameters :
            ------------
                file_name : str
                    Process file_name where it will be later used in Image.save path.

                secret_text : str
                    Process secret text in convert_to_ascii & text_encryption. Contain user text that will be embedded into the image.

            
            ```
                Return : None
            ```
        """
        self.file_name : str = file_name
        self.secret_text : str = secret_text
        self.new_file_name : str = os.path.splitext(file_name)[0]

        self.current_path : str = os.getcwd().replace(os.sep, '/')
        self.save_result_image_path : str = f"{self.current_path}/IMG RES"
        self.save_result(image_path=self.save_result_image_path)

    def save_result(self, image_path) -> None:
        """
            Automatically create folder to save result of given image. Create folder IMG_RES in current working directory.
        
            Parameters :
            ------------
                image_path : str
                    Take image path from IMG RES folder

            ```
                Return : None
            ```
        """

        os.makedirs(name=image_path, exist_ok=True)

    def convert_to_ascii(self, user_secret_text : str) -> str:
        """
            Convert given secret text into ASCII number.

            user_secret_text contain text given by user where it will be concealed in the image. 
            After convert each character and append to the list, it will call text_encryption to pass the list.

            Parameters :
            ------------
                user_secret_text : str
                    Process given text by user into ASCII numbers.


            ```
                Return : list[int]
                    Return list of integer contain each character in given text into ASCII number.
            ```

        """
        character_bin : list = []
        
        # Iterate each character and convert into ASCII
        for i in user_secret_text :
            char_unicode = ord(i)
            char_bin = f"{char_unicode:08b}"
            print(char_bin,'char_bin')
            character_bin.append(char_bin)
        
        print(character_bin)

        data_bin_len = len(character_bin)
        self.file_write(text_len=data_bin_len)

        character_bin = ''.join(x for x in character_bin)

        return character_bin

    def file_write(self, text_len : int) :
        
        file_name = 'dump.md'

        # save to the IMG RES folder
        file_name_path = f"{self.save_result_image_path}/dump.md"

        with open(file=file_name_path, mode='w') as file : 
            file.write(f"FILE_NAME ={self.new_file_name}.bmp")
            file.write('\n')
            file.write(f"TEXT LENGTH ={text_len}")
            file.write('\n')

    def convert_image(self, image_path : str) -> None :
        """
            Convert Image into RGB mode.

            Take an image, check the mode of the image. If it's RGBA then convert it to the RGB with background value of white, removing transparent background.
            Save image to the IMG RES folders.

            Parameters :
            ------------
                image_path : str 
                    Take and image path which is Images folder.
                
            
            ```
                Return : None
            ```
        """
        image = Image.open(image_path)

        if image.mode != 'RGB' :
            
            # make new background
            bg_image = Image.new('RGBA',size=image.size,color=(255,255,255,0))

            # paste the image into new bacground
            bg_image.paste(image, (0,0), image)

            # convert to the RGB
            bg_image = bg_image.convert('RGB')

            # Assign of the new image with removed background to image variable
            image = bg_image

        else :
            image = image.convert('RGB')

        # Save with .bmp extension, lossless type.
        image.save(f"{self.save_result_image_path}/{self.new_file_name}.bmp",'BMP')

    def embed_text(self, image_path : str,secret_text : str) -> None:
        """
            Embed of given text into the image.

            Take only blue channel blue image to conceal the given text. Iterate blue channel only left part of the image (high , width // 2).
            After embedding, the blue channel will merge with other channel to make full image.

            Parameters :
            ------------
                image_path : str
                    Get image path which is IMG RES folder, take converted image.
                
                secret_text : str
                    Pass secret text into convert_to_ascii method which later will be embedded into the image.

            
            ```
                Return : None
            ```
        """
        image = Image.open(image_path)

        # Split all the channels
        red_channel, green_channel, blue_channel = image.split()

        # Copy the blue channel
        blue_image = blue_channel.copy()

        pixels = blue_image.load()
        width, height  = blue_channel.size

        secret_text_data = self.convert_to_ascii(user_secret_text=secret_text)
        print(secret_text_data, 'salted') 
        index = 0
        message_length = len(secret_text_data)

        # Iterate only left part of the image, so it can run faster
        for y in range(height) :
            for x in range(width) :
                if index >= message_length :
                    print('Successfully encoded')
                    break

                blue_pixels = pixels[x,y]
                print(blue_pixels, 'original')

                # Do LSB using 0xFE which make 7 bit untouched with the LSB (Least Significant Bit) left.
                blue_pixels = (blue_pixels & 0xFE) ^ (int(secret_text_data[index]))
                pixels[x,y] = blue_pixels
                index += 1

            if index >= message_length :
                break               
            
        # Merge the image and save to the IMG RES folder
        merge_image = Image.merge(mode='RGB', bands=(red_channel, green_channel, blue_channel))
        merge_image.save(f"{self.save_result_image_path}/{self.new_file_name}.bmp",'BMP')
                 