import getpass

users =[
    {
        'username': 'aden',
        'password': 'aden'
    }
]

print ("====================================================")
print ("                PROGRAM RUMAH SAKIT                 ")
print ("====================================================")

input_user =input("Username:")
input_pass =getpass.getpass("Password:")

def out():
    print("Silahkan")

for user in users:
    if input_user == user['username'] and input_pass == user['password']:
        out()
    else:
        exit()