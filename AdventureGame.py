"""
Author: Marcelo Duarte

Purpose: In a text-based adventure game, the user is presented a scenario with different options.
Depending on the option they choose, they have different consequences, which in turn present 
different choices for the next action
"""

print(" ========== Adventure Game =============")
print()
answer1 = input ("You are walking through a dark forest and find two items: a MATCH and a FLASHLIGHT.  Which one do you want to pick up?")
# ===========================================
# Tratament of cenary MATH ===========================================
# ===========================================
if answer1.upper() == "MATCH":
    answer2 = input ("You pick up the match and strike it, and for an instant, the forest around you is illuminated. You see a large grizzly bear, and then the match burns out. Do you want to RUN, or HIDE behind a tree?")
    if answer2.upper() == "RUN":
      print("Go ahead and running faster for to scape of bear and fire")
    elif answer2.upper() == "HIDE":
      print("make silence until the bear go away")
    else:
      print("Please choose between RUN or HIDE")
# ===========================================
# Tratament of cenary FLASHLIGHT ===========================================
# ===========================================
elif answer1.upper() == "FLASHLIGHT":
  answer3 = input ("You pick up the flashlight and turn it on. You see the pathway lit up in front of you, but you thought you also heard something off to the side. Do you want to FOLLOW the path or LOOK in the trees for the thing that made the noise?")
  if answer3.upper() == "FOLLOW":
   print("Great choose, now follow until back off the florest")   
  elif answer3.upper() == "LOOK":
     answer4 = input ("Wow, you are courageous!looking through the trees you notice that the fire is spreading quickly, what do you do? SCREAM, CRY or PRAY  ") 
     if answer4.upper() == "SCREAM":
      print("Scream as loud as you can, maybe someone will hear you.")
     elif answer4.upper() == "CRY":
      print("Complicated situation, but crying now will only dehydrate you more.")
     elif answer4.upper() == "PRAY":
      print("Tt looks like today is your lucky day. Be calm, firefighters have already located you for your safe return home.")
     else:
      print("Please choose between SCREAM, RUN or PRAY")           
  else:
   print("Please choose between FOLLOW or LOOK")   
else:
   print("Please choose between MATCH or FLASHLIGHT")