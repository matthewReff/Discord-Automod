import asyncio #REMEBER THAT MOST THINGS MUST BE SPECIFIED AS ASYNCRONOUS TO WORK PROPERLY
import discord
import logging
import random
import time
import os
import time
import math
from discord import opus
from discord.ext.commands import Bot
from discord.ext import commands

currentFileName = os.path.split(os.path.abspath(__file__))[0]
botTextsDir = os.path.join(currentFileName,'bot texts')
#generates seed for random by smashing together hours/minutes/seconds of the current time
random.seed(int(str(time.localtime()[3]) + str(time.localtime()[4]) + str(time.localtime()[5])))
      
    
#loads in all elements from config txt file,
def setConfig():
    settings=[]
    settingsDesc=[]
    with open(os.path.join(botTextsDir,'config.txt'),'r') as config: #open config.txt as config, in read mode
        for line in config:
            try:
                splitLine = line.split(':')
                settingName = splitLine[0]
                settingValue = splitLine[1].strip()
                settingsDesc.append(settingName)
                settings.append(settingValue)
            except(IndexError):
                continue
                
    botPrefix = settings[0]
    botToken = str(settings[1])
    
    if botToken == "''":
        print('\n\nPut your bot token into the config before running your bot, or else it will give scary errors.\n\n')
        time.sleep(3)
        exit()
    print('Loaded the following settings from config: ')
    for i in range(0,len(settings)-1):
        print(settingsDesc[i] + ':\n' + settings[i])
    print("")
    return botPrefix, botToken

botPrefix, botToken = setConfig()
Client = discord.Client() #often called bot in api and examples
client = commands.Bot(command_prefix = botPrefix) #used when referencing discord.Client commands in api
logging.basicConfig(level = logging.INFO)


#passes a dict and a filename, to save the dict to the file
def dictWrite(setdict,filename):
    with open(os.path.join(botTextsDir,filename + '.txt'),'w') as setTxt:
        setTxt.write(str(setdict))


#opens up a txt file in read mode, name prodivded in args        
def dictRead(filename):
    setList = []
    setdict = dict() 
    
    with open(os.path.join(botTextsDir,filename + '.txt'),'r') as setTxt: #read in banktxt to banklist
        for line in setTxt:
            try:
                setList.append(eval(line))
            except (NameError,KeyError):
                pass
                
    for i in range(0,len(setList)): #convert banklist into bankDict
        setdict.update(setList[i])
    return setdict 

    
#displays message when bot becomes usable
@client.event
async def on_ready():  
    print('Bot ID: ' + str(client.user.id))
    print("Bot Online!")
    


@client.command(pass_context = True)
async def ping():
    '''
    Used to test if bot is responding
    '''
    await client.say("Pong!")
    
@client.event            
async def on_message(message): 
        #print(message.content)
        swears = ["potato", "tomato"]
        for word in swears:
            if word in message.content:
                await client.delete_message(message)
                censoredWord = ""
                censoredWord += word[0]
                for i in range(1, len(word)):
                    censoredWord += "-"
                print(censoredWord)
                print(word) 
                await client.send_message(message.author, (censoredWord + " is a banned word on this server, any messages that contain it will be removed."))
            
client.run(botToken) #client botToken
