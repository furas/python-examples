#!/usr/bin/enc python3

# date: 2019.10.14
# https://stackoverflow.com/questions/58379009/linking-a-command-to-a-chat-using-nltk

import nltk
from nltk.chat.util import Chat, reflections
import re
import random
import webbrowser

class MyChat(Chat):
    
    def __init__(self, pairs, reflections={}):
        """
        Initialize the chatbot.  Pairs is a list of patterns and responses.  Each
        pattern is a regular expression matching the user's statement or question,
        e.g. r'I like (.*)'.  For each such pattern a list of possible responses
        is given, e.g. ['Why do you like %1', 'Did you ever dislike %1'].  Material
        which is matched by parenthesized sections of the patterns (e.g. .*) is mapped to
        the numbered positions in the responses, e.g. %1.

        :type pairs: list of tuple
        :param pairs: The patterns and responses
        :type reflections: dict
        :param reflections: A mapping between first and second person expressions
        :rtype: None
        """
        # add `z` because now items in pairs have three elements
        self._pairs = [(re.compile(x, re.IGNORECASE), y, z) for (x, y, z) in pairs]
        self._reflections = reflections
        self._regex = self._compile_reflections()
        
    def respond(self, str):
        """
        Generate a response to the user input.

        :type str: str
        :param str: The string to be mapped
        :rtype: str
        """

        # check each pattern
        # add `callback` because now items in pairs have three elements
        for (pattern, response, callback) in self._pairs:
            match = pattern.match(str)
            # did the pattern match?
            if match:

                resp = random.choice(response)  # pick a random response
                resp = self._wildcards(resp, match)  # process wildcards

                # fix munged punctuation at the end
                if resp[-2:] == '?.':
                    resp = resp[:-2] + '.'
                if resp[-2:] == '??':
                    resp = resp[:-2] + '?'
                  
                # run `callback` if exists  
                if callback: # if callable(callback):
                    callback(match)
                    
                return resp

# create function before `pairs`
#def open_google(match):
#    webbrowser.open('https://google.com')

def open_something(match):
    #webbrowser.open('https://google.com')
    groups = match.groups()
    if groups:
        if groups[0] == 'google':
            webbrowser.open('https://google.com')
        elif groups[0] == 'so':
            webbrowser.open('https://stackoverflow.com')
        else:
            print('What is "{}"?'.format(groups[0]))
    else:
        print("I don't know what to open")
                   
# every question need `callback` or `None`
            
pairs = [
    ["Hi im (.*)", ["hello %1, What can I do for you?"], None],
#    ["Open google", ["opening www.google.com"], open_google],
    ["Open (.*)", ["opening something ..."], open_something],
]

print("Greetings! My name is Chatbot-T1, What is yours?.")
Chatbot = MyChat(pairs, reflections)
Chatbot.converse()
