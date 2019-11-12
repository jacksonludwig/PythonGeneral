import datetime
import os

MAX_CHAR_PER_LINE = 13

author = input("Enter author name: ")


def create_journal():
    name = input("Please name your journal: ")
    current_dir = os.getcwd()
    new_journal_path_with_name = current_dir + "/" + name

    try:
        os.mkdir(new_journal_path_with_name)
    except OSError:
        print("Directory for journal \"" + name + "\" could not be created.")
    else:
        print("Directory for journal \"" + name + "\" was created successfully.")


def view_journal():
    os.chdir(os.getcwd())
    journal_list = os.listdir()

    print("Journals currently created: " + str(len(journal_list)))
    for item in journal_list:
        print(item)

    name_for_selection = input("Enter the name of the journal you would like to open: ")
    current_dir = os.getcwd()
    updated_path = current_dir + "/" + name_for_selection
    os.chdir(updated_path)

    entry_list = os.listdir()
    print("Existing journal entries: " + str(len(entry_list)))
    for item in entry_list:
        print(item)


def enter_entry_content():
    info = input("Please write your journal entry below:\n")
    return info


def write_to_file(entry, content):
    char_count = 0
    word_start_index = 0
    for i in range(0, len(content) - 1):
        if content[i] == " ":
            entry.write(content[word_start_index:i])
            char_count += 1
            word_start_index = i
        if char_count == MAX_CHAR_PER_LINE:
            char_count = 0
            entry.write("\n")

    entry.close()


def enter_entry_supplemental_with_title(title):
    content = enter_entry_content()
    file = title.replace(" ", "") + ".txt"
    entry = open(file, "a")
    entry.write(author + "\n")
    entry.write(title + "\n")
    entry.write(str(datetime.datetime.now()) + "\n")

    write_to_file(entry, content)


def add_page():
    title = input("Enter a name for the new journal entry:\n")
    enter_entry_supplemental_with_title(title)


def remove_page():
    title = input("Enter the title of the entry you want to delete:\n")
    file = title.replace(" ", "")
    os.remove(file)


def use_journal():
    print("Journal Controls: ")
    print("1: Make a new journal")
    print("2: Open an existing journal")
    print("3: Create a new entry in an existing journal")
    print("4: Add on to an existing entry")
    print("5: Remove an existing entry")

    while True:
        menu_choice = input("Type your choice here: ")
        print("--------------------")
        if menu_choice is 1 or menu_choice is "1":
            create_journal()
        elif menu_choice is 2 or menu_choice is "2":
            view_journal()
        elif menu_choice is 3 or menu_choice is "3":
            add_page()
        elif menu_choice is 4 or menu_choice is "4":
            enter_entry_content()
        elif menu_choice is 5 or menu_choice is "5":
            remove_page()
        elif menu_choice is 6 or menu_choice is "6":
            break
        else:
            print("Only enter given options")


use_journal()
