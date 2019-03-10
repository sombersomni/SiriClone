# SiriClone
A terminal based program that allows you to ask the computer a question and it will generate an answer by scraping google. 

## Prerequistes 
Currently only works on Windows as the text to speech interpreter is handled by ptts. 
You will need to install it on your machine for this program to work properly.

You can downlaod here [http://jampal.sourceforge.net/ptts.html](https://www.google.com)

**if you want to use a different speech interpreter, go into the say.py file and replace the command variable with the one you're using**

You will also need to do a pip install for the following modules

..*speechrecognition
..*pyaudio
..*selenium
..*beautifulsoup4

### Commands
###### To Exit
"no", "dont", "don't", "negative", "stop", "nope", "cancel", "end", "exit"

###### To ask a question
Ex: Siri, what is Battlefield Earth? 
> Question must always begin with Siri
