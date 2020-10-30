import random
import string
import json
from PIL import Image
from claptcha import Claptcha


def randomString():
    rndLetters = (random.choice(string.ascii_uppercase) for _ in range(6))
    return "".join(rndLetters)

def generateCaptcha():
    # Initialize Claptcha object with random text, FreeMono as font, of size
    # 100x30px, using bicubic resampling filter and adding a bit of white noise
    c = Claptcha(randomString, "Abel/Abel-Regular.ttf",
                resample=Image.BICUBIC, noise=0.3)

    text, _ = c.write('pythonFiles/captcha1.png')
    # c.size = (150, 90)
    # c.margin = (25, 25)
    # print(text)  # 'PZTBXB', string printed into captcha1.png

    # text, _ = c.write('pythonFiles/captcha2.png')
    # print(text)  # 'NEDKEM', string printed into captcha2.png

    # Change images' size to 150x90 and estimated margin to 25x25
    

    # text, _ = c.write('pythonFiles/captcha3.png')
    # print(text)  # 'XCQYVS', captcha3.png has different dimentions than
    # captcha1.png and captcha2.png
    return json.dumps({'secret':text})
if __name__ == '__main__':
    generateCaptcha = generateCaptcha()
    print(generateCaptcha)
