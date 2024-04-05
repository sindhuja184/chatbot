#import the required libraries
import numpy as np
import nltk
import string
import random

#importing and reading corpus
f = open('chatbot.txt', 'r', errors = 'ignore')
raw_doc = f.read()
raw_doc = raw_doc.lower()
nltk.download('punkt')
nltk.download('wordnet')
sent_tokens = nltk.sent_tokenize(raw_doc)
word_tokens = nltk.word_tokenize(raw_doc)

#Text preprocessing
lemmer = nltk.stem.WordNetLemmatizer()

#wordnet is semantically orienteddictionary of English included in NLTK
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

remove_punc_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punc_dict)))



#Defining greet function 
greet_inputs = ('hello', 'hi', 'greetings', 'sup', "what's up" , 'hey',)
greet_responses = ['hi', 'hey', 'hi there', 'hello', 'I am glad! You are talking to me']

def greet(sentence):
    for word in sentence.split():
        if word.lower() in greet_inputs:
            return random.choice(greet_responses)
 
    
#Response Generstion 
from sklearn.feature_extraction.text import TfidfVectorizer
#Term Frequency and inverse document frequency -- TfidfVectorizer
#how rare the word occurs 
from sklearn.metrics.pairwise import cosine_similarity
#once we have bags of words and gives us normalized output
def response(user_response):
    chat_res = ''
    #sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens) 
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if req_tfidf == 0:
        chat_res = chat_res + "I am sorry I could not understand you"  
        return chat_res
    else:
        chat_res = chat_res + sent_tokens[idx]
        return chat_res

#Defining Conversation
flag = True
print("Bot: I am Chatbot. Lets have a conversation! ALso if you want to exit at any time type 'bye':")
while flag:
    user_response = input().lower()
    
    if user_response == 'bye':
        flag = False
        print("Bot: Goodbye!")
    elif user_response in ['thanks', 'thank you']:
        flag = False
        print("Bot: You're welcome!")
    else:
        if greet(user_response) is not None:
            print("Bot: " + greet(user_response))
        else:
            sent_tokens.append(user_response)
            word_tokens += nltk.word_tokenize(user_response)
            final_words = list(set(word_tokens))
            print("Bot:", end=" ")
            print(response(user_response))
