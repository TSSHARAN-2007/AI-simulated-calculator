#Sharan's calculator:

print("Hey, I hope you are doin' good! I am yours friendly neighbourhood AI-simulated calculator.")
print("Choose your answer between yes and no.")

a = input()

if a == "yes":
   print("That's great!")
else:
    print("That's sad to hear from you...")

print("Okay, you can begin to test my efficiency on dual-numbered calculations:")
a = int(input("Choose number 1: "))
b = int(input("Choose number 2: "))
print("A = Add", ("S = Subtract"), ("M = Multiply"), ("D = Divide"), ("E = Exponent"), ("R = Remainder"))
c = input("Choose the respective operation: ")

if c == "A":
  print("Answer:", a+b) 
elif c == "S":
    print("Answer:", a-b)
elif c == "M":
     print("Answer:", a*b)
elif c == "D":
     print("Answer:", a/b)
elif c == "E":
    print("Answer:", a**b)
elif c == "R":
     print("Answer:", a%b)
else:
    print("Try again!")

print("Thank you for utilising me. If you ever nee any help regarding simple calculations, I'll cover your back. Bye for now!")   