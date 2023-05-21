import random
import webbrowser

def generate_random_word(length):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    return ''.join(random.choice(letters) for i in range(length))

def search_random_word():
    random_word = generate_random_word(random.randint(5, 10))
    query = f"https://www.bing.com/search?q={random_word}"
    webbrowser.open(query)

# Prompt for the number of searches
num_searches = int(input("Enter the number of random searches: "))

# Perform random searches
for i in range(num_searches):
    search_random_word()