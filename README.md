Hello Everyone, 

In this repository I have created a simple chat bot which is capable of taking the input from the user and giving the related output to the user.

INTRODUCTION:
	This chatbot takes the input from the user ad returns the output. I have giving the data science wikipedia page as the input to the chatbot. This basic chat bot returns the related sentence from the input

FEATURES:
	This intracts effectively eith the users
DEPENDENCIES:
	This chatbot uses librsries like NumPy, String, Random, NLTK(Natural Language ToolKit)
WORKING:
	1. Importing Libraries: The code starts by importing the neccesary libraries like Nu	Numpy, String, Random, NLTK(Natural Language Toolkit)
	2. Reading Corpuses: It reads the contents of "chatbot.txt",which contains the 	content of "data science" wikipedia page
	3. Tokenization: The text is tokenised into sentences and words (sent_tokens, 	word_tokens) using nltk functions sent_tokenize and word_tokenize
	4. Preprocessing :The LemTokens and LemNormalize functions are defined for lemmatization and normalization of text. The remove_punc_dict is a dictionary used to remove punctuation from text.
	5.Greet Function: Generate random greetings if the user imput matches predefined greetings
	6. Response Generation: This genertes a response based on user input. It uses TF IDF to calculate similarity betweeb the user input and sentences in corpus, and returns most similar sentence
	7. Conversation Loop: This is the main connversation with the bot. This continually yakes the user input, processes and generstes a respomnses until user types 'bye'
    Now, let's go through the conversation loop:
    ->The loop continuously takes user input using the input() function.
    ->If the user input is "bye", the bot responds with "Goodbye!" and breaks out of the loop.
    ->If the user input is "thanks" or "thank you", the bot responds with "You're welcome!" and breaks out of the loop.
    ->If the user input matches a predefined greeting, the bot responds with a random greeting from the list.
    ->If none of the above conditions are met, the bot processes the user input and generates a response using the response function.


