from googletrans import Translator
#https://py-googletrans.readthedocs.io/en/latest/ documentation
import keyboard

translator = Translator()

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

var_translation1 = input('Title in ENGLISH: \n')
var_translation3 = input('Hashtag in ENGLISH: \n')
var_translation2 = input('Description in ENGLISH: \n')


#keyboard.read_key()

def translation():

    if dest_ == 'ar':
        print('Arabic')
    elif dest_ == 'zh-tw':
        print('Chinese (traditional)')
    elif dest_ == 'tl':
        print('Filipino')
    elif dest_ == 'ka':
        print('Georgian')
    elif dest_ == 'de':
        print('German')
    elif dest_ == 'hi':
        print('Hindi')
    elif dest_ == 'id':
        print('Indonesian')
    elif dest_ == 'it':
        print('Italian')
    elif dest_ == 'ja':
        print('Japanese')
    elif dest_ == 'ko':
        print('Korean')
    elif dest_ == 'lv':
        print('Latvian')
    elif dest_ == 'lt':
        print('Lithuanian')
    elif dest_ == 'no':
        print('Norwegian')
    elif dest_ == 'fa':
        print('Persian')
    elif dest_ == 'pl':
        print('Polish')
    elif dest_ == 'pt':
        print('Portuguese')
    elif dest_ == 'ru':
        print('Russian')
    elif dest_ == 'es':
        print('Spanish')
    elif dest_ == 'sv':
        print('Swedish')
    elif dest_ == 'th':
        print('Thai')
    elif dest_ == 'tr':
        print('Turkish')
    elif dest_ == 'uk':
        print('Ukrainian')
    elif dest_ == 'vi':
        print('Vietnamese')
    elif dest_ == 'zu':
        print('Zulu')
    elif dest_ == 'fr':
        print('French')

    out1 = translator.translate(var_translation1, dest=dest_)
    out3 = translator.translate(var_translation3, dest=dest_)
    out2 = translator.translate(var_translation2, dest=dest_)

    print(out1.text + '\n' + out3.text + '\n' + '\n' + out2.text)


for dest_ in languages_dict:
    translation()
    print('\n')


