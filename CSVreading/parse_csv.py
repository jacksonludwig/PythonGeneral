# explaining the python with statement: https://effbot.org/zone/python-with-statement.htm
# Python 2 may use: with open("new_file.csv", "wb") instead of the 3 shown below)

# since import was used instead of from ... import *, you must access the import before
# using any members

import csv

# lines 5 and 6 open the names.csv file and put it into a csv reader Object
with open("names.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)

# the rest of the file opens a new file and writes the data that is found in names.csv
    with open("new_names.csv", "w", newline="") as new_file:
        csv_writer = csv.writer(new_file, delimiter="\t")
        for line in csv_reader:
            csv_writer.writerow(line)
            print(line, end="")
            print(" added to file!")
