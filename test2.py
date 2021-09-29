import re

# Have some text to test that we display at start so its obvious 
text = ("Silence, Earthling! My Name Is Darth Vader. I Am An Extraterrestrial From The Planet Vulcan. 12/11/1985 ")
print(text)

# Ask user for a pattern
pattern = (input('Pattern input: '))

# Build the regular expression for the pattern entered in
regex = re.compile(pattern)

# Search for  expression in the string
matches = regex.finditer(text)

if matches is not None:
    for match in matches:
        print(f"found {regex.pattern} at position {match.start()}")
else:
    # display a message if regex was not found as macth object has been created.
    print(f"{regex.pattern} was not found")
