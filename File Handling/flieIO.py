# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists

# f = open("experimental.txt", "w")
# f.write("Hi, my name is saifullah balghari................")
# f.truncate(34)
# f.close()

with open("experimental.txt", "w") as f:
    f.write("Hi, my name is saifullah balghari................")
    f.truncate(34)

with open("experimental.txt", "rt") as f:
    print(f.read())

