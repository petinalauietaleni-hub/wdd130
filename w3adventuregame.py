# Adventure Game - Final Version by Petina Lauie Taleni.
# I added a third choice in the first scenario and a hidden path if the user types "secret".

print("You wake up on a mysterious island. You see a BOAT, a CAVE, and a TRAIL. Which one do you want to explore?")
choice1 = input("Type BOAT, CAVE, or TRAIL: ").lower()

if choice1 == "boat":
    print("You approach the boat and find it half-sunken. Do you want to REPAIR it, SEARCH the shore for supplies, or SIGNAL for help?")
    choice2 = input("Type REPAIR, SEARCH, or SIGNAL: ").lower()

    if choice2 == "repair":
        print("You patch the boat and set sail. A storm hits! Do you DROP anchor or KEEP sailing?")
        choice3 = input("Type DROP or KEEP: ").lower()
        if choice3 == "drop":
            print("You survive the storm and reach a nearby island. You’re safe!")
        elif choice3 == "keep":
            print("The storm capsizes your boat. You swim to shore, exhausted but alive.")
        else:
            print("Invalid choice. You hesitate and the storm overtakes you.")
    elif choice2 == "search":
        print("You find a flare and a map. Do you USE the flare or FOLLOW the map?")
        choice3 = input("Type USE or FOLLOW: ").lower()
        if choice3 == "use":
            print("A rescue plane sees your flare and picks you up!")
        elif choice3 == "follow":
            print("You discover a hidden bunker with supplies and shelter.")
        else:
            print("Invalid choice. You get lost in the jungle.")
    elif choice2 == "signal":
        print("You wave and shout. A nearby fisherman sees you. Do you TALK to him or HIDE?")
        choice3 = input("Type TALK or HIDE: ").lower()
        if choice3 == "talk":
            print("He offers you a ride back to the mainland. You’re saved!")
        elif choice3 == "hide":
            print("He leaves, unaware of your presence. You remain stranded.")
        else:
            print("Invalid choice. You miss your chance for help.")
    else:
        print("Invalid choice. You wander aimlessly by the boat.")

elif choice1 == "cave":
    print("You enter the cave and hear dripping water. Do you LIGHT a torch or LISTEN carefully?")
    choice2 = input("Type LIGHT or LISTEN: ").lower()

    if choice2 == "light":
        print("The torch reveals ancient markings. Do you FOLLOW them or IGNORE them?")
        choice3 = input("Type FOLLOW or IGNORE: ").lower()
        if choice3 == "follow":
            print("You discover a hidden treasure chamber!")
        elif choice3 == "ignore":
            print("You trip over a rock and sprain your ankle. You must rest.")
        else:
            print("Invalid choice. You wander deeper and get lost.")
    elif choice2 == "listen":
        print("You hear whispers. Do you CALL out or STAY silent?")
        choice3 = input("Type CALL or STAY: ").lower()
        if choice3 == "call":
            print("A voice responds and guides you to safety.")
        elif choice3 == "stay":
            print("You remain hidden and discover a secret exit.")
        else:
            print("Invalid choice. You panic and run into a wall.")
    else:
        print("Invalid choice. You stumble in the dark.")

elif choice1 == "trail":
    print("You follow the trail and find footprints. Do you FOLLOW them or RETURN to the beach?")
    choice2 = input("Type FOLLOW or RETURN: ").lower()

    if choice2 == "follow":
        print("You meet a stranger. Do you TRUST them or RUN?")
        choice3 = input("Type TRUST or RUN: ").lower()
        if choice3 == "trust":
            print("They lead you to a safe camp.")
        elif choice3 == "run":
            print("You escape but get lost in the forest.")
        else:
            print("Invalid choice. You freeze in fear.")
    elif choice2 == "return":
        print("You find a message in a bottle. Do you OPEN it or IGNORE it?")
        choice3 = input("Type OPEN or IGNORE: ").lower()
        if choice3 == "open":
            print("It contains coordinates to a rescue point!")
        elif choice3 == "ignore":
            print("You miss a chance for help and remain stranded.")
        else:
            print("Invalid choice. The tide washes the bottle away.")
    else:
        print("Invalid choice. You wander off the trail.")

elif choice1 == "secret":
    print("You discovered a hidden path! A glowing portal appears. Do you ENTER or WAIT?")
    choice2 = input("Type ENTER or WAIT: ").lower()
    if choice2 == "enter":
        print("You’re transported to a paradise island. You win!")
    elif choice2 == "wait":
        print("The portal fades. You missed your chance.")
    else:
        print("Invalid choice. The portal vanishes.")

else:
    print("That’s not a valid choice. Try again and choose BOAT, CAVE, or TRAIL.")
