def accept_login(users,a,b):
    if users.get(a)==b:
        return True
    else: False

users={"user1":"password1","user2":"password2","user3":"password3"}
if accept_login(users,input("Username?"),input("Password?")):
    print("Login successfully")
else:
    print("Login failed")
