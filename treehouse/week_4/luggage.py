# I'm just playing around with packing and unpacking dictionaries


def packer(name=None, **kwargs):
    print(kwargs)


def unpacker(first_name=None, last_name=None):
    if first_name and last_name:
        print("Hi {} {}!".format(first_name, last_name))
    else:
        print("Hi no name!")


packer(name="kenneth", num=42, spanish_inquisition=None)
unpacker(**{"last_name": "Love", "first_name": "Kenneth"})


def word_count(string):
    word_list = string.lower().split()
    word_dict = {}
    for word in word_list:
        count = 0
        for match_word in word_list:
            if word == match_word:
                count += 1
        word_dict[word] = count
    return word_dict
