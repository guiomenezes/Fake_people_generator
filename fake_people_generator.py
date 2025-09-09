from faker import Faker
from time import sleep

fake = Faker(['en-US'])
print("""\033[1m _____     _          _   _                  ____                _             
|  ___|_ _| | _____  | | | |___  ___ _ __   / ___|_ __ ___  __ _| |_ ___  _ __ 
| |_ / _` | |/ / _ \ | | | / __|/ _ \ '__| | |   | '__/ _ \/ _` | __/ _ \| '__|
|  _| (_| |   <  __/ | |_| \__ \  __/ |    | |___| | |  __/ (_| | || (_) | |   
|_|  \__,_|_|\_\___|  \___/|___/\___|_|     \____|_|  \___|\__,_|\__\___/|_|
\033[0m""")

red = ''

while True:
    perg = str(input('CHOOSE AN OPTION.\n1 - Create fake users.\n2 - Exit.\nOption: '))
    if perg == '1':
        try:
            quant = str(input('Numbers of user to create: '))
            print('Creating users...')
            sleep(3)
            for usuario in range(int(quant)):
                print(30 * '-')
                print(f'NAME: {fake.name()}')
                print(f'ID: {fake.ssn()}')
                print(f'EMAIL: {fake.email()}')
                print(f'ADDRESS: {fake.address()}')
                print(f'CELL: {fake.phone_number()}')
                print(30 * '-')
        except ValueError:
            print('Invalid option! Try again.')
            
    elif perg == '2':
        break
    elif perg != '1' or perg != '2':
        print('Invalid option! Type 1 or 2.')

    