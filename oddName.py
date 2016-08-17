"""
Michael
"""
user_name = input("Enter your name: ")
while user_name == "":
    user_name = input("Make sure field is not blank: ")
count = 1
for char in list(user_name):
    if count % 2 != 0:
        print(char)
        count += 1
    else:
        count +=1



