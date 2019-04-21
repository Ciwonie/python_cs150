shopping_list = []


def show_help():
    print("What should we pick up at the store?")
    print("""
    Enter 'DONE' to stop adding items.
    Enter 'HELP for this help.
    ENTER 'SHOW" for the list.
    """)


def add_to_list(item):
    shopping_list.append(item)
    print('* ', item, 'added. Total #: ', len(shopping_list))

# Define a function named show_list that prints all the items in the list


def show_list():
    for item in shopping_list:
        print('* ', item)


show_help()
while True:
    new_item = input("> ")

    if new_item == 'DONE':
        break
    elif new_item == 'HELP':
        show_help()
        continue
    elif new_item == 'SHOW':
        show_list()
        continue

    add_to_list(new_item)
