from random import randint

user = input("FOLD OR UNFOLD? ")

print(f"USER : {user} ")
C2 = randint(1,2)
if C2 == 1:
    print("C2 : FOLD")
else:
    print("C2 : UNFOLD")

C3 = randint(1,2)
if C3 == 1:
    print("C3 : FOLD")
else:
    print("C3 : UNFOLD")

        
if (user == "FOLD" and C2 == 1 and C3 == 1) or (user == "UNFOLD" and C2 == 2 and C3 == 2):
    print("DRAW")

elif (user == "FOLD" and C2 == 2 and C3 == 1) or (user == "UNFOLD" and C2 == 1 and C3 == 2):
    print("C2 wins")


elif (user == "FOLD" and C2 == 1 and C3 == 2) or (user == "UNFOLD" and C2 == 2 and C3 == 1):
    print("C3 wins")


elif (user == "UNFOLD" and C2 == 1 and C3 == 1) or (user == "FOLD" and C2 == 2 and C3 == 2):
    print("User wins")

else:
    print("TRY AGAIN")