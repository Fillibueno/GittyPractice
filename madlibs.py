passage = '''You are an expert at sorry and keeping lines blurry
Never impressed by me acing your tests
All the girls that you've run dry have tired lifeless eyes
'Cause you burned them out
But I took your matches before fire could catch me
So don't look now 
I'm shining like fireworks over your sad empty town'''
newPassage = ""


def madlibsJoiner(passage,prompt,start, end):
    return(passage[start:end]+input(prompt))

inputPrompt = "Please enter a word here: "
newPassage += madlibsJoiner(passage, inputPrompt, 0, 21)
newPassage += madlibsJoiner(passage, "enter a noun here:", 26, 39)
newPassage += madlibsJoiner(passage, "enter a verb here:", 44, 58)
newPassage += madlibsJoiner(passage, "enter a plural noun here: ", 67, 85)
newPassage += madlibsJoiner(passage, "enter a past tense verb here: ", 26, 39)
newPassage += madlibsJoiner(passage, "enter an adjective here: ", 90, 99)
newPassage += madlibsJoiner(passage, "enter a body part: ", 104, 117)
newPassage += madlibsJoiner(passage, "enter a pronoun here: ", 124, 130)
newPassage += madlibsJoiner(passage, "enter a verb here: ", 135, 145)
newPassage += madlibsJoiner(passage, "enter a pronoun here: ", 160, 161)
newPassage += madlibsJoiner(passage, "enter a plural flamable object here: ", 167, 181)
newPassage += madlibsJoiner(passage, "enter a hot object here: ", 182, 193)
newPassage += madlibsJoiner(passage, "enter a verb here: ", 200, 208)
newPassage += madlibsJoiner(passage, "enter either 'now', 'soon', or 'then' here: ", 212, 219)
newPassage += madlibsJoiner(passage, "enter present tense verb here: ", 224, 242)
newPassage += madlibsJoiner(passage, "enter noun here: ", 246, 251)
newPassage += madlibsJoiner(passage, "enter a hot object here: ", 258, 264)
newPassage += madlibsJoiner(passage, "enter a verb here: ", 273, 284)
newPassage += madlibsJoiner(passage, "enter adjective here: ", 287, 287)
print(newPassage)