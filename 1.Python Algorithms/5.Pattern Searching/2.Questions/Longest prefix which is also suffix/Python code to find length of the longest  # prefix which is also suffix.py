# Python code to find length of the longest
# prefix which is also suffix
import re

s = "ABCABCABCABCABC" # Example input

print(len(re.findall(r'^(\w*).*\1$',s)[0]))
