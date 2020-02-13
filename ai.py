import random 

# DEFINE THE FUNCTIONS
# 1. chatbot
def chatbot():
    print("Hello. I'm Chatbot. ")
    user_name = get_name()
    user_mood_response = get_mood(user_name)
    print(user_mood_response)
    if user_mood_response == "Sorry to hear that.":
        print(therapist())
    else: 
        random_question()
        print(random_answer())

# 2. function to get user's name
def get_name():
    res = input("What is your name? ")
    return res

# 3. function to get the user's mood. Note this has a flaw: if the user uses one of the key words along with a qualification, the app might get confused (for example, the response "not bad" shoul be positive, but the app would treat it as negative.)
def get_mood(name):
    res = input("How are you {}? ".format(name)).lower()
    print(res)
    if res.__contains__("good") or res.__contains__("great"):
        return "Glad to hear it."  
    elif res.__contains__("sad") or res.__contains__("bad"):
        return "Sorry to hear that."
    else:
        return "Right."
     
# 4. 
def therapist():
    res = input("Tell me what's wrong. ").lower()
    res_list = res.split()
    if len(res_list) >= 2:
        echo = res_list[-2] + " " + res_list[-1]
    else: 
        echo = res
    stripped = echo.strip(".,!?")
    answer = random.choice(["Oh dear.", "Toughen up!", "I see.", "How does that make you feel?", "You fool!"])
    return "{}? {}".format(stripped, answer)

# 5. creates a set of stock answers to make it sound like the chatbot is listening to the user.
def random_answer():
    answers = ["Interesting. ", "What makes you say that? ", "Tell me more about it. ", "What the hell! ", "How do you feel about that? ", "How dare you say that! ", "So...", "Hahahah! "]
    return random.choice(answers)

# 6. creates a set of random topics for the chatbot to ask about.
def random_question():
    questions = ["What's your favourite film? ", "Do you believe that aliens exist? ", "What makes you tick? "]
    res = input(random.choice(questions))
    return res

# . function to print a message when the user input is invalid.
def print_message():
    print("Sorry, I don't understand. Can you rephrase that?")

# CALL THE CHATBOT
chatbot()