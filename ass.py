from random import randint

P1 = input("P1, choose FOLD or UNFOLD (or type 'exit' to quit): ").upper()

if P1 == "EXIT":
    print("Game over. Thanks for playing!")
elif P1 not in ["FOLD", "UNFOLD"]:
    print("Invalid choice. Please choose FOLD or UNFOLD.")
else:
    C2 = "UNFOLD" if P1 == "FOLD" else "FOLD"
    C3 = "FOLD" if randint(1, 2) == 1 else "UNFOLD"

    print(f"P1: {P1}")
    print(f"C2 picks: {C2}")
    print(f"C3 picks: {C3}")

    if (P1 == "FOLD" and C2 == "FOLD") or (P1 == "UNFOLD" and C2 == "UNFOLD"):
        print("Result: It's a tie!\n")
    elif (P1 == "FOLD" and C2 == "UNFOLD"):
        print("Result: P1 wins.\n")
    elif (P1 == "FOLD" and C3 == "UNFOLD"):
        print("Result: P1 wins.\n")
    elif (P1 == "UNFOLD" and C2 == "FOLD"):
        print("Result: C2 wins.\n")
    else:
        print("Result: C2 wins the game.\n")
