# Pangram
sentence = input("Give the word or sentence to check if it is a pangram: ")
letters = input("Give the letters to check if the given word is a pangram: ")
def is_pangram(sentence, letters):
    set_lst = set(filter(str.isalpha, sentence.lower()))
    set_letters = set(letters)
    for i in set_letters:
        if i not in set_lst:
            return False
    return True

res = is_pangram(sentence, letters)
print("Is Panagram ?", res )