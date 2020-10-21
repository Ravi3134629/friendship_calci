score=0
names=input("enter the names of 2 people: ")
for character in names:
    if character in "aeiou":
        score+=10
    if character in "friend":
        score+=15
print("your friendship score is: ",score)
if score>100:
    print("best friends!")