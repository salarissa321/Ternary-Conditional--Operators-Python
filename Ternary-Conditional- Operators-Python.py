



#------------------------------------------------
#----Ternary Conditional Operators---------
#------------------------------------------------

# country = "Kuwait"

if country == "Deutschland" : print(f"The Weather in {country} is 15") # # The Weather in Deutschland is 15
     
elif country == "KSA" : print(f"The Weather in {country} is 30") # The Weather in KSA is 30
     
else : print("Country is nicht in The List") # Country is nicht in The List


# Short if

movieRate = 18
age = 16

if age < movieRate :
    print("Movie is Not good for you")  # Condition if True

else:
    print("The Movie is good for You and happy watching") # Condition if False

print("Movie is not good for you" if age < movieRate else "Movie is good for you and happy Watching")

# Coindition If True + If Condition + Else + Condition If False