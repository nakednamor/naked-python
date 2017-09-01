import string
import random

print("Enter some text --> but only characters a-z (lower-case)")
# todo validate if text is empty or contains invalid characters
text = input("Your text:")
text_length = len(text)

hits = ['n' for i in range(0, text_length)]

for counter in range(1, 1000):
    evolved_text = ''

    for i in range(0, text_length):
        letter_to_add = ''
        if hits[i] == 'n':
            random_letter = random.choice(string.ascii_lowercase)
            letter_to_add = random_letter

            if random_letter == text[i]:
                hits[i] = 'y'
        else:
            letter_to_add = text[i]

        evolved_text = evolved_text + letter_to_add

    print(evolved_text)

    if evolved_text == text:
        print("Yeah! I've found your text")
        print("It took me " + str(counter) + " trials")
        break
