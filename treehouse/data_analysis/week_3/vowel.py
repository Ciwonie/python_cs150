def disemvowel(word):
    index = 0
    vowel_list = []
    vowel_list.extend(word)
    print(vowel_list)

    while index <= len(word):
        for i in vowel_list:
            if i == 'A' or i == 'E' or i == "I" or i == "O" or i == "U":
                vowel_list.remove(i)
            elif i == 'a' or i == 'e' or i == "i" or i == "o" or i == "u":
                vowel_list.remove(i)
        index += 1

    word = "".join(vowel_list)
    return word
