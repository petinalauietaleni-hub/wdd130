# Adventure Game Milestone - Samuelu
# I added a third choice in the first scenario and plan to include a hidden path later in the game.

print("You wake up on a mysterious island. You see a BOAT, a CAVE, and a TRAIL. Which one do you want to explore?")
choice1 = input("Type BOAT, CAVE, or TRAIL: ").lower()

if choice1 == "boat":
    print("You approach the boat and find it half-sunken. Do you want to REPAIR it or SEARCH the shore for supplies?")
elif choice1 == "cave":
    print("You enter the cave and hear dripping water. Do you want to LIGHT a torch or LISTEN carefully?")
elif choice1 == "trail":
    print("You follow the trail and find footprints. Do you want to FOLLOW them or RETURN to the beach?")
else:
    print("That’s not a valid choice. Try again and choose BOAT, CAVE, or TRAIL.")