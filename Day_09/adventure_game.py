while True:
    
    choice_01 = int(input("""

        1. Enter the dark cave.
        2. Follow the path through the forest."

    """))

    if choice_01 == 1:
        print("You chose to enter the dark cave. Inside, you find a treasure chest.")
        choice_02 = int(input("""

            1. Open the chest.
            2. Leave the cave.

    """))
    
        if choice_02 == 1:
            print("You chose to open the chest. Congratulations! You found a valuable gem.")
        elif choice_02 == 2:
            print("You leave the cave.")
            break
        else:
            print("You leave the cave")
            raise ValueError("Vous avez entre une valeur invalide")
    elif choice_01 == 2:
        print("You follow the path through the forest.")
        break
    else:
        raise ValueError("Vous avez entre une valeur invalide")
    break