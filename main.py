from googletrans import Translator
import json
translator = Translator()

my_file = open(r"C:\Users\vasil\OneDrive\Рабочий стол\Translation.txt", 'w')

languages_dict = {
    'ar': 'arabic',
    'zh-tw': 'chinese (traditional)',
    'tl': 'filipino',
    'fr': 'french',
    'ka': 'georgian',
    'de': 'german',
    'hi': 'hindi',
    'id': 'indonesian',
    'it': 'italian',
    'ja': 'japanese',
    'ko': 'korean',
    'lv': 'latvian',
    'lt': 'lithuanian',
    'no': 'norwegian',
    'fa': 'persian',
    'pl': 'polish',
    'pt': 'portuguese',
    'ru': 'russian',
    'es': 'spanish',
    'sv': 'swedish',
    'th': 'thai',
    'tr': 'turkish',
    'uk': 'ukrainian',
    'vi': 'vietnamese',
    'zu': 'zulu',
}
var_translation = input('What you want to translate? \n')


def translation():

    out = translator.translate(var_translation, dest=dest_)
    #output = [word.encode('utf-8') for word in out.text]
    print(out.text)
    print(out.dest)


for dest_ in languages_dict:
    translation()
    print(dest_)


