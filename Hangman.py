import random


def mask_word(word):
    display_answer = ['_' for _ in word]
    return display_answer


def find_all_indexes(word, letter):
    return [i for i, ch in enumerate(word) if ch == letter]


def check_element(symbol):
    if symbol in current_word:
        print('Yeah!')
        indexes = find_all_indexes(current_word, symbol)
        if len(indexes) > 0:
            indexes = list(indexes)
            for number in indexes:
                display_mask_word[number] = symbol
        else:
            ind = current_word.index(symbol)
            display_mask_word[ind] = symbol
    else:
        print('Not this!')

# TODO: перевести слова на английский
words_list = [
    'яблоко', 'кот', 'дом', 'солнце', 'река', 'лес', 'машина', 'книга',
    'звезда', 'собака', 'цветок', 'дождь', 'ветер', 'гора'
]
attempts = 7
current_word = random.choice(words_list)
display_mask_word = mask_word(current_word)
while attempts != 0:
    print(' '.join(display_mask_word))
    element = input('Enter the letter: ')
    check_element(element)
    if '_' not in display_mask_word:
        print('You WIN!')
        break
    attempts -= 1
    print(f'{attempts} Attempts remaining')
print('Game over')
