from googletrans import Translator
import json
translator = Translator()

my_file = open(r"C:\Users\vasil\OneDrive\Рабочий стол\Translation.txt", 'w')

languages_dict = {
    'ar',
    'zh-tw',
    'tl',
    'fr',
    'ka',
    'de',
    'hi',
    'id',
    'it',
    'ja',
    'ko',
    'lv',
    'lt',
    'no',
    'fa',
    'pl',
    'pt',
    'ru',
    'es',
    'sv',
    'th',
    'tr',
    'uk',
    'vi',
    'zu'
}
var_translation = input('What you want to translate? \n')


def translation():

    out = translator.translate(var_translation, dest=dest_)
    #output = [word.encode('utf-8') for word in out.text]
    print(out.text)


for dest_ in languages_dict:
    translation()
    print(dest_)

my_file.close()

