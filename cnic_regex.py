import re

cnic = input("Enter cnic with dashes")

pattern = r"^\d{5}-\d{7}-\d{1}$"

if re.fullmatch(pattern,cnic):
    print("You have entered cnic, in correct format")

else:
    print("You have entered invalid cnic")