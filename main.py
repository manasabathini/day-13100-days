print("Check your grade")
testName = input("Type the name of the test: ")
print("Max score of the", testName,"is 100.")
score = int(input("Plese enter the score you received: "))
if score >=90 and score<=100:
  print("Your grade is A+")
elif score >=80 and score<=89:
  print("Your grade is A")
elif score >=70 and score<=79:
  print("Your grade is B")
elif score >=60 and score<=69:
  print("Your grade is c")
elif score>=50 and score<=59:
  print("Your grade is D")
else:
  print("Your grade is U")