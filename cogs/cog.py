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
UP_BUTTON='up'
LEFT_BUTTON='left'
DOWN_BUTTON='down'
RIGHT_BUTTON='right'
B_BUTTON='c'
A_BUTTON='v'
Y_BUTTON='x'
X_BUTTON='d'
START_BUTTON='space'
SELECT_BUTTON='enter'
L_BUTTON='a'
R_BUTTON='r'
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

    @commands.command()
    async def aaaa(self, ctx):
        if ctx.channel.id != self.channel_id:
            await ctx.send('command test')

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

        if  message.content.startwith('u'):
            threadA = threading.Thread(target=key_push, args=(message.content, UP_BUTTON,))
            threadA.start()

        elif message.content.startwith('d'):
            threadA = threading.Thread(target=key_push, args=(message.content, DOWN_BUTTON,))
            threadA.start()
        
        elif message.content.startwith('r'):
            threadA = threading.Thread(target=key_push, args=(message.content, RIGHT_BUTTON,))
            threadA.start()

        elif message.content.startwith('l'):
            threadA = threading.Thread(target=key_push, args=(message.content, LEFT_BUTTON,))
            threadA.start()

        elif message.content.startwith('a'):
            threadA = threading.Thread(target=key_push, args=(message.content, A_BUTTON,))
            threadA.start()

        elif message.content.startwith('b'):
            threadA = threading.Thread(target=key_push, args=(message.content, B_BUTTON,))
            threadA.start()

        elif message.content.startwith('x'):
            threadA = threading.Thread(target=key_push, args=(message.content, X_BUTTON,))
            threadA.start()

        elif message.content.startwith('y'):
            threadA = threading.Thread(target=key_push, args=(message.content, Y_BUTTON,))
            threadA.start()

        elif message.content.startwith('L'):
            threadA = threading.Thread(target=key_push, args=(message.content, L_BUTTON,))
            threadA.start()

        elif message.content.startwith('R'):
            threadA = threading.Thread(target=key_push, args=(message.content, R_BUTTON,))
            threadA.start()

        elif message.content.startwith('start'):
            threadA = threading.Thread(target=key_push, args=(message.content, START_BUTTON,))
            threadA.start()

        elif message.content.startwith('select'):
            threadA = threading.Thread(target=key_push, args=(message.content, SELECT_BUTTON,))
            threadA.start()

    @commands.Cog.listener()
    async def on_ready(self):
        print('Connected to Discord.')


def setup(bot):
    bot.add_cog(Commands(bot))
