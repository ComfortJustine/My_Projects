print ("Welcome to my Quiz Game!")

playing = input ("Do you wanna to play? ")

if playing.lower() != "yes":
   # yes == Yes
   quit()
print("okay! Let's play: )")
score = 0

answer = input("What does CPU stand for?  ")
if answer.lower() == "central processing unit":
   print('Correct!')
   score += 1
else:
   print("Incorrect!")
    
answer = input("What does ROM stand for?  ")
if answer.lower() == "read only memory":
   print('Correct!')
   score += 1
else:
   print("Incorrect!")

    
answer = input("What does ALU stand for?  ")
if answer.lower() == "arithmetic logical unit":
   print('Correct!')
   score += 1
else:
   print("Incorrect!")

    
answer = input("What does JVM stand for?  ")
if answer.lower() == "java virtual machine":
   print('Correct!')
   score += 1
else:
   print("Incorrect!")

    
answer = input("What does RAM stand for?  ")
if answer.lower() == "random access memory":
   print('Correct!')
   score += 1
else:
   print("Incorrect!")

print("You got " +  str(score) + " questions correct!  ")

var = "You got {:.3f} %".format((score / 6) * 100)
var = f"You got {(score / 6) * 100} %"
print("You got {:.3f} %".format((score / 6) * 100))