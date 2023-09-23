with open("input.txt", "r") as f:
    text = f.read()
import re
shetchic = 0
for i in re.split('\. ',text):
    if i[0].isupper( ):
        shetchic += 1
for i in re.split('\! ',text):
    if i[0].isupper( ):
        shetchic += 1
for i in re.split('\? ',text):
    if i[0].isupper( ):
        shetchic += 1
print(shetchic - 2)
    
