#!/usr/bin/env python
# coding: utf-8

# # 對話機器人
# 建立一個對話機器人, 機器人裡面內建一個資料問答資料庫, 資料庫的問題跟答案如下所示:
# 問題:保險 答案: 以下是我們推薦的險總類
# 問題:貸款 答案: 以下是我們推薦的貸款總類
# 問題:存款 答案: 以下是您的銀行存款餘額
# 當使用者輸入問題時, 只要問題中有部分關鍵字對到問答資料庫的問題,電腦就予以回答
#    

# In[1]:


qa = {'保險':'以下是我們推薦的險總類',
    '貸款':'以下是我們推薦的貸款總類',
    '存款':'以下是您的銀行存款餘額'}

question = input('請輸入您的問題?')
for q in qa:
  if q in question:
    print(qa.get(q))
    break
else:
  print('我現在還不聰明, 等我變聰明以後再回答您')


# ## Third Party Tool
# ### Speech Recognition套件 (語音識別)

# In[17]:


get_ipython().system(' pip install SpeechRecognition')


# In[28]:


import sys
print(sys.version)


# ### PyAudio套件

# In[3]:


get_ipython().system(' pip install pyAudio')


# ### 呼叫speech_recognition套件，從麥克風取得聲音後丟給google去辨識聲音內容

# In[8]:


get_ipython().system(' pip3 install --upgrade speechrecognition')


# In[3]:


import speech_recognition as sr

def listenTo():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)

    ret = r.recognize_google(audio,language = 'zh-TW')
    return ret

ret = listenTo()
print(ret)


# ### text to speech
# ### pyttsx3套件(文字轉語音)

# In[6]:


get_ipython().system('pip install pyttsx3')


# In[8]:


import pyttsx3
def speak(s):
    engine = pyttsx3.init()
    engine.say(s)
    engine.runAndWait()


# In[10]:


qa = {'保險':'以下是我們推薦的險總類',
    '貸款':'以下是我們推薦的貸款總類',
    '存款':'以下是您的銀行存款餘額'}

question = listenTo()
for q in qa:
  if q in question:
    speak(qa.get(q))
    break
else:
  speak('我現在還不聰明, 等我變聰明以後再回答您')


# In[ ]:

# 我某一天加入的新程式碼


