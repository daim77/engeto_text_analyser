# =====  MARTIN DANĚK™  =====
TEXTS = [
    '''
Situated about 10 miles west of Kemmerer, Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, which traverse the valley.
''',

    '''At the base of Fossil Butte are the bright red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, which are about 300 feet thick.
''',

    '''The monument contains 8198 acres and protects a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils represent several varieties of perch, as well as 
other freshwater genera and herring similar to those in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.
'''
    ]
# definitions for variables
autent_dict = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}
my_user_name = ""  # empty username def
my_pass_name = ""  # empty password def
my_text = 0  # default value for text choice
my_text_list = []

# user welcome
print('=' * 60)
print('                TEXT ANALYSER')
print('=' * 60)
print('Welcome: login, choo®se text and view instant results!')
print('=' * 60)

# autentication via input and verification if in database
my_user_name = input('user name: ')
my_pass_name = input('password:  ')
if my_user_name not in autent_dict:
    exit()
if my_user_name in autent_dict:
    if autent_dict[my_user_name] != my_pass_name:
        exit()

# three text choices to be analysed - input int
my_text = int(input('Insert which text you woud like to analyze (from 1 to 3): '))
my_text = my_text - 1

# text separation from TEXTS
my_text_list = TEXTS[my_text].split()

# stats for text
# total amount of words
# .title amount of words
# .uppercase amount of words
# .lowercase amount of words
# amount of numbers

# star chart as stats of amount of lenghts of the words

# sum of all numbers from the text

# FINAL OUTPUT
