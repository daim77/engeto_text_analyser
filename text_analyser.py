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
AUTENT_DICT = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}
count = 0
my_text = 0
sixty = '=' * 60
my_text_list = list()
spec_stat = {
    'length': 0,
    'title': 0,
    'upper': 0,
    'lower': 0,
    'digit': 0,
    'sum': 0,
}

length_stat = []    # index 1 == 1 letter words, index 2 == 2 letters words etc

# user welcome
print(
    sixty, '\n',
    'TEXT ANALYSER'.rjust(33), '\n',
    sixty, '\n',
    'Welcome: login, choose text and view instant results!'.rjust(56), '\n',
    sixty
)

# authentication and login
my_user_name = input('user name: ')
my_pass_word = input('password:  ')
if my_user_name not in AUTENT_DICT or my_pass_word != AUTENT_DICT[my_user_name]:
    print("Wrong credentials!")
    exit()

# text choices to be analysed - input int
while count == 0:
    my_text = input(f'Insert which text you would like to analyze (from 1 to {len(TEXTS)}): ')
    if not my_text.isdigit():
        print('Entry must be NUMBER within required interval!...')
        continue
    elif int(my_text) in range(1, (len(TEXTS) + 1)):
        my_text = int(my_text) - 1
        break
    else:
        print('Entry must be number within REQUIRED INTERVAL!...')
print('=' * 60)

# text separation from TEXTS
my_text_list = TEXTS[my_text].split()
for count, char in enumerate(my_text_list):
    my_text_list[count] = char.strip(",.")

# fullfilment length_stat LIST for counting letters in particular words,
# last index = the longiest word + 1
count = -1
while count < len(max(my_text_list, key=len)):
    length_stat.append(0)
    count += 1

# stats for text
spec_stat['length'] = len(my_text_list)
for count, char in enumerate(my_text_list):
    if my_text_list[count].istitle():
        spec_stat['title'] += 1
    elif my_text_list[count].isupper():
        spec_stat['upper'] += 1
    elif my_text_list[count].islower():
        spec_stat['lower'] += 1
    elif my_text_list[count].isdigit():
        spec_stat['digit'] += 1
        spec_stat['sum'] += int(my_text_list[count])
    length_stat[len(my_text_list[count])] += 1

# FINAL OUTPUT
print(
    sixty, '\n',
    'Total words amount:              ', spec_stat['length'], '\n',
    'Total titlecase words amount:    ', spec_stat['title'], '\n',
    'Total uppercase words amount:    ', spec_stat['upper'], '\n',
    'Total lowercase words amount:    ', spec_stat['lower'], '\n',
    'Total numeric strings amount:    ', spec_stat['digit'], '\n',
    sixty
)

# star chart visualisation
count = 0
for char in length_stat:
    if length_stat[count] != 0:
        print(count, '*' * length_stat[count], ' ', length_stat[count])
    count += 1

# sum up output
print(sixty)
print('Total sum of all numeric strings: ', spec_stat['sum'])
print(sixty)
