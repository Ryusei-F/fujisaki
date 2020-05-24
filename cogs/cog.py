#-*- coding: utf-8 -*-
import discord
import os
import time
import pyautogui
import re
import threading

from discord.ext import commands

# class, メンバにdefaultSEC, 詰めて書いて同時押し, spaceで連続押下, 1p2pオブジェクト, ボタン連打

# Input Config
UP_BUTTON= ['up', 'i']
LEFT_BUTTON= ['left', 'j']
DOWN_BUTTON= ['down', 'k']
RIGHT_BUTTON= ['right', 'l']
B_BUTTON= ['c', 'g']
A_BUTTON= ['v', 'h']
Y_BUTTON= ['x', 'f']
X_BUTTON= ['d', 't']
START_BUTTON= ['space', 'p']
SELECT_BUTTON= ['enter', 'o']
L_BUTTON= ['a', 'y']
R_BUTTON= ['r', 'u']
SLEEP_TIME=0.0

def toNumber(arg, sleep_time):
    try:
        res = float(arg)
        return res if res < 10.0 else sleep_time
    except ValueError:
        return sleep_time

def key_push(msg, button, sleep_time):
    formattedMsg = (msg + '_' + sleep_time).split('_')[1]
    s_time = toNumber(formattedMsg, sleep_time)
    pyautogui.keyDown(button)
    time.sleep(s_time)
    pyautogui.keyUp(button)

def test(msg):
    print(msg)

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.channel_id = os.getenv('DISCORD_CHANNEL_ID')
        self.auto_mode_flag = False
        self.group = {}
        self.sleep_time = SLEEP_TIME

    @commands.command()
    async def team(self, ctx):
        if ctx.channel.id != int(self.channel_id):
            return
        list1 = ""
        list2 = ""
        for key in self.group:
            list1 += str(key) + "\n" if self.group[key] == 0 else ""
            list2 += str(key) + "\n" if self.group[key] == 1 else ""
        embed = discord.Embed(title="TEAM LIST")
        embed.add_field(name="1P", value=list1 if list1 else ':heart:')
        embed.add_field(name="2P", value=list2 if list2 else ':blue_heart:')
        await ctx.send(embed = embed)

    @commands.command()
    async def setsec(self, ctx):
        if (ctx.channel.id == int(self.channel_id)):
            msg = ctx.message.content + ' ' + str(self.sleep_time)
            self.sleep_time=toNumber(msg.split(' ')[1], self.sleep_time)
            await ctx.send("スリープタイムを" + str(self.sleep_time) + "秒に設定したよ :heart:")

    @commands.command()
    async def join1(self, ctx):
        if (ctx.channel.id == int(self.channel_id)):
            self.group[ctx.author.name] = 0
            await ctx.send(str(ctx.author.name) + 'くんが1Pになったよ :heart:')
    
    @commands.command()
    async def join2(self, ctx):
        if (ctx.channel.id == int(self.channel_id)):
            self.group[ctx.author.name] = 1
            await ctx.send(str(ctx.author.name) + 'くんが2Pになったよ :blue_heart:')

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        if message.channel.id != int(self.channel_id):
            return

        if message.content == "thread":
            t = threading.Thread(target=test, args=('thread test', ))
            t.start()
            await message.channel.send(toNumber("10", self.sleep_time))

        if message.author.name in self.group and message.content.startswith('u'):
            await message.channel.send('u press')
            await message.channel.send(UP_BUTTON[self.group[message.author.name]])
            await message.channel.send(str(self.sleep_time))

            threading.Thread(
                target=key_push,
                args=(message.content, UP_BUTTON[self.group[message.author.name]],self.sleep_time,
            )).start()
        elif message.author.name in self.group and message.content.startswith('d'):
            threading.Thread(
                target=key_push,
                args=(message.content, DOWN_BUTTON[self.group[message.author.name]],self.sleep_time,
            )).start()
        elif message.author.name in self.group and message.content.startswith('l'):
            threading.Thread(
                target=key_push,
                args=(message.content, LEFT_BUTTON[self.group[message.author.name]],self.sleep_time,
            )).start()
        elif message.author.name in self.group and message.content.startswith('r'):
            threading.Thread(
                target=key_push,
                args=(message.content, RIGHT_BUTTON[self.group[message.author.name]],self.sleep_time,
            )).start()

        elif message.author.name in self.group and message.content.startswith('a'):
            threading.Thread(
                target=key_push,
                args=(message.content, A_BUTTON[self.group[message.author.name]],self.sleep_time,
            )).start()
        elif message.author.name in self.group and message.content.startswith('b'):
            threading.Thread(
                target=key_push,
                args=(message.content, B_BUTTON[self.group[message.author.name]],self.sleep_time,
            )).start()
        elif message.author.name in self.group and message.content.startswith('x'):
            threading.Thread(
                target=key_push,
                args=(message.content, X_BUTTON[self.group[message.author.name]],self.sleep_time,
            )).start()
        elif message.author.name in self.group and message.content.startswith('y'):
            threading.Thread(
                target=key_push,
                args=(message.content, Y_BUTTON[self.group[message.author.name]],self.sleep_time,
            )).start()
        elif message.author.name in self.group and message.content.startswith('L'):
            threading.Thread(
                target=key_push,
                args=(message.content, L_BUTTON[self.group[message.author.name]],self.sleep_time,
            )).start()
        elif message.author.name in self.group and message.content.startswith('R'):
            threading.Thread(
                target=key_push,
                args=(message.content, R_BUTTON[self.group[message.author.name]],self.sleep_time,
            )).start()

        elif message.author.name in self.group and message.content == 'start':
            threading.Thread(
                target=key_push,
                args=(message.content, START_BUTTON[self.group[message.author.name]],self.sleep_time,
            )).start()
        elif message.author.name in self.group and message.content == 'select':
            threading.Thread(
                target=key_push,
                args=(message.content, SELECT_BUTTON[self.group[message.author.name]],self.sleep_time,
            )).start()

    @commands.Cog.listener()
    async def on_ready(self):
        print('Connected to Discord.')


def setup(bot):
    bot.add_cog(Commands(bot))
