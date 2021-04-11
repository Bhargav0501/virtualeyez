import os

os.environ["LRU_CACHE_CAPACITY"] = "1"

BASE_PATH = os.path.dirname(__file__)
MODULE_PATH = os.path.dirname(__file__) + '\\modules'

# detector parameters
DETECTOR_FILENAME = 'craft_mlt_25k.pth'

# recognizer parameters
latin_lang_list = ['en']
devanagari_lang_list = ['hi']
other_lang_list = ['ta', 'te', 'kn']

all_lang_list = latin_lang_list + \
                devanagari_lang_list +  other_lang_list
imgH = 64

number = '0123456789'
symbol = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ '

# All language characters
characters = {
    'all_char': 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' + \
                'ÀÁÂÃÄÅÆÇÈÉÊËÍÎÑÒÓÔÕÖØÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõöøùúûüýþÿąęĮįıŁłŒœŠšųŽž',
    'en_char': 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
    'devanagari_char': '.ँंःअअंअःआइईउऊऋएऐऑओऔकखगघङचछजझञटठडढणतथदधनऩपफबभमयरऱलळवशषसह़ािीुूृॅेैॉोौ्ॐ॒क़ख़ग़ज़ड़ढ़फ़ॠ।०१२३४५६७८९॰',
    'te_char': 'ఁంఃఅఆఇఈఉఊఋఌఎఏఐఒఓఔకఖగఘఙచఛజఝఞటఠడఢణతథదధనపఫబభమయరఱలళవశషసహాిీుూృౄెేైొోౌ్ౠౡౢౣ',
    'kn_char': 'ಂಃಅಆಇಈಉಊಋಎಏಐಒಓಔಕಖಗಘಙಚಛಜಝಞಟಠಡಢಣತಥದಧನಪಫಬಭಮಯರಲಳವಶಷಸಹಾಿೀುೂೃೆೇೈೊೋೌ್೦೧೨೩೪೫೬೭೮೯',
}
