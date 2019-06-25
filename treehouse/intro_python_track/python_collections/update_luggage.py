# packing and unpacking dictionaries

teachers = {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
            'Kenneth Love': ['Python Basics', 'Python Collections', 'AWS', 'Advanced Java']}


def packer(name=None, **kwargs):
    print(kwargs)


def unpacker(first_name=None, last_name=None):
    if first_name and last_name:
        print("Hi {} {}!".format(first_name, last_name))
    else:
        print("Hi no name!")


packer(name="kenneth", num=42, spanish_inquisition=None)
unpacker(**{"last_name": "Love", "first_name": "Kenneth"})

course_minutes = {"Python Basics": 232, "Django Basics": 237,
                  "Flask Basics": 189, "Java Basics": 133}

for course, minutes in course_minutes.items():
    print("{} is {} minutes long".format(course, minutes))


# def word_count(string):
#     word_list = string.lower().split()
#     word_dict = {}
#     for word in word_list:
#         count = 0
#         for match_word in word_list:
#             if word == match_word:
#                 count += 1
#         word_dict[word] = count
#     return word_dict


# def most_courses(dict):
#     most_class = ""     # holds the name of teach with most class
#     max_count = 0       # max counter for classes
#     for teacher in dict:
#         if len(dict[teacher]) > max_count:
#             max_count = len(dict[teacher])
#             most_class = teacher
#     return most_class


# def stats(dict):
#     all_courses = []
#     for teachers in dict:
#         all_courses.append([teachers, len(dict[teachers])])
#     return all_courses
