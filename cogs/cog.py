#-*- coding: utf-8 -*-
import discord
import os
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
            pyautogui.typewrite('Hello world!\n', 0.1)
            pyautogui.press(UP_BUTTON, presses=1, interval=INTERVAL)
        elif message.content == 'down':
            pyautogui.press(DOWN_BUTTON, presses=1, interval=INTERVAL)
        elif message.content == 'right':
            pyautogui.press(RIGHT_BUTTON, presses=1, interval=INTERVAL)
        elif message.content == 'left':
            pyautogui.press(LEFT_BUTTON, presses=1, interval=INTERVAL)

        elif message.content == 'a' or 'A':
            pyautogui.press(A_BUTTON, presses=1, interval=INTERVAL)
        elif message.content == 'b' or 'B':
            pyautogui.press(B_BUTTON, presses=1, interval=INTERVAL)
        elif message.content == 'x' or 'X':
            pyautogui.press(X_BUTTON, presses=1, interval=INTERVAL)
        elif message.content == 'y' or 'Y':
            pyautogui.press(Y_BUTTON, presses=1, interval=INTERVAL)

        elif message.content == 'l' or 'L':
            pyautogui.press(L_BUTTON, presses=1, interval=INTERVAL)
        elif message.content == 'r' or 'R':
            pyautogui.press(R_BUTTON, presses=1, interval=INTERVAL)

        elif message.content == 'start':
            pyautogui.press(START_BUTTON, presses=1, interval=INTERVAL)
        elif message.content == 'select':
            pyautogui.press(SELECT_BUTTON, presses=1, interval=INTERVAL)


    @commands.Cog.listener()
    async def on_ready(self):
        print('Connected to Discord.')


def setup(bot):
    bot.add_cog(Commands(bot))
