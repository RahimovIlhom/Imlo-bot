from uzwords import words
from difflib import get_close_matches

def checkWord(word, words=words):
    if word[0] == ' ' or word[-1] == ' ':
        word = word.replace(' ', '')
    word.lower()
    matches = set(get_close_matches(word, words))
    avairable = False
    if word in matches:
        avairable = True
        matches = word
    elif 'ҳ' in word:
        word = word.replace('ҳ', 'х')
        matches.update(get_close_matches(word, words))
    elif 'х' in word:
        word = word.replace('х', 'ҳ')
        matches.update(get_close_matches(word, words))

    return {'avairable':avairable, 'matches':matches}

if __name__ == '__main__':
    print(checkWord(' покиза '))
    print(checkWord('ҳусан'))