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
autent_dict = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}  # authencitation database
my_user_name = ""  # empty username var
my_pass_word = ""  # empty password var
count = 0  # universal counting variable
my_text = 0  # default value for text choice
my_text_list = list()  # here is saved separated text from original TEXTS
spec_stat = {
    'length': 0,
    'title': 0,
    'upper': 0,
    'lower': 0,
    'digit': 0,
    'sum': 0,
}  # cleaning counter for spec stat

length_stat = []  # index 1 == 1 letter words, index 2 == 2 letters words etc | 45 indexes = the longiest english word

# user welcome
print('=' * 60)
print('                TEXT ANALYSER')
print('=' * 60)
print('Welcome: login, choo®se text and view instant results!')
print('=' * 60)

# authentication and login
my_user_name = input('user name: ')
my_pass_word = input('password:  ')
if my_user_name not in autent_dict:
    print('wrong user name!!!')
    exit()
if my_user_name in autent_dict:
    if autent_dict[my_user_name] != my_pass_word:
        print('wrong password!!!')
        exit()

# three text choices to be analysed - input int
my_text = int(input('Insert which text you would like to analyze (from 1 to 3): '))
my_text = my_text - 1
print('=' * 60)

# text separation from TEXTS
count = 0
my_text_list = TEXTS[my_text].split()
while count < len(my_text_list):
    my_text_list[count] = my_text_list[count].strip(",.")  # cleaning from unwanted characters
    count += 1

# fullfilment length_stat LIST for counting letters in particular words, last index = the longiest word + 1
count = -1
while count < len(max(my_text_list, key=len)):
    length_stat.append(0)
    count += 1

# stats for text
count = 0
spec_stat['length'] = len(my_text_list)  # total amount of words
while count < len(my_text_list):
    if my_text_list[count].istitle():  # counting titlecase
        spec_stat['title'] += 1
    if my_text_list[count].isupper():  # counting uppercase
        spec_stat['upper'] += 1
    if my_text_list[count].islower():  # counting lowercase
        spec_stat['lower'] += 1
    if my_text_list[count].isdigit():  # counting numeric and summary
        spec_stat['digit'] += 1
        spec_stat['sum'] += int(my_text_list[count])
    length_stat[len(my_text_list[count])] += 1  # stats of amount of lenghts of the words
    count += 1


# FINAL OUTPUT
print('=' * 60)
print('Total words amount:              ', spec_stat['length'])
print('Total titlecase words amount:    ', spec_stat['title'])
print('Total uppercase words amount:    ', spec_stat['upper'])
print('Total lowercase words amount:    ', spec_stat['lower'])
print('Total numeric strings amount:    ', spec_stat['digit'])
print('=' * 60)

# star chart visualisation
count = 1
while count < (len(length_stat) - 1):
    if length_stat[count] != 0:
        print(count, '*' * length_stat[count], ' ', length_stat[count])
    count += 1

# sum up output
print('=' * 60)
print('Total sum of numeric strings: ', spec_stat['sum'])
print('=' * 60)
