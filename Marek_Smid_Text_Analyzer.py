# Data -------------------------------------------------------------------------
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

         '''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

         '''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''

# Overeni hesla -------------------------------------------------
hesla = {
    'uzivatel1': 'heslo',
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'
}

# Zeptej se na uzivatelske jmeno a heslo
username = input('Username: ')
password = input('Password: ')

# Podminkovy vyraz
if hesla.get(username) == password:
    print(f"Welcome to the app, {username}")

else:
    print('Wrong name or password')
    exit

text_choice = int(input("Choose the text to be analysed (1 - Text 1, 2 - Text 2, 3 - Text 3): "))
text_choice = text_choice - 1

if text_choice == 0 or text_choice == 1 or text_choice == 2:
    pass
else:
    print("invalid choice")
    exit()
    
selected_text = TEXTS[text_choice]
word_count = len(selected_text.split())

selected_text_list = [slovo.strip(",.()") for slovo in selected_text.split()]
#selected_text_list = selected_text.split()

list_capital_start=[]
for word in selected_text_list:
    if word[0].isupper():
        list_capital_start.append(word)

capital_start_count = len(list_capital_start)

list_capital_all=[]
for word in selected_text_list:
    if word.isupper():
        list_capital_all.append(word)

capital_all_count = len(list_capital_all)

list_lowercase_all=[]
for word in selected_text_list:
    if word.islower():
        list_lowercase_all.append(word)

lowercase_all_count = len(list_lowercase_all)

count_numbers = 0
for i in selected_text_list:
      if i.isnumeric():
        count_numbers+=1
        
numbers_list = [] 
for i in selected_text_list:
      if i.isnumeric():
        numbers_list.append(i)
        
#number_list_int = list(map(int, numbers_list))
number_sum = sum(list(map(int, numbers_list)))


lengths = [len(word) for word in selected_text_list]
max_length = max(lengths)
tallies = [0 for x in range(max_length+1)]

for length in lengths:
   tallies[length] += 1
   
tallies.pop(0)


import numpy as np   
    
def unique(lengths):
    x = np.array(lengths)
    print(np.unique(x))
    
freq_keys = np.unique(lengths)


frequencies = dict(zip(freq_keys, tallies))

print(f"There are {word_count} in the selected text.")

print(f"There are {capital_start_count} titlecase words.")

print(f"There are {capital_all_count} uppercase words.")

print(f"There are {lowercase_all_count} lowercase words.")

print(f"There are {count_numbers} numeric strings.")

print(f"The sum of all the numbers is {number_sum}")

print("LEN|","OCCURANCE|","NR.")
for key, value in frequencies.items() :
    print (key,"*"*key ,value)
    
