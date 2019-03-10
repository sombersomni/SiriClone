from say import say
from query import Fetcher
from time import sleep
import subprocess
import sys

class Commander:
    def __init__(self, name):
        self.name = name
        self.cancel = ("no", "dont", "don't", "negative", "stop", "nope", "cancel", "end", "exit")

    def discover(self, text):
        if "what" and "your name" in text:
            if "my" in text:
                self.respond("I don't know. What is your name?")
            else: 
                self.respond("My name is {}. How can I help you?".format(self.name))
        for no in self.cancel:
            if no in text:
                self.respond("Exiting now")
                sys.exit()
        
        if self.name in text:
            search = text.split(" ", 1)[-1]
            search = search.replace(" ", "+")
            fetch = Fetcher("http://www.google.com/search?q="+search)
            sleep(5)
            response = fetch.lookup()
            self.respond(response)
        
    def respond(self, response):
        say(response)

