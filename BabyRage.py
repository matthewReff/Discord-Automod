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
    pass

Client = discord.Client() #often called bot in api and examples
client = commands.Bot(command_prefix = '$') #used when referencing discord.Client commands in api
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
    await client.say(makeBottyString("Pong!"))
    
client.run("") #client botToken
