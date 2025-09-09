def repeat_vowels(s):
    temp = []
    vowels = ['a','e','i','o','u']
    vowel_cnt = 0
    for key in s:
        v = key.lower()
        if v in vowels:
            vowel_cnt += 1
            if vowel_cnt == 1:
                temp.append(key)
            else:
                temp.append(key)
                temp.append(v * (vowel_cnt - 1))
        else:
            temp.append(key)
    return ''.join(temp)

res = repeat_vowels("AEIOU")
print(res)