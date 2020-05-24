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


def isNumber(arg):
    try:
        res = float(arg)
        return res if res < 10.0 else 0.0
    except ValueError:
        return False

def key_push(msg, button):
    formattedMsg = msg.split('_')[1]
    s_time = float(formattedMsg) if isNumber(formattedMsg) else SLEEP_TIME
    pyautogui.keyDown(button)
    time.sleep(s_time)
    pyautogui.keyUp(button)

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.channel_id = os.getenv('DISCORD_CHANNEL_ID')
        self.auto_mode_flag = False
        self.group = {}

    @commands.command()
    async def grouplist(self, ctx):
        if ctx.channel.id != int(self.channel_id):
            return
        list1 = ""
        list2 = ""
        for key in self.group:
            list1 += str(key) + " " if self.group[key] == 0 else ""
            list2 += str(key) + " " if self.group[key] == 1 else ""
        embed = discord.Embed(title="TEAM LIST")
        embed.add_field(name="1P", value=list1)
        embed.add_field(name="2P", value=list2)
        await ctx.send(embed = embed)

    @commands.command()
    async def set(self, ctx):
        if self.auto_mode_flag:
            self.auto_mode_flag = False
        else:
            self.auto_mode_flag = True

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        if message.channel.id != int(self.channel_id):
            return
        if message.content == 'join1':
            self.group[message.author.name] = 0
            message.send(message.author.name + ' joined 1P')
        elif message.content == 'join2':
            self.group[message.author.name] = 1
            message.send(message.author.name + ' joined 2P.')

        if message.author.name in self.group and message.content.startwith('u'):
            threading.Thread(
                target=key_push,
                args=(message.content, UP_BUTTON[self.group[message.author.name]],
            )).start()
        elif message.author.name in self.group and message.content.startwith('d'):
            threading.Thread(
                target=key_push,
                args=(message.content, DOWN_BUTTON[self.group[message.author.name]],
            )).start()
        elif message.author.name in self.group and message.content.startwith('l'):
            threading.Thread(
                target=key_push,
                args=(message.content, LEFT_BUTTON[self.group[message.author.name]],
            )).start()
        elif message.author.name in self.group and message.content.startwith('r'):
            threading.Thread(
                target=key_push,
                args=(message.content, RIGHT_BUTTON[self.group[message.author.name]],
            )).start()

        elif message.author.name in self.group and message.content.startwith('a'):
            threading.Thread(
                target=key_push,
                args=(message.content, A_BUTTON[self.group[message.author.name]],
            )).start()
        elif message.author.name in self.group and message.content.startwith('b'):
            threading.Thread(
                target=key_push,
                args=(message.content, B_BUTTON[self.group[message.author.name]],
            )).start()
        elif message.author.name in self.group and message.content.startwith('x'):
            threading.Thread(
                target=key_push,
                args=(message.content, X_BUTTON[self.group[message.author.name]],
            )).start()
        elif message.author.name in self.group and message.content.startwith('y'):
            threading.Thread(
                target=key_push,
                args=(message.content, Y_BUTTON[self.group[message.author.name]],
            )).start()
        elif message.author.name in self.group and message.content.startwith('L'):
            threading.Thread(
                target=key_push,
                args=(message.content, L_BUTTON[self.group[message.author.name]],
            )).start()
        elif message.author.name in self.group and message.content.startwith('R'):
            threading.Thread(
                target=key_push,
                args=(message.content, R_BUTTON[self.group[message.author.name]],
            )).start()

        elif message.author.name in self.group and message.content.startwith('start'):
            threading.Thread(
                target=key_push,
                args=(message.content, START_BUTTON[self.group[message.author.name]],
            )).start()
        elif message.author.name in self.group and message.content.startwith('select'):
            threading.Thread(
                target=key_push,
                args=(message.content, SELECT_BUTTON[self.group[message.author.name]],
            )).start()

    @commands.Cog.listener()
    async def on_ready(self):
        print('Connected to Discord.')


def setup(bot):
    bot.add_cog(Commands(bot))
