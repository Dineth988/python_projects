

word = (input("Give the word: ")).lower()

it_word = iter(word)

def vowel_to_g():
    translation = ""

    for char in it_word:
        if char in "aeiou" :
            translation = translation + "g"
        else:
            translation = translation + char
    return translation

print(vowel_to_g())



