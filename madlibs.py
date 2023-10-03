passage = '''You are an expert at sorry and keeping lines blurry
Never impressed by me acing your tests
All the girls that you've run dry have tired lifeless eyes
'Cause you burned them out
But I took your matches before fire could catch me
So don't look now
I'm shining like fireworks over your sad empty town'''
start = 0
end = 99
npass = ""
npass += passage[start:end]
npass += input("enter plural noun here")
print(npass)
epass = ""
epass += passage[105:-34]
epass += input("enter plural bright objects")
print(epass)
wpass = ""
wpass += passage[-24:-5]
wpass += input("enter singular object here")
print(wpass)