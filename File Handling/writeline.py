lines = ['This is the first line.\n',
         'Here comes the second line.\n',
         'The third line is next.\n',
         'Line number four is here.\n',
         'Fifth line coming through.\n',
         'And here is the sixth line.\n']

with open('Lines.txt', 'w') as f:
    f.writelines(lines)
