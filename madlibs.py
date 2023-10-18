passage = '''You are an expert at sorry and keeping lines blurry
Never impressed by me acing your tests
All the girls that you've run dry have tired lifeless eyes
'Cause you burned them out
But I took your matches before fire could catch me
So don't look now 
I'm shining like fireworks over your sad empty town'''
newPassage = ""
start = passage[0]
end = passage[21]
newPassage += passage[start:end]
newPassage += input("enter a word here: ")
start = passage[26]
end = passage[39]
newPassage += passage[start:end]
newPassage += input("enter a plural noun here: ")
start = passage[44]
end = passage[58]
newPassage += passage[start:end]
newPassage += input("enter a verb here: ")
start = passage[67]
end = passage[85]
newPassage += passage[start:end]
newPassage += input("enter a plural noun here: ")
start = passage[90]
end = passage[99]
newPassage += passage[start:end]
newPassage += input("enter a plural noun here: ")
start = passage[104]
end = passage[117]
newPassage += passage[start:end]
newPassage += input("enter a past tense verb here: ")
start = passage[124]
end = passage[130]
newPassage += passage[start:end]
newPassage += input("enter an adjective here: ")
start = passage[135]
end = passage[145]
newPassage += passage[start:end]
newPassage += input("enter a body part here: ")
start = passage[149]
end = passage[157]
newPassage += passage[start:end]
newPassage += input("enter a pronoun here: ")
start = passage[3]
end = passage[3]
newPassage = passage[start:end]
newPassage += input("enter a verb here: ")
start = passage[167]
end = passage[181]
newPassage += passage[start:end]
newPassage += input("enter a pronoun here: ")
start = passage[182]
end = passage[193]
newPassage += passage[start:end]
newPassage += input("enter a plural flamable object here: ")
start = passage[200]
end = passage[208]
newPassage += passage[start:end]
newPassage += input("enter a hot object here: ")
start = passage[212]
end = passage[219]
newPassage += passage[start:end]
newPassage += input("enter a verb here: ")
start = passage[224]
end = passage[237]
newPassage += passage[start:end]
newPassage += input("enter a verb here: ")
start = passage[3]
end = passage[3]
newPassage += passage[start:end]
newPassage += input("enter either 'now', 'soon', or 'then' here: ")
start = passage[245]
end = passage[251]
newPassage += passage[start:end]
newPassage += input("enter present tense verb here: ")
start = passage[258]
end = passage[264]
newPassage += passage[start:end]
newPassage += input("enter noun here: ")
start = passage[273]
end = passage[284]
newPassage += passage[start:end]
newPassage += input("enter adjective here: ")
start = passage[293]
end = passage[293]
newPassage = passage[start:end]
newPassage += input("enter adjective here: ")
start = passage[293]
end = passage[300]
newPassage += passage[start:end]
print(newPassage)

#def madlibsJoiner(passage,prompt,start, end):
    #return(passage[start:end]+input(prompt))

#nputPrompt = "Please enter"
 #+= madlibsJoiner(passage, inputPrompt, )