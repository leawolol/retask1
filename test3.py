import re
f =open('data.txt', 'rt')
lines = f.readlines()
f.close()
regex = re.compile('delorean')
linecount = 0
for line in lines:
    m = regex.search(line)
    if m is not None:
        print(f"Found {regex.pattern} on line {linecount} at position {m.start()}")
    linecount = linecount + 1
