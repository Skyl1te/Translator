# import libraries
from translate import Translator
from colorama import Fore, init
init()

# list of bad words (you can add words)
badWords = ['bitch', 'shit', 'пидр', 'сука', 'блять', 'блядь', 'пздабол', 'ебать', 'долбоеб', 'долбоёб']

# color's variables
quastionColor = Fore.MAGENTA
userColor = Fore.LIGHTMAGENTA_EX

# loop cycle
while True:
    # parameters variables
    fromLang = input(f'{quastionColor}Enter the language from which you want to translate: {userColor}')
    toLang = input(f'{quastionColor}Enter the language into which you want to translate: {userColor}')
    text = input(f'{quastionColor}Enter the text which you want to translate: {userColor}')

    # make user's text lowercase
    text.lower()
    # check user's text on bad words
    for word in badWords:
        word.lower()
        if word in text:
            print(Fore.RED + f'Pls, don\'t use this word: {word}')
            while word in text:
                text = input(
                    f'{quastionColor}Enter the text which you want to translate: {userColor}')

    # make user's languages lowercase
    fromLang.lower()
    toLang.lower()
    # analyze user's languages which he entered
    try:
        # choose user's languages which he entered
        translator = Translator(from_lang=fromLang, to_lang=toLang)
    except:
        # if error - miss
        pass
    
    # translate text
    translation = translator.translate(text)

    # display result
    print(Fore.GREEN + translation)
    print(Fore.YELLOW + '-' * 50)