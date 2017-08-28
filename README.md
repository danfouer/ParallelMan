# ParallelMan
At the beginning, a ParallelMan is you pet. Then with it growing up, it will be your assistant. When you get older, it will become your autobiography. At the end of your life, it will become you soul, a soul will never disappear
# installing itchat:https://github.com/littlecodersh/ItChat
pip install itchat

# installing ChatterBot:https://github.com/gunthercox/ChatterBot
pip install chatterbot

# Create your own Corpus Training data:https://github.com/gunthercox/chatterbot-corpus
Chatterbot is a very flexible and dynamic chatbot that you easily can create your own training data and structure.

Create or copy an existing .yml file and put that file in a existing or a new directory you created under `chatterbot_corpus\data\<NEW DIRECTORY>`
Edit that file with any text editor that you like to work with.

In the beginning of the file you set one or two categories.
```
categories:
- myown
- my own categories
````

Then can you start your actual training conversation data.

```
conversations:
- - Hello
  - Hello
- - Hi
  - Hello
```
