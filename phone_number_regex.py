import re

from pytz import country_timezones

country = int(input("""Select country for which you want to enter number
                1. Pakistan
                2. India
                3. UK
                4. USA
                5. SaudiArabia
                """))

number = input("Enter number in correct format")

if country == 1:
     pattern = r"^(?:\+92|0)3\d{9}$"
     if re.fullmatch(pattern, number):
        print("Valid Pakistani phone number")
     else:
        print("Invalid Pakistani phone number format")

if country == 2:
     pattern = r"^(?:\+91|0)\d{10}$"
     if re.fullmatch(pattern, number):
        print("Valid India phone number")
     else:
        print("Invalid India phone number format")

if country == 3:
     pattern = r"^(?:\+44|0)7\d{9}$"
     if re.fullmatch(pattern, number):
        print("Valid UK phone number")
     else:
        print("Invalid UK phone number format")

if country == 4:
     pattern = r"^(?:\+1|1)\d{10}$"
     if re.fullmatch(pattern, number):
        print("Valid USA phone number")
     else:
        print("Invalid USA phone number format")

if country == 5:
     pattern = r"^(?:\+966|0)5\d{8}$"
     if re.fullmatch(pattern, number):
        print("Valid Saudi Arabia phone number")
     else:
        print("Invalid Saudi Arabia phone number format")