# Very simple program to play with Regex. It is obvious.
import re

# Have some text to test that we display at start so its obvious 
text = ("Silence, Earthling! My Name Is Darth Vader. I Am An Extraterrestrial From The Planet Vulcan. 12/11/1985 ")
print(text)

# Ask user for a pattern
pattern = (input('Pattern input: '))

# Build the regular expression for the pattern entered in
regex = re.compile(pattern)

# search the expression in the string
m = regex.findall(text)

# Check if the object was created
if m is not None:
    print(f"Found {m}")
else:
# Display message if object wa not created
    print(f"{regex.pattern} was not found")
