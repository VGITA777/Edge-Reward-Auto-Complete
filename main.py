import random
import webbrowser

def generate_random_word(length):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    return ''.join(random.choice(letters) for i in range(length))

def search_random_word():
    random_word = generate_random_word(random.randint(5, 10))
    query = f"https://www.bing.com/search?q={random_word}"
    webbrowser.open(query)

# Perform random searches
while True:
    try:
        num_searches = int(input("Enter the number of random searches: "))
        for i in range(num_searches):
            search_random_word()
    except ValueError:
        print('Put valid input!')
        continue
    while True:
        loop = input('Again (Y/N?): ')
        if loop.upper() == 'Y' or loop.upper() == 'N':
            break
        else:
            print('Put a valid input!')
    if loop.upper() == 'N':
        print('Good bye :)')
        break