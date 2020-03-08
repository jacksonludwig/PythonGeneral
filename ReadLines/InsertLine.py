import fileinput
for line in fileinput.FileInput("D:\\app-of-elements\\app\\src\\main\\res\\layout\\activity_periodic_table.xml", inplace=1):
    if "android:background" in line:
        line = line.replace(line, line+"\nandroid:onClick=\"openInfoMenu\"")
    print(line, end='')
