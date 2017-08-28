
# coding: utf-8

# In[1]:

import itchat
import os, codecs
import datetime
from itchat.content import *
from time import strftime, gmtime
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
BotName="肖恩"
chatbot = ChatBot("BotName")
chatbot.set_trainer(ChatterBotCorpusTrainer)
# 使用中文语料库训练它
chatbot.train("chatterbot.corpus.chinese")


# In[2]:

FILENAME = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M') +".txt"
PATH = "./outputweixin/"
if os.path.exists(PATH)==False:
    os.makedirs(PATH)
fp = codecs.open(PATH + FILENAME, "a", "utf-8")

itchat.auto_login(enableCmdQR = False, hotReload = False)



# In[3]:

@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_send_test(msg):
    res = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+itchat.search_friends(userName =msg['FromUserName'])['NickName'] + "to"+itchat.search_friends(userName =msg['ToUserName'])['NickName']+ ":"+msg['Text']
    fp.write(res + "\n\n")
    print (res) 
    res2 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+itchat.search_friends(userName =msg['ToUserName'])['NickName'] + "to"+itchat.search_friends(userName =msg['FromUserName'])['NickName']+ ":"#+chatbot.get_response(msg['Text'])
    #fp.write(res2 + "\n\n")
    #print (res2) 
    
    if itchat.search_friends(userName =msg['FromUserName'])['NickName']!=BotName:
        res3=chatbot.get_response(msg['Text'])
        print('%s%s'%(res2,res3)) 
        msg.user.send('%s' % (res3))
        fp.write('%s%s\n\n'%(res2,res3))  
        #print('%s%s'%(res2,chatbot.get_response(msg['Text'])))     
        #msg.user.send('%s' % (chatbot.get_response(msg['Text'])))
        #fp.write('%s%s\n\n'%(res2,chatbot.get_response(msg['Text'])))  


# In[4]:

#@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
#def text_reply(msg):
#    msg.user.send('%s: %s' % (msg.type, chatbot.get_response(msg['Text'])))


# In[5]:

@itchat.msg_register(TEXT, isGroupChat = True)
def Gchat(msg) :
    gres = "Group#"+ "/"+ msg['FromUserName']+ "/" +datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+msg['ActualNickName'] + ":" +msg['Text']
    fp.write(gres + "\n\n")
    print (gres)
    if msg.isAt:
        gres2 = "Group#"+ "/"+ msg['FromUserName']+ "/" +datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+BotName+":@"+msg['ActualNickName']
        gres3=chatbot.get_response(msg['Text'])
        msg.user.send(u'@%s\u2005%s' % (
            msg.actualNickName,  gres3))
        print('%s%s'%(gres2,gres3)) 
        fp.write('%s%s\n\n'%(gres2,gres3))     



# In[6]:

#@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
#def download_files(msg):
#    msg.download(msg.fileName)
#    typeSymbol = {
#        PICTURE: 'img',
#        VIDEO: 'vid', }.get(msg.type, 'fil')
#    return '@%s@%s' % (typeSymbol, msg.fileName)


# In[7]:

@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    msg.download("./images/"+msg.fileName)
    itchat.send('@%s@%s' % (
        'img' if msg['Type'] == 'Picture' else 'fil', msg['FileName']),
        msg['FromUserName'])
    return '%s received' % msg['Type']


# In[8]:

@itchat.msg_register(FRIENDS)
def add_friend(msg):
    msg.user.verify()
    msg.user.send('Nice to meet you!')


# In[9]:

if __name__ == "__main__":
    try:
        chatrooms = itchat.get_chatrooms(update=True, contactOnly=True)
        chatroom_ids = [c['UserName'] for c in chatrooms]
        print(chatroom_ids)
        print('正在监测的群聊：', len(chatrooms), '个')
        print(' '.join([item['NickName'] for item in chatrooms]))
        itchat.run()
    except KeyboardInterrupt:
        fp.close()
        itchat.logout()


# In[ ]:



