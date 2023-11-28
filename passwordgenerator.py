import random, string

def generate_password(len, complex):
    password = ""
    if complex == 1:
        for i in range(len):
            password += random.choice(string.ascii_letters + string.ascii_uppercase)
    elif complex == 2:
        for i in range(len):
            password += random.choice(string.ascii_letters + string.ascii_uppercase + string.digits)
    elif complex == 3:
        for i in range(len):
            password += random.choice(string.ascii_letters + string.ascii_uppercase + string.digits + string.punctuation)
    return password

len = int(input("Longueure du mot de passe :"))
complex = int(input("Complexitée du mot de passe (1 -> 3) :"))

print(generate_password(len, complex))
