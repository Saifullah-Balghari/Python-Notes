with open("experimental.txt", "w") as f:
    f.write("Hi, my name is saifullah balghari. extra words.")
    f.truncate(34)   # set the length

# seek = move to position
with open("experimental.txt", "r") as f:
    print(f.tell()) # Print the current file position
    f.seek(3)  # Move the file pointer to position 3 (zero-based index)
    print(f.tell())  # Print the current file position
    print(f.read())  # Read and print the remaining content of the file

# f.truncate(...)   --> set the length
# f.tell() --> Print the current pointer position
# f.seek(...) --> Move the file pointer to position
