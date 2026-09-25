AllNumbers = "1234567890"
SpecialNums = "!@#$%^&*()_-+=±§:;>.<,?/""''| {}[]`~¡™£¢∞§¶•ªº–≠œ∑´®†¥¨ˆøπ“‘åß∂ƒ˙∆˚¬…æ«`Ω≈ç√∫˜µ≤≥÷"
Contains8Chars = False
Password = input("Enter the password: ")
if len(Password) >= 8:
    print(f"Your password is 8 characters or more. It is exactly {len(Password)} characters. ")
    Contains8Chars = True
else:
    print(f"Your password is less than 8 characters. It is exactly {len(Password)} characters. ")

ContainsNum = False
for character in Password:
    if character in AllNumbers:
        print("Your password contains numbers.")
        ContainsNum = True
        break 
if ContainsNum == False:
    print("Your password does not include numbers.")

ContainsSpecChar = False
for character in Password:
    if character in SpecialNums:
        print("Your password contains special characters.")
        ContainsSpecChar = True
        break 
if ContainsSpecChar == False:
    print("Your password does not include special characters.")

if ContainsNum == True and ContainsSpecChar == True and Contains8Chars == True:
    print("Your password is very strong! Rating: 3/3")

elif ContainsNum == True and ContainsSpecChar == True or ContainsNum == True and Contains8Chars == True or ContainsSpecChar == True and Contains8Chars == True:
    print("Your password is strong. Rating: 2/3")

else:
    print("Your password is weak. Rating: 1/3")
