#add the title of your story in a header format
print("~ Tales of UMBC ~")
#add a sub-header
print("(A work of Fiction)")
# add space
print()
#######################Intoduction########################################################
#add a decription of the story############################################################
print("You are a knight in the year 650 CE, and you're trying to become the most famous knight of them all.")
#add space
print()
#continue adding description
print("You decide to go on an adventure at Castle UMBC to earn your glory!")
#add space
print()
###########################################################################################
#continue adding more explanations  
A = "The local blacksmith, who needs a rare sword"
B = "The town's teacher, who has a question"
C = "The king, who needs a brave warrior"
print("You are outside the castle grounds, and see three different people asking for help. You could talk to: ")
print("   A. The local blacksmith, who needs a rare sword")
print("   B. The town's teacher, who has a question")
print("   C. The king, who needs a brave warrior")
answer = input("Who will you talk to? Please select option A through C: ")
print(answer)

##########################################################################################
# If the blacksmith is selected###########################################################
if answer == "A":
  print("You meet with the blacksmith, looking for a legendary sword.") 
  print("They tell you that the legend is that the sword is frozen in ice waiting to be found.")
  print("You chose to search for it:")

  #define the choices
  a = "In the Desert"
  b = "In the Forest"
  c = "In the Arctic"

  print("   a. In the Desert")
  print("   b. In the Forest")
  print("   c. In the Arctic")
#ask user to enter his/her choice
  choice1 = input("Please select option a through c:")
  print(choice1)
#add space
  print()
#add a situation with good ending using if statement
  if choice1 == "c":
    print("After looking long and hard through the arctic, you've found it - the legendary sword of programing! The blacksmith is thrilled and rewards you with a suit of armor worthy of a hero! ~ The End ~")
  else:
    print("You searched and searched for the rest of your life, but you never found it. It might've been a good idea to heed the blacksmith's advice and go to a cold place. ~ The End ~")



##########################################################################################
# if the town's teacher is selected#######################################################
if answer == "B":
  print("You meet with the town's teacher, who is asking you a question")
  print("'I have to be honest with you,' they say. 'I am not really qualified to teach and am struggling with this question.'")
  #add space
  print()
  print("They gesture to a math equation that reads as follows:")
  #add space
  print()
  print("y = 6 + 2 + 1")
  #add space
  print()
  #ask user to enter the solution to the problem
  solution = input("Please enter the solution to this problem: ")
  print(solution)
  #add if the user enter the correct answer using if-statement
  if solution == "9":
    print("'That makes perfect sense!' the teacher cries, and they award you with an honorary degree. You are forever known as one of the smartest in the land! ~ The End ~")
  else:
    print("'That makes no sense!' the teacher says, and they send you to exile. You are forever known as the dumbest person in the land!")

  
  
##########################################################################################
# if the King is selected#################################################################
if answer == "C":
  print("You meet with the king of UMBC, looking for a brave warrior. 'I need someone to conquer a nearby dragon to save the kingdom! There is no time, head east and be ready for battle!' ")
  #add space
  print()
  print("Yo head east and find the dragon. You ready yourself for battle. But in a twist, the dragon asks you to solve a riddle in exchange for your kingdom.")
  #add space
  print()
  print("'What two numbers, when added together, equal ten?'")
  #add space
  print()
  print("You ponder for a moment. There's multiple answers to this question, aren't there?")
  print("After thinking for a moment, you answer with two numbers...")
  #ask user to enter first and second numbers
  FirstNum = input("Enter the first number: ")
  FirstNum = int(FirstNum)
  print(FirstNum)
  SecondNum = input("Enter the second number: ")
  SecondNum = int(SecondNum)
  print(SecondNum)
  
  #King wins. Enter two numbers that add to 10
  if(FirstNum + SecondNum) == 10:
    print(f"'Ah yes,{FirstNum} and {SecondNum} add up to 10!' The dragon explained. The dragon decides to leave your kingdom alone, and the king declares you are the greatest hero in all the land! ~ The End ~ ")
  else: 
  #King loses: Enter two numbers that do not add to 10
    print(f"'Ah no, {FirstNum} and {SecondNum} do not add up to 10!' The dragon explained. The dragon decides to invade your kingdom! ~ The End ~ ")  














  








