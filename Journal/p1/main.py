import datetime
import os

author = "testAuthor"


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


def enter_entry_supplemental():
    title = input("Enter a title for this entry:\n")
    content = enter_entry_content()
    file = title.replace(" ", "") + ".txt"
    entry = open(file, "a")
    entry.write(author + "\n")
    entry.write(title + "\n")

    char_count = 0
    word_start_index = 0
    for i in range(0, len(content) - 1):
        if content[i] == " ":
            entry.write(content[word_start_index:i])
            char_count += 1
            word_start_index = i
        if char_count == 10:
            char_count = 0
            entry.write("\n")

    entry.write("\n" + str(datetime.datetime.now()))
    entry.close()


create_journal()
view_journal()
enter_entry_supplemental()
