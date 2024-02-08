name = "saifullah"
nameLen = len(name)
print(nameLen)
print(name[0:9])              # including 0 but not 9
print(name[:9])               # 0 is automatically placed
print(name[1:9])              # including 1 but not 9
print(name[0:-5])             # length of name is placed before and subtracted frome the negative number  
print(name[0:len(name)-5])    # Hypothetically new statement is print(name[0:4]) 
print(name[-5:9])             # Hypothetically new statement is print(name[4:9])
print(name[-5:-2])            # Hypothetically new statement is print(name[4:7])
print(name[:])                # 0 and length of string is automatically placed and new statement will be print(name[0:9]) 

# etc