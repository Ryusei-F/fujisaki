#-*- coding: utf-8 -*-
import discord
import os
import time
import pyautogui

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
SLEEP_TIME=0.5

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

        if message.content == 'up':
            pyautogui.keyDown(UP_BUTTON)
            time.sleep(SLEEP_TIME)
            pyautogui.keyUp(UP_BUTTON)
            #pyautogui.press(UP_BUTTON, presses=1, interval=INTERVAL)
        elif message.content == 'down':
            pyautogui.keyDown(DOWN_BUTTON)
            time.sleep(SLEEP_TIME)
            pyautogui.keyUp(DOWN_BUTTON)
            #pyautogui.press(DOWN_BUTTON, presses=1, interval=INTERVAL)
        elif message.content == 'right':
            pyautogui.keyDown(RIGHT_BUTTON)
            time.sleep(SLEEP_TIME)
            pyautogui.keyUp(RIGHT_BUTTON)
            #pyautogui.press(RIGHT_BUTTON, presses=1, interval=INTERVAL)
        elif message.content == 'left':
            pyautogui.keyDown(LEFT_BUTTON)
            time.sleep(SLEEP_TIME)
            pyautogui.keyUp(LEFT_BUTTON)
            #pyautogui.press(LEFT_BUTTON, presses=1, interval=INTERVAL)

        elif message.content == 'a' or message.content == 'A':
            pyautogui.keyDown(A_BUTTON)
            time.sleep(SLEEP_TIME)
            pyautogui.keyUp(A_BUTTON)
            #pyautogui.press(A_BUTTON, presses=1, interval=INTERVAL)
        elif message.content == 'b' or message.content == 'B':
            pyautogui.keyDown(B_BUTTON)
            time.sleep(SLEEP_TIME)
            pyautogui.keyUp(B_BUTTON)
            #pyautogui.press(B_BUTTON, presses=1, interval=INTERVAL)
        elif message.content == 'x' or message.content == 'X':
            pyautogui.keyDown(X_BUTTON)
            time.sleep(SLEEP_TIME)
            pyautogui.keyUp(X_BUTTON)
            #pyautogui.press(X_BUTTON, presses=1, interval=INTERVAL)
        elif message.content == 'y' or message.content == 'Y':
            pyautogui.keyDown(Y_BUTTON)
            time.sleep(SLEEP_TIME)
            pyautogui.keyUp(Y_BUTTON)
            #pyautogui.press(Y_BUTTON, presses=1, interval=INTERVAL)

        elif message.content == 'l' or message.content == 'L':
            pyautogui.keyDown(L_BUTTON)
            time.sleep(SLEEP_TIME)
            pyautogui.keyUp(L_BUTTON)
            #pyautogui.press(L_BUTTON, presses=1, interval=INTERVAL)
        elif message.content == 'r' or message.content == 'R':
            pyautogui.keyDown(R_BUTTON)
            time.sleep(SLEEP_TIME)
            pyautogui.keyUp(R_BUTTON)
            #pyautogui.press(R_BUTTON, presses=1, interval=INTERVAL)

        elif message.content == 'start':
            pyautogui.keyDown(START_BUTTON)
            time.sleep(SLEEP_TIME)
            pyautogui.keyUp(START_BUTTON)
            #pyautogui.press(START_BUTTON, presses=1, interval=INTERVAL)
        elif message.content == 'select':
            pyautogui.keyDown(SELECT_BUTTON)
            time.sleep(SLEEP_TIME)
            pyautogui.keyUp(SELECT_BUTTON)
            #pyautogui.press(SELECT_BUTTON, presses=1, interval=INTERVAL)


    @commands.Cog.listener()
    async def on_ready(self):
        print('Connected to Discord.')


def setup(bot):
    bot.add_cog(Commands(bot))
