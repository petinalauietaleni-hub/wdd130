# Adventure Game Milestone Submission
# Creativity Note: I plan to add hidden and a fouth level of depth to exceed requirement.

print("You wake up on a deserted island with two items nearby: a MAP and a COMPASS. Which one do you want to pick up?")
choice1 = input("Type MAP or COMPASS:").strip().lower()

if choice1 == "map":
   print("You pick up the map and see a trail leading into the jungle. Do you want to FOLLOW the trail or EXPLORE the beach?")
elif choice1 == "compass"
     print("You pick up the compass and notice it pointing towards a rocky hill. Do you want to CLIMB the hill or SEARCH the nearby cave?")
else:
    print("That's not a valid choice. You hesitate too long and a storm begins to roll in")
