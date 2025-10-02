# Adventure Game Milestone
# Creativity Note: I plan to add a hidden choice that unlocks a secret path and use lists to track inventory.

# First scenario
print("You wake up in a mysterious cave. You see a TORCH, a MAP, and a SWORD. Which one do you pick up?")
choice1 = input("Type TORCH, MAP, or SWORD: ").strip().lower()

if choice1 == "torch":
    print("You light the torch and see ancient carvings on the wall. A tunnel leads LEFT or RIGHT. Which way do you go?")
elif choice1 == "map":
    print("You study the map and notice a hidden exit behind a waterfall. Do you want to SEARCH for the waterfall or EXPLORE the cave?")
elif choice1 == "sword":
    print("You grip the sword and hear growling nearby. Do you want to FIGHT or RUN?")
else:
    print("That’s not a valid choice. You remain confused in the cave.")
