# #users input
# 3Username= input("enter username")
# Password= input("enter password")

# if Username == "admin" and Password == "1234":
#     print("login successful")

# else:
#     print("unsuccessful login")


# days= ["Monday","Tuesday","wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# num= int(input("enter a number between 1-7"))
# if num >=1 and num<=7:
#         print(f"the day of the week is {list(days)[num-1]}")
# else:
#         print("invalid ") 

#users input
# Username= input("enter username")
# Password= input("enter password")

# if Username == "admin" and Password == "1234":
#    role=input("what is your role")
#    if role == "Viewer":

#         print("admin logged in as viewer")

#         if role=="editor":

#             print("admin logged in as editor")

#             if role  "viewer" 

# else:
#     print("unsuccessful login")

login = input("Please, enter login: ")
pas = input("Please, enter password: ")
if login == "admin" and pas == "1234":
    print("What is your role? (Viewer, Editor)")
    if input() == "Viewer":
        print("Admin logged in as Viewer")
    elif input() == "Editor":
        print("Admin logged in as Editor")
    else:
        print("Unknown role")
else:
    print("Invalid login or password")


