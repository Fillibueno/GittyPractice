passage = '''You are an expert at sorry and keeping lines blurry
Never impressed by me acing your tests
All the girls that you've run dry have tired lifeless eyes
'Cause you burned them out
But I took your matches before fire could catch me
So don't look now 
I'm shining like fireworks over your sad empty town'''
apass = ""
apass += passage[0:21]
apass += input("enter a word here: ")
bpass = ""
bpass += passage[26:39]
bpass += input("enter a noun here: ")
cpass = ""
cpass += passage[44:58]
cpass += input("enter a verb here: ")
dpass = ""
dpass += passage[67:85]
dpass += input("enter a plural noun here: ")
epass = ""
epass += passage[90:99]
epass += input("enter a plural noun here: ")
fpass = ""
fpass += passage[104:117]
fpass += input("enter a past tense verb here: ")
gpass = ""
gpass += passage[124:130]
gpass += input("enter an adjective here: ")
hpass = ""
hpass += passage[135:145]
hpass += input("enter a body part: ")
ipass = ""
ipass += passage[149:157]
ipass += input("enter a pronoun here: ")
jpass = ""
jpass += passage[160:161]
jpass += input("enter a verb here: ")
upass = ""
upass += passage[167:181]
upass += input("enter a pronoun here: ")
kpass = ""
kpass += passage[182:193]
kpass += input("enter a plural flamable object here: ")
lpass = ""
lpass += passage[200:208]
lpass += input("enter a hot object here: ")
mpass = ""
mpass += passage[212:219]
mpass += input("enter a verb here: ")
npass = ""
npass += passage[224:242]
npass += input("enter either 'now', 'soon', or 'then' here: ")
ppass = ""
ppass += passage[246:251]
ppass += input("enter present tense verb here: ")
qpass = ""
qpass += passage[258:264]
qpass += input("enter noun here: ")
rpass = ""
rpass += passage[273:284]
rpass += input("enter adjective here: ")
spass = ""
spass += passage[287]
spass += input("enter adjective here: ")
tpass = ""
tpass += passage[293:299]
newpass = ""
newpass += apass
newpass += bpass
newpass += cpass
newpass += dpass
newpass += epass
newpass += fpass
newpass += gpass
newpass += hpass
newpass += ipass
newpass += jpass
newpass += upass
newpass += kpass
newpass += lpass
newpass += mpass
newpass += npass
newpass += ppass
newpass += qpass
newpass += rpass
newpass += spass
newpass += tpass
print(newpass)