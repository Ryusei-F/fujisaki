#-*- coding: utf-8 -*-
import discord
import os
import time
import pyautogui
import re
import threading

from discord.ext import commands
from discord.ext import tasks

# class, メンバにdefaultSEC, 詰めて書いて同時押し, spaceで連続押下, 1p2pオブジェクト, ボタン連打

# Input Config
UP_BUTTON =    ['1', 'e', 'g', 'shiftright']
LEFT_BUTTON =  ['2', 'left', 'h', 'shiftleft']
DOWN_BUTTON =  ['3', 'y', 'j', 'ctrlleft']
RIGHT_BUTTON = ['4', 'y', 'k', 'ctrlright']
B_BUTTON=      ['5', 'u', 'l', 'backspace']
A_BUTTON=      [';', 'i', 'z', 'enter']
Y_BUTTON=      [':', 'o', 'x', 'space']
X_BUTTON=      ['8', 'p', 'c', 'home']
START_BUTTON=  ['9', 'a', 'v', 'pageup']
SELECT_BUTTON= ['0', 's', 'b', 'pagedown']
L_BUTTON=      ['q', 'd', 'n', 'enter']
R_BUTTON=      ['w', 'f', 'm', 'delete']
SLEEP_TIME=0.0
CORRESP_EMU_BUTTON= {'UP_BUTTON': UP_BUTTON, 'LEFT_BUTTON': LEFT_BUTTON, 'DOWN_BUTTON': DOWN_BUTTON, 'RIGHT_BUTTON': RIGHT_BUTTON,
                     'A_BUTTON': A_BUTTON, 'B_BUTTON': B_BUTTON, 'Y_BUTTON': Y_BUTTON, 'X_BUTTON': X_BUTTON,
                     'START_BUTTON': START_BUTTON, 'SELECT_BUTTON': SELECT_BUTTON, 'L_BUTTON': L_BUTTON, 'R_BUTTON': R_BUTTON}
BUTTON_LIST= {'u': 'UP_BUTTON', 'l': 'LEFT_BUTTON', 'd':'DOWN_BUTTON', 'r':'RIGHT_BUTTON',
              'a': 'A_BUTTON', 'b': 'B_BUTTON', 'x': 'X_BUTTON', 'y': 'Y_BUTTON',
              'start': 'START_BUTTON', 'select': 'SELECT', 'L': 'L_BUTTON', 'R': 'R_BUTTON'}

def toNumber(arg, sleep_time):
    try:
        res = float(arg)
        return res if res < 60.0 else sleep_time
    except ValueError:
        return sleep_time

def key_push(msg, button, sleep_time):
    formattedMsg = (msg + '_' + str(sleep_time)).split('_')[1]
    s_time = toNumber(formattedMsg, sleep_time)
    pyautogui.keyDown(button)
    time.sleep(s_time)
    pyautogui.keyUp(button)

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.channel_id = os.getenv('DISCORD_CHANNEL_ID')
        self.auto_mode_flag = False
        self.auto_button = ';'
        self.group = {}
        self.sleep_time = SLEEP_TIME

    @commands.command()
    async def team(self, ctx):
        if ctx.channel.id != int(self.channel_id):
            return
        lst = ["", "", "", ""]
        for key in self.group:
            for i in range(4):
                lst[i] += str(key) + "\n" if self.group[key] == i else ""
        embed = discord.Embed(title="TEAM LIST")
        embed.add_field(name="1P", value=lst[0] if lst[0] else ':heart:')
        embed.add_field(name="2P", value=lst[1] if lst[1] else ':blue_heart:')
        embed.add_field(name='3P', value=lst[2] if lst[2] else ':yellow_heart:')
        embed.add_field(name='4P', value=lst[3] if lst[3] else ':purple_heart:')
        await ctx.send(embed = embed)

    @commands.command()
    async def switchauto(self, ctx):
        if (ctx.channel.id == int(self.channel_id)):
            self.auto_mode_flag = False if self.auto_mode_flag else True

    @commands.command()
    async def autobutton(self, ctx):
        if (ctx.channel.id == int(self.channel_id)) and ctx.author.name in self.group:
            msg = (ctx.message.content + ' a').split(' ')[1]
            if msg in BUTTON_LIST:
                self.auto_button = CORRESP_EMU_BUTTON[BUTTON_LIST[msg]][self.group[ctx.author.name]]
                await ctx.send("オートボタンを" + BUTTON_LIST[msg] + "に設定したよ :heart:")

    @tasks.loop(seconds=0.1)
    async def automode(self):
        if self.auto_mode_flag:
            threading.Thread(
                target=key_push,
                args=('dummy_0', self.auto_button,self.sleep_time,
            )).start()

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

    @commands.command()
    async def join3(self, ctx):
        if (ctx.channel.id == int(self.channel_id)):
            self.group[ctx.author.name] = 2
            await ctx.send(str(ctx.author.name) + 'くんが3Pになったよ :yellow_heart:')
    
    @commands.command()
    async def join4(self, ctx):
        if (ctx.channel.id == int(self.channel_id)):
            self.group[ctx.author.name] = 3
            await ctx.send(str(ctx.author.name) + 'くんが3Pになったよ :perple_heart:')

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        elif message.channel.id != int(self.channel_id):
            return
        elif message.author.name not in self.group:
            self.group[message.author.name] = 0

        if message.content.startswith('w'):
            threading.Thread(
                target=key_push,
                args=(message.content, UP_BUTTON[self.group[message.author.name]],self.sleep_time,
            )).start()
        elif message.content.startswith('s'):
            threading.Thread(
                target=key_push,
                args=(message.content, DOWN_BUTTON[self.group[message.author.name]],self.sleep_time,
            )).start()
        elif message.content.startswith('a'):
            threading.Thread(
                target=key_push,
                args=(message.content, LEFT_BUTTON[self.group[message.author.name]],self.sleep_time,
            )).start()
        elif message.content.startswith('d'):
            threading.Thread(
                target=key_push,
                args=(message.content, RIGHT_BUTTON[self.group[message.author.name]],self.sleep_time,
            )).start()

        elif message.content.startswith('1'):
            threading.Thread(
                target=key_push,
                args=(message.content, A_BUTTON[self.group[message.author.name]],self.sleep_time,
            )).start()
        elif message.content.startswith('2'):
            threading.Thread(
                target=key_push,
                args=(message.content, B_BUTTON[self.group[message.author.name]],self.sleep_time,
            )).start()
        elif message.content.startswith('3'):
            threading.Thread(
                target=key_push,
                args=(message.content, X_BUTTON[self.group[message.author.name]],self.sleep_time,
            )).start()
        elif message.content.startswith('4'):
            threading.Thread(
                target=key_push,
                args=(message.content, Y_BUTTON[self.group[message.author.name]],self.sleep_time,
            )).start()
        elif message.content.startswith('r'):
            threading.Thread(
                target=key_push,
                args=(message.content, L_BUTTON[self.group[message.author.name]],self.sleep_time,
            )).start()
        elif message.content.startswith('l'):
            threading.Thread(
                target=key_push,
                args=(message.content, R_BUTTON[self.group[message.author.name]],self.sleep_time,
            )).start()

        elif message.content == 'start':
            threading.Thread(
                target=key_push,
                args=(message.content, START_BUTTON[self.group[message.author.name]],self.sleep_time,
            )).start()
        elif message.content == 'select':
            threading.Thread(
                target=key_push,
                args=(message.content, SELECT_BUTTON[self.group[message.author.name]],self.sleep_time,
            )).start()
        elif message.content == '236p':
            pidx = self.group[message.author.name]
            pyautogui.keyDown(DOWN_BUTTON[pidx])
            pyautogui.keyDown(RIGHT_BUTTON[pidx])
            pyautogui.keyUp(DOWN_BUTTON[pidx])
            #pyautogui.hotkey(DOWN_BUTTON[pidx], RIGHT_BUTTON[pidx])
            pyautogui.keyDown(Y_BUTTON[pidx])
            pyautogui.keyUp(RIGHT_BUTTON[pidx])
            pyautogui.keyUp(Y_BUTTON[pidx])
        elif message.content ==  '214p':
            pidx = self.group[message.author.name]
            pyautogui.keyDown(DOWN_BUTTON[pidx])
            pyautogui.keyDown(LEFT_BUTTON[pidx])
            pyautogui.keyUp(DOWN_BUTTON[pidx])
            #pyautogui.hotkey(DOWN_BUTTON[pidx], RIGHT_BUTTON[pidx])
            pyautogui.keyDown(Y_BUTTON[pidx])
            pyautogui.keyUp(LEFT_BUTTON[pidx])
            pyautogui.keyUp(Y_BUTTON[pidx])


    @commands.Cog.listener()
    async def on_ready(self):
        print('Connected to Discord.')


def setup(bot):
    bot.add_cog(Commands(bot))
