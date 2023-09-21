import random as rand

#rando = random.random()
#rando *= 256
#print(int(rando))

#dooby = rand.randint(1,(rand.randint(8,100)))

#print(dooby)
myList = ["agate", "renne", "estelle", "kloe", "joshua", "anelace", "mueller"]
prob = myList[rand.randint(0, len(myList)-1)]
print(prob)

def rollDie(sides):
    
    return rand.randint(1, sides)

print(rollDie(20))
print(rollDie(6))