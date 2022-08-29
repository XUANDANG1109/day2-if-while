# Ex1
legal = False

print("A")
if legal:
    print("B")
    print("C")
print("D")

# Ex2
age = int(input("what is your age?"))

print("A")
if age >= 10:
    print("B")
    print("C")
print("D")

# Ex3
age = int(input("what is your age?"))
print("A")
if age >= 10:
    print("B")
    if age >= 100:
        print("C")
    print("D")
print("E")

# Ex4
age = int(input("what is your age?"))
print("A")
if age >= 10:
    print("B")
if age >= 100:
    print("C")
    print("D")
print("E")

# Ex5
secret_code = input("What is the secret code?")

if secret_code == "NATO":
    print("correct")
print("not correct")

# Ex 6
secret_code = "NATO"
answer = input("what is the secret code?")

if secret_code == answer:
    print("correct")
else:
    print("not correct")

#Ex 7
secret_code1 = "NATO"
secret_code2 = "EU"

answer = input("what is the secret code?")
if answer == secret_code1 and answer == secret_code2:
    print("correct")
else:
    print("not correct")

#Ex 8
secret_code1 = "NATO"
secret_code2 = "EU"

answer = input("what is the secret code?")
if answer == secret_code1 or answer == secret_code2:
    print("correct")
else:
    print("not correct")

# Ex 8
secret_code1 = "NATO"
secret_code2 = "EU"

answer = input("what is the secret code?")
if answer == secret_code1 and answer == secret_code2 or 1 == 1:
    print("correct")
else:
    print("not correct")