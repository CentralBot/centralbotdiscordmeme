import os
import discord
from discord import Game
from discord.ext.commands import Bot
from pfaw import Fortnite, Platform, Mode
fortnite = Fortnite(fortnite_token='ZWM2ODRiOGM2ODdmNDc5ZmFkZWEzY2IyYWQ4M2Y1YzY6ZTFmMzFjMjExZjI4NDEzMTg2MjYyZDM3YTEzZmM4NGQ=', launcher_token='MzRhMDJjZjhmNDQxNGUyOWIxNTkyMTg3NmRhMzZmOWE6ZGFhZmJjY2M3Mzc3NDUwMzlkZmZlNTNkOTRmYzc2Y2Y=',
                    password='Ho#F&NXbkQqkt95K5$Rw', email='fortniteapi@protonmail.com') #working 7/10/2018
def subtract(a, b):                              
    return "".join(a.rsplit(b))
oof = subtract('oof', 'o')
import time
import pickle

TOKEN = 'NDY2NDE3MzU3NTkwMzY0MTc3.DibwiA.Ejv3TC-QFZs0yRBzw85sM2H0tt8'
BOT_PREFIX = ("cn!")
client = Bot(command_prefix=BOT_PREFIX)
@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('cn!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith('?help'):
        xmsg = "Dyno Sucks, Use Central Bot instead {0.author.mention}".format(message)
        await client.send_message(message.channel, xmsg)
    
    if message.content.startswith('cn!add') and message.channel.id == '466420629965504512':
        newmessage = (str(message.content)[:-2])
        print(newmessage)
        userid = subtract(newmessage, 'cn!add ')
        print(userid)
        to_subtract = 'cn!add ' + userid + ' '
        pointstoadd = subtract(message.content, to_subtract)
        fileexists = 0
        print(pointstoadd)
        fileuserid = subtract(userid, '<@!')
        realfilename = subtract(fileuserid, '>')
        intofpointstoaddd = int(pointstoadd)
        filename = realfilename + ".txt"
        try:
            file = open(filename, 'r')
            fileexists = 1
        except FileNotFoundError:
                file = open(filename, 'w+')
                file.write('0')
                fileexists = 0
                file.close()
                outfile = open(filename , "wb")
                pointsnowtoadd = str(pointstoadd)
                pickle.dump(pointsnowtoadd, outfile)
                xxxtenationmsg = 'You are adding(' + pointstoadd + ')to : ' + userid
                await client.send_message(message.channel, xxxtenationmsg)
                outfile.close()
                file.close()
        print(filename)
        infile = open(filename,"rb")
        print(infile)
        if fileexists == 1:
            currentpoints = open(filename, "rb")
            oofooe = pickle.load(currentpoints)
            print(oofooe)
            intofnewpoints = int(oofooe)
            print(intofnewpoints)
            strofpointz = int(pointstoadd)
            newpoints = intofnewpoints + strofpointz
            print(newpoints)
            dumpingfinal = open(filename, "wb")
            pickle.dump(newpoints, dumpingfinal)
            dumpingfinal.close()
            xxxtenationmsg = 'You are adding(' + pointstoadd + ')to : ' + userid
            await client.send_message(message.channel, xxxtenationmsg)
            currentpoints.close()
    if message.content.startswith('cn!subtract') and message.channel.id == '466420629965504512':
        await client.send_message(message.channel, "Reminder, This will not work unless you add some points first")
        newmessage = (str(message.content)[:-2])
        print(newmessage)
        userid = subtract(newmessage, 'cn!subtract ')
        print(userid)
        to_subtract = 'cn!subtract ' + userid + ' '
        pointstosub = subtract(message.content, to_subtract)
        fileexists = 0
        print(pointstosub)
        fileuserid = subtract(userid, '<@!')
        realfilename = subtract(fileuserid, '>')
        intofpointstosubbb = int(pointstosub)
        filename = realfilename + ".txt"
        currentpointz = open(filename, "rb")
        raw_points = pickle.load(currentpointz)
        final_points = int(raw_points) - intofpointstosubbb
        print(final_points)
        final_pointz = int(final_points)
        final_resting_place = open(filename, "wb")
        print(final_pointz)
        pickle.dump(final_pointz, final_resting_place)
        final_resting_place.close()
        currentpointz.close()
        submessage = "Completed" 
        await client.send_message(message.channel, submessage)
    if message.content.startswith('cn!check'):
        userid = message.author.id
        filenam = userid + '.txt'
        oofergang = open(filenam, "rb")
        totalpointspls = pickle.load(oofergang)
        msgww = str(totalpointspls)
        msgpls = "You have : " + msgww + " points, {0.author.mention}".format(message)
        await client.send_message(message.channel, msgpls)
        
        
















@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=Game(name="Central Link: discord.gg/YVmjC5c"))
client.run(TOKEN)
