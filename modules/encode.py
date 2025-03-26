# Convert Text into Binaries and embed it into given image

class convertText :

    def __init__(self) :
        self.user_secret_text = input('Input your text : ')

        self.convert_to_binary(user_secret_text=self.user_secret_text)

    def convert_to_binary(self, user_secret_text : str) -> bin:
        character_bin = []
        
        for i in user_secret_text :
            char_unicode = ord(i)
            character_bin.append(bin(char_unicode)[2:])
        
        print(character_bin)
        return character_bin

    def embed_text(self, image_path) :
        image = Img.open(image_path)

        if image.mode != 'RGB' :
            image = image.convert('RGB')

        return image_path