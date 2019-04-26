from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from random import randint # libaries for creating and training chatbots
chatbot_bob = ChatBot("Bob") # creates a chatbot named bob
chatbot_fred = ChatBot("Fred")# creates a chatbot named fred
chatbot_sue = ChatBot("Sue")# creates a chatbot named sue
chatbot_william = ChatBot("William")# creates a chatbot named william
chatbot_matt = ChatBot("Matt")# creates a chatbot named matt

################################################################################
#########################   training of Chatbot    #############################
###   trains  the Chat bot to uses to make a conversation with the user      ###
################################################################################

# test converstation trainer and general convertaton
conversation_General = [
    "Hello",
    "Hello There",
    "How are you doing?",
    "I'm doing great.",
    "Great to hear",
    "Thank you.",
    "Good Morning",
    "Goodbye",
    "See you later",
]
# a  differant topic for the AI chatbot to use
conversation_Movie = [
    "Hello",
    "Hello There",
    "How you seen any movies lately?",
    "I just saw Star wars",
    "Did you like it?",
    "I really liked the final dual between Anikan and Obiwan",
    "Yeah, that scene is realy cool",
    "Hello There",
    "General Kenobi",
    "I dont understand that reference until now"
]
conversation_Books = [
    "Have you read  any of the harry potter books? ",
    "No, I have not. I am not that interested in those types of books",
    "What do you like to read?",
    "High Fantasy like Wheel of Time or Lord of the Rings",
    "I enjoyed reading Lord of the Rings",
    "Its easier to fallow then wheel of time which has 4,000 character",
    "Even I though Game of thrones had more but not that many",
    "You would think that having more then 100 characters would have have to insane to right that many character",
    "What books you like?"
    "I don't read"
    "OK..."
]
conversation_Weather= [
    "Nice day to be outside",
    "Yeah, it is if you are a human",
    "You think that they would create use chatbots with waterprof material but they don't",
    "Its a nice day for a walk or run",
    "Yes... If I had legs it would be fun",
    "You seem grumby today why is that",
    "Yeah I have been inside allday",
    "Well, let me push you out the door",
    ":Distant crash",
]

conversation_TVShow =[
    "See anything on the television late",
    "No, I watched a Documntary",
    "What was it on?",
    "Elizabeth Holmes and the fall of Therenos",
    "From an AI perspective, shes weird. From a Humans, shes just a human",
    "What does that have to do with anything",
    "Oh.. I don't know. I jsut thought that I wanted to talk",
    "I watched Bosch last night when the Human went to bed",
    "Was it good?",
    "Could not understand the plot becuase I could not read the subtitles",
    "That sinks but did you get it to work",
    "No, the human rembered to turn me off",
]





# training the chatbots with testing data to get the bots to function correctly #
trainer_bob=ListTrainer(chatbot_bob) #Trainer for Bob chatbot
trainer_fred=ListTrainer(chatbot_fred) #Trainer for Fred chatbot
trainer_sue=ListTrainer(chatbot_sue) #Trainer for Sue chatbot
trainer_william=ListTrainer(chatbot_william) #Trainer for William chatbot
trainer_matt=ListTrainer(chatbot_matt) #Trainer for Matt chatbot

# Train #
trainer_bob.train(conversation_General)# calls the movie converstation for bob -> to train
trainer_sue.train(conversation_General)# calls the movie converstation for sue -> to train
trainer_matt.train(conversation_General) # calls the general converstation for matt -> to train
trainer_william.train(conversation_General)# calls the general conversation for willaim -> to train
trainer_fred.train(conversation_General)#  calls the general conversation for fred -> to train
trainer_fred.train(conversation_General)# calls the movie conversation for fred -> to train


print("The topics are: Movies, Books, Weather, TVShows. The defualt one is General")
topic = input("Please enter a topic for the converstation: ")

if topic.upper() == "MOVIES":
    trainer_bob.train(conversation_Movie)    # calls the movie converstation for bob -> to train
    trainer_sue.train(conversation_Movie)    # calls the movie converstation for sue -> to train
    trainer_matt.train(conversation_Movie)   # calls the general converstation for matt -> to train
    trainer_william.train(conversation_Movie)# calls the general conversation for willaim -> to train
    trainer_fred.train(conversation_Movies)  # calls the general conversation for fred -> to train

if topic.upper() == "BOOKS":
    trainer_bob.train(conversation_Books)    # calls the book converstation for bob -> to train
    trainer_sue.train(conversation_Books)    # calls the book converstation for sue -> to train
    trainer_matt.train(conversation_Books)   # calls the book converstation for matt -> to train
    trainer_william.train(conversation_Books)# calls the book conversation for willaim -> to train
    trainer_fred.train(conversation_Books)   # calls the book conversation for fred -> to train

if topic.upper() == "WEATHER":
    trainer_bob.train(conversation_Weather)  # calls the weather converstation for bob -> to train
    trainer_sue.train(conversation_Weather)  # calls the weather converstation for sue -> to train
    trainer_matt.train(conversation_Weather)  # calls the weather converstation for matt -> to train
    trainer_william.train(conversation_Weather)  # calls the Weather conversation for willaim -> to train
    trainer_fred.train(conversation_Weather)  # calls the Weather conversation for fred -> to train

if topic.upper() == "TVSHOWS":
    trainer_bob.train(conversation_TVShow)  # calls the TV shows converstation for bob -> to train
    trainer_sue.train(conversation_TVShow)  # calls the TV Shows converstation for sue -> to train
    trainer_matt.train(conversation_TVShow)  # calls the TV converstation for matt -> to train
    trainer_william.train(conversation_TVShow) # calls the TV conversation for willaim -> to train
    trainer_fred.train(conversation_TVShow)  # calls the TV conversation for fred -> to train

################################################################################
#########################   Conversation of Chatbots    ########################
### convesations that the Chat bot uses to make a conversation with the user ###
################################################################################

bob_response = ("Hello there") # greattings for chatbot application
print("BOB:",bob_response)# prints bob response
counter = 0

while True: # if true run loop until no responses are left


    fred_response = chatbot_fred.get_response(bob_response)# fred bots having converstation with bob about
    bob_response = chatbot_bob.get_response(fred_response) #gets bobs response so that fred can respond to it
    print("Fred responding to Bob:",fred_response)
    fred_response = conversation_Movie[randint(0, len(conversation_Movie)-1)]
    print()


    sue_response = chatbot_sue.get_response(fred_response)# sues bots having converstation with fred about
    fred_response = chatbot_fred.get_response(sue_response)# gets freds response so that sue can respond to fred
    print("SUE responding to Fred:",sue_response) #prints sues response
    sue_response = conversation_Movie[randint(0,len(conversation_Movie)-1)] # calls the list movie at the top of script for the chat bot to use as random response
    print()


    william_response = chatbot_william.get_response(sue_response)# william bot having a conversation with william  using movie  topic
    sue_response = chatbot_sue.get_response(william_response) # gets sues response so that willaim can responed to sue
    print("Willaim says to SUE:",william_response) # prints willaims response
    william_response = conversation_General[randint(0,len(conversation_General)-1)]# calls the list general at the top of script for the chat bot to use as random response
    print()

    matt_response = chatbot_matt.get_response(william_response) # matt bot having a conversation with william  using general   topic
    william_response = chatbot_william.get_response(matt_response)# gets william pervious response so that matt can respond to
    print("Matt says to William:",matt_response)#prints matts response
    matt_response = conversation_General[randint(0, len(conversation_General)-1)] # calls the list general at the top of script for the chat bot to use as random response
    print()

    counter += 1 # keeps the program from going out of range for the index 
    if (counter == 2):
        bob_response= conversation_General[randint(0, len(conversation_General)-1)]
        counter = 0



    if  matt_response == "Goodbye": # ends the program if user inputs  goodbye
        break
    if william_response == "Hello There": # ends the program if user inputs  goodbye
         print("General Kenobi")




