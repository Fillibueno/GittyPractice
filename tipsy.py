#x = 5
#age = 5
#greeting = "hello tipsy"
#print(greeting)
#print("goodbye dipsy")
#isItRainingOutside = True;
#notRainingOutside = False;

#if(isItRainingOutside):
    #print("Bring an umbrella")

#print(8//4.1)

#num = 5 #type int
#num2 = 5.0 #type float
#testVal = True #type boolean or true/false
#TestVal = False
#true/false can be represented as a 1/0
#print(type(testVal))
#print(type(num2))
#print(type(num))
#print(testVal)
#print(TestVal)

#we can turn strings to numbers, numbers to strings decimals(floats) to integers
#and integers to floats
#print(type(str(bool(1))))

#print("hello" + " this is a test")
#concatenation ^
#print("25" + str(25))
#camelcase is when the first word in a group is lowercase but the following
#words are capitalized
#they can contain numbers but may not start with them
#len=500 
#print(len)
#dont name stuff len
fooball1 = "lions"
football2 = "chiefs"
scoreLions = 0 
scoreChiefs = 0
TOUCHDOWN = 7
FIELDGOAL = 3
scoreLions += TOUCHDOWN
print(scoreLions, scoreChiefs)
scoreChiefs += TOUCHDOWN*2
print(scoreLions, scoreChiefs)
scoreLions += TOUCHDOWN
scoreChiefs += FIELDGOAL
print(scoreLions, scoreChiefs)
scoreLions += TOUCHDOWN
scoreChiefs += FIELDGOAL
print(scoreLions, scoreChiefs)
if(scoreLions > scoreChiefs):
    Lions = "Lions Win"
    Chiefs = "Chiefs Lose"
if(scoreLions < scoreChiefs):
    Lions = "Lions Lose"
    Chiefs = "Chiefs Win"
print(Lions, Chiefs)