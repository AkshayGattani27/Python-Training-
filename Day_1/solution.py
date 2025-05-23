n=int(input("How many people ? "))
people = {}
for i in range(n):
    print()
    print (f"Person {i+1} :" )
    name = input("Enter name : ")
    age = int(input("Enter age : "))
    people[name] = age

print()
print(people)
#commented