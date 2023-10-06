passage = '''You are an expert at sorry and keeping lines blurry
Never impressed by me acing your tests
All the girls that you've run dry have tired lifeless eyes
'Cause you burned them out
But I took your matches before fire could catch me
So don't look now 
I'm shining like fireworks over your sad empty town
Dear John, I see it all now that you're gone
Don't you think I was too young to be messed with?
The girl in the dress cried the whole way home
I see it all now that you're gone
Don't you think I was too young to be messed with?
The girl in the dress wrote you a song
You should've known'''
start = 0
end = 99
npass = ""
npass += passage[start:end]
npass += input("enter a plural noun here: ")
epass = ""
epass += passage[104:193]
epass += input("enter a plural flamable object here: ")
wpass = ""
wpass += passage[200:242]
wpass += input("enter either 'now', 'soon', or 'then' here: ")
dpass = ""
dpass += passage[245:251]
dpass += input("enter present tense verb here: ")
xpass = ""
xpass += passage[258:264]
xpass += input("enter noun here: ")
spass = ""
spass += passage[274:284]
spass += input("enter adjective here: ")
mpass = ""
mpass += passage[287]
mpass += input("enter adjective here: ")
mpass += passage[293:299]
print(npass)
print(epass)
print(wpass)
print(dpass)
print(xpass)
print(spass)
print(mpass)