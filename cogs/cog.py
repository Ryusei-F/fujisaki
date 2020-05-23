#-*- coding: utf-8 -*-
import discord
import os
import time
import pyautogui
import re

from discord.ext import commands

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
INTERVAL=float(0.1)
SLEEP_TIME=0.1


def isNumber(arg):
    try:
        float(arg)
        return True
    except ValueError:
        return False

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

    #@commands.command()
    #async def automode(self):
    #    if self.auto_mode_flag:
    #        self.automode(self)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        if message.channel.id != int(self.channel_id):
            return

        if message.content == 'w' or re.match(r'w_.*', message.content) != None:
            formattedMsg = message.content.replace('w_', '')
            s_time = float(formattedMsg) if isNumber(formattedMsg) else SLEEP_TIME
            pyautogui.keyDown(UP_BUTTON)
            time.sleep(s_time)
            pyautogui.keyUp(UP_BUTTON)
        elif message.content == 's' or re.match(r's_.*', message.content) != None:
            formattedMsg = message.content.replace('s_', '')
            s_time = float(formattedMsg) if isNumber(formattedMsg) else SLEEP_TIME
            pyautogui.keyDown(DOWN_BUTTON)
            time.sleep(s_time)
            pyautogui.keyUp(DOWN_BUTTON)
        elif message.content == 'd' or re.match(r'd_.*', message.content) != None:
            formattedMsg = message.content.replace('d_', '')
            s_time = float(formattedMsg) if isNumber(formattedMsg) else SLEEP_TIME
            pyautogui.keyDown(RIGHT_BUTTON)
            time.sleep(s_time)
            pyautogui.keyUp(RIGHT_BUTTON)
        elif message.content == 'a' or re.match(r'a_.*', message.content) != None:
            formattedMsg = message.content.replace('a_', '')
            s_time = float(formattedMsg) if isNumber(formattedMsg) else SLEEP_TIME
            pyautogui.keyDown(LEFT_BUTTON)
            time.sleep(s_time)
            pyautogui.keyUp(LEFT_BUTTON)

        elif message.content == 'a' or re.match(r'a_.*', message.content) != None:
            formattedMsg = message.content.replace('a_', '')
            s_time = float(formattedMsg) if isNumber(formattedMsg) else SLEEP_TIME
            pyautogui.keyDown(A_BUTTON)
            time.sleep(s_time)
            pyautogui.keyUp(A_BUTTON)
        elif message.content == 'b' or re.match(r'b_.*', message.content) != None:
            formattedMsg = message.content.replace('b_', '')
            s_time = float(formattedMsg) if isNumber(formattedMsg) else SLEEP_TIME
            pyautogui.keyDown(B_BUTTON)
            time.sleep(s_time)
            pyautogui.keyUp(B_BUTTON)
        elif message.content == 'x' or re.match(r'x_.*', message.content) != None:
            formattedMsg = message.content.replace('x_', '')
            s_time = float(formattedMsg) if isNumber(formattedMsg) else SLEEP_TIME
            pyautogui.keyDown(X_BUTTON)
            time.sleep(s_time)
            pyautogui.keyUp(X_BUTTON)
        elif message.content == 'y' or re.match(r'y_.*', message.content) != None:
            formattedMsg = message.content.replace('y_', '')
            s_time = float(formattedMsg) if isNumber(formattedMsg) else SLEEP_TIME
            pyautogui.keyDown(Y_BUTTON)
            time.sleep(s_time)
            pyautogui.keyUp(Y_BUTTON)

        elif message.content == 'l' or re.match(r'l_.*', message.content) != None:
            formattedMsg = message.content.replace('l_', '')
            s_time = float(formattedMsg) if isNumber(formattedMsg) else SLEEP_TIME
            pyautogui.keyDown(L_BUTTON)
            time.sleep(s_time)
            pyautogui.keyUp(L_BUTTON)
            
        elif message.content == 'r' or re.match(r'r_.*', message.content) != None:
            formattedMsg = message.content.replace('r_', '')
            s_time = float(formattedMsg) if isNumber(formattedMsg) else SLEEP_TIME
            pyautogui.keyDown(R_BUTTON)
            time.sleep(s_time)
            pyautogui.keyUp(R_BUTTON)

        elif message.content == 'start' or re.match(r'start_.*', message.content) != None:
            formattedMsg = message.content.replace('start_', '')
            s_time = float(formattedMsg) if isNumber(formattedMsg) else SLEEP_TIME
            pyautogui.keyDown(START_BUTTON)
            time.sleep(s_time)
            pyautogui.keyUp(START_BUTTON)
        elif message.content == 'select' or re.match(r'select_.*', message.content) != None:
            formattedMsg = message.content.replace('select_', '')
            s_time = float(formattedMsg) if isNumber(formattedMsg) else SLEEP_TIME
            pyautogui.keyDown(SELECT_BUTTON)
            time.sleep(s_time)
            pyautogui.keyUp(SELECT_BUTTON)

        
    @commands.Cog.listener()
    async def on_ready(self):
        print('Connected to Discord.')


def setup(bot):
    bot.add_cog(Commands(bot))
