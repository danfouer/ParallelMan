# 用自己的微信聊天数据，去训练自己的平行人

# ParallelMan平行人

“以后不但物理世界有一个你，在虚拟的网络世界里还有多个平行的“你”，时时刻刻伴你生活、学习、工作……，这个虚拟的你可以在许多方面督促、帮助、指引物理空间中的你，与你一起成长、变化，协助你解决各种问题。未来的世界，一定是真人与虚人一体化的平行人”

“将来，一定是真人与虚人一体化的平行人：平行人=人+i人，平行物=物+i物，开始是虚实的一对一，然后是一对多，多对一，最后是多对多，形成虚实互动、互生、互存的平行社会。”

”虚实二象性，整个人类文明就是这样来的。理性是有限的，智力必然也是有限的。人类的智力一定要通过平行的虚拟系统来扩展。平行智能就是再回到Memex的想法，就是建设一大批X 5.0智能系统，扩展人类智能。“

”不久的将来，一个个体的实力，很大程度上可能并不取决于物理本身，而取决于与其伴生的软件定义的人工映像。
“
“将来就是一个可编程的世界，软件定义一切。未来的企业要看有多深的知识就有多大的实力，软的就是实的，是铁打的营盘，我们这些物理的都是流水的兵。所以以后你的智力有多深不是你有多聪明，而是软件定义的你有多聪明。你从小生下来就要买各种各样的软件机器人，帮你记事，帮你做各种各样的工作，从你一生下来就把你该记的东西都记下来，跟你一起生活、一起学习、一起工作，你将来不是单纯的你，你有一个属于自己的庞大的组织、庞大的王国，你是你那个王国的King、Emperor，我们就是要靠它们来弥补我们智力上的不对称。”

在第一世界，出生在贵族皇家你才能享受，现在我们每一个人比两百年前两千年前皇帝过得都好，即血缘的不对称被弥补了。现在物联网、计算机兴起，将弥补我们信息上的不对称。下一个不对称是智力的不对称，智能就是弥补我们的智力不对称。所以我还是那句话，人工能有多广，智能才有多深。”

“什么是平行人——开始是一个宠物，慢慢是你的助手，然后是你的自传，最后是你灵魂。对于你爱的人，想说的都在平行机器人的答案中。你可以不断完善自己的平行机器人，最终使它拥有和你一样的价值观，从而将你对这个世界的看法记录和保存下来。”

“平行人的特点——人机一体，软硬兼施，上下一致，人在回路中。”

“要再细分市场，平行人是可以人在回路中的，只要比原来完全靠人厉害，就会有市场。”

“在平行人的实践中，技术不起决定作用，基于技术之上对行业细节的深刻理解才是平行人核心价值所在，也是其可以向平台演化的基石。”

“星星之火，可以燎原，当一个行业有很多个平行人崛起时，将构建一个充满多样性的智慧森林。而这个森林，整体是一个大脑，也就是上面所说的平台。”

“平行人的第二种诠释——人类和机器正处于一个互补的阶段，他们都有一些不同于对方的卓越的才能。这表明人类能够专注于他们独有的技能同时还可以享受锻炼的乐趣，而机器专注于处理大多数那些不需要人类的判断力，创造力和同情心等能力就能完成的常规任务。”

“现在回头再看MOOC，无论是Coursera也好，可汗学堂也好， 就犹如当年项羽看始皇出巡——彼可取而代之。我相信，在现代人工智能和移动互联网技术的帮助下，成千上万优秀的教师都将成为独立地提供知识系统服务的平行人——人机一体，上下一致，人在回路中——从而成为去中心化的超级个体。”

“无孔不入，无所不知，无坚不摧，有所为而有所不为，这就是平行人的未来！”

# 安装 Anaconda Python 3.6 version: https://www.anaconda.com/download/

# 安装 itchat:https://github.com/littlecodersh/ItChat
pip install itchat

# 安装 ChatterBot:https://github.com/gunthercox/ChatterBot
pip install chatterbot

# 注意事项
1. Run Jupyter Notebook from Anaconda
2. Changing BotName="肖恩" to your wechat name
3. 用CRTL-C退出

# 建立自己的训练库:https://github.com/gunthercox/chatterbot-corpus
Chatterbot is a very flexible and dynamic chatbot that you easily can create your own training data and structure.

Create or copy an existing .yml file and put that file in a existing or a new directory you created under `\Anaconda3\Lib\site-packages\chatterbot_corpus\data\chinese\*.yml` and `\Anaconda3\Lib\site-packages\chatterbot_corpus\data\english\*.yml`
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

