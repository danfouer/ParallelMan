# ParallelMan
At the beginning, a ParallelMan is you pet. Then with it growing up, it will be your assistant. When you get older, it will become your autobiography. At the end of your life, it will become you soul, a soul will never disappear
# installing Anaconda Python 3.6 version: https://www.anaconda.com/download/

# installing itchat:https://github.com/littlecodersh/ItChat
pip install itchat

# installing ChatterBot:https://github.com/gunthercox/ChatterBot
pip install chatterbot

# Create your own Corpus Training data:https://github.com/gunthercox/chatterbot-corpus
Chatterbot is a very flexible and dynamic chatbot that you easily can create your own training data and structure.

Create or copy an existing .yml file and put that file in a existing or a new directory you created under `\Anaconda3\Lib\site-packages\chatterbot_corpus\data\chinese\children.yml`
Edit that file with any text editor that you like to work with.

In the beginning of the file you set one or two categories.
```
categories:
- children
conversations:
- - 你是谁？
  - 我是一名资深的青少年心理顾问，专门解答青少年遇到的各种困惑。
- - 你什么时候在线？
  - 24小时随时在线。
- - 你会解答哪些问题？
  - 有关青少年家庭、学校、自我、朋友、健康、娱乐、性、道德、爱情等方面的问题
- - 你还会什么？
............
# Notice
Changing BotName="肖恩" to your wechat name
