## Python Chatbots 

This is a collection of programs that get user input and respond to the user based on that input. Incidentally, one of the main learning points for me was the use of recursion.

---

## Setup
* Python 3
* __random__ package

---

__coffee_shop.py__
This program is adapted from a (Codecademy)[https://www.codecademy.com] lesson. It runs on the command line. The user is asked a series of free-text and multiple-choice questions, in order to process a coffee order.

Ideas for extensions:
* have milk questions for every type of drink.
* have a function that uses random, maybe something like "Ooops! We're out of that" or "You've won a freebie"
* have a loyalty card - could the app remember multiple visits by the same person?
* change the print statement so that it's more like Starbucks. Maybe have a timer that waits until your coffee is ready - (indicated on screen by " . . . " or "waiting..." - then says "That's a large skinny latte for Chris".

---

__ai.py__
This is a chatbot that has a short conversation with the user. The format of the conversation is:
1. Chatbot introduces itself and asks the user's name.
2. Chatbot asks the user how they are feeling.
3. The chatbot responds to the user, then asks a further question. If the user gave a positive response for step 2, the question is a random question. If the user gave a negative response, the chatbot asks what is wrong.
4. The chatbot gives a random response to the user's response. 