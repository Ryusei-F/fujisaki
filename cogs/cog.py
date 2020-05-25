#-*- coding: utf-8 -*-
import discord
import os
import time
import pyautogui
import re
import threading

from discord.ext import tasks, commands

# class, メンバにdefaultSEC, 詰めて書いて同時押し, spaceで連続押下, 1p2pオブジェクト, ボタン連打

# Input Config
UP_BUTTON =    ['1', 'e', 'g', 'up']
LEFT_BUTTON =  ['2', 'left', 'h', '[']
DOWN_BUTTON =  ['3', 't', 'j', 'down']
RIGHT_BUTTON = ['4', 'y', 'k', 'right']
B_BUTTON=      ['5', 'u', 'l', 'backspace']
A_BUTTON=      [';', 'i', 'z', 'enter']
Y_BUTTON=      [':', 'o', 'x', 'space']
X_BUTTON=      ['8', 'p', 'c', 'home']
START_BUTTON=  ['9', 'a', 'v', 'pageup']
SELECT_BUTTON= ['0', 's', 'b', 'pagedown']
L_BUTTON=      ['q', 'd', 'n', 'enter']
R_BUTTON=      ['w', 'f', 'm', 'delete']
DEFAULT_SLEEP_TIME=0.0
KEYCONF_DICT= {'UP_BUTTON': UP_BUTTON, 'LEFT_BUTTON': LEFT_BUTTON, 'DOWN_BUTTON': DOWN_BUTTON, 'RIGHT_BUTTON': RIGHT_BUTTON,
                     'A_BUTTON': A_BUTTON, 'B_BUTTON': B_BUTTON, 'Y_BUTTON': Y_BUTTON, 'X_BUTTON': X_BUTTON,
                     'START_BUTTON': START_BUTTON, 'SELECT_BUTTON': SELECT_BUTTON, 'L_BUTTON': L_BUTTON, 'R_BUTTON': R_BUTTON}
BUTTON_DICT= {'w': 'UP_BUTTON', 'a': 'LEFT_BUTTON', 's':'DOWN_BUTTON', 'd':'RIGHT_BUTTON',
              'l': 'A_BUTTON', 'k': 'B_BUTTON', 'i': 'X_BUTTON', 'j': 'Y_BUTTON',
              'start': 'START_BUTTON', 'select': 'SELECT_BUTTON', 'u': 'L_BUTTON', 'o': 'R_BUTTON'}
BUTTON_LIST= ['UP_BUTTON', 'LEFT_BUTTON', 'DOWN_BUTTON', 'RIGHT_BUTTON',
              'A_BUTTON', 'B_BUTTON', 'X_BUTTON', 'Y_BUTTON',
              'START_BUTTON', 'SELECT_BUTTON', 'L_BUTTON', 'R_BUTTON']

def toNumber(arg):
    try:
        res = float(arg)
        return res if res <= 30.0 else DEFAULT_SLEEP_TIME
    except ValueError:
        return DEFAULT_SLEEP_TIME

def key_push(msg, button, sleep_time):
    formattedMsg = (msg + '_' + str(sleep_time)).split('_')[1]
    s_time = toNumber(formattedMsg)
    pyautogui.keyDown(button)
    time.sleep(s_time)
    pyautogui.keyUp(button)

# async key_push for array
def key_push_of_array(msg, group_num, sleep_time, keyconf_dict, button_dict):
    keyarray = list(msg.split(' ')[0])
    #print('msg:' + msg + ',group_num:' + str(group_num))
    s_time = toNumber((msg + ' ' + str(sleep_time)).split(' ')[1])
    for key in keyarray:
        if key in button_dict:
            kmap = keyconf_dict[button_dict[key]][group_num]
            pyautogui.keyDown(kmap)
            time.sleep(s_time)
            pyautogui.keyUp(kmap)
            # test
            #print("グループ" + str(group_num) + "が" + kmap + "を" + str(s_time) + "秒間おしたよ")


class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.channel_id = os.getenv('DISCORD_CHANNEL_ID')
        self.auto_mode_flag = False
        self.auto_button = ';'
        self.group = {}
        self.sleep_time = DEFAULT_SLEEP_TIME
        self.button_dict = BUTTON_DICT
        self.keyconf_dict = KEYCONF_DICT
        self.sorted_button_list = BUTTON_LIST
        self.switchauto

    #def cog_unload(self):
    #    self.automode.cancel()

    @commands.command()
    async def team(self, ctx):
        if ctx.channel.id != int(self.channel_id):
            return
        lst = ["", "", "", ""]
        for key in self.group:
            lst[self.group[key]] += str(key) + "\n" 
        embed = discord.Embed(title="TEAM LIST")
        embed.add_field(name="1P", value=lst[0] if lst[0] else ':heart:')
        embed.add_field(name="2P", value=lst[1] if lst[1] else ':blue_heart:')
        embed.add_field(name='3P', value=lst[2] if lst[2] else ':yellow_heart:')
        embed.add_field(name='4P', value=lst[3] if lst[3] else ':purple_heart:')
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        await ctx.send(embed = embed)
    
    @commands.command()
    async def keymap(self, ctx):
        if (ctx.channel.id == int(self.channel_id)):
            keystr = '```'
            for value in self.sorted_button_list:
                for k,v in self.button_dict.items():
                    if value == v: 
                        fvalue = value.split('_')[0]
                        keystr += (f'{fvalue}').center(8) + ':' + (f'{k}').center(8) + '\n'
                        break
            keystr += '```'
            await ctx.send(keystr)

    @commands.command()
    async def changekey(self, ctx):
        if (ctx.channel.id == int(self.channel_id)):
            if re.match(r'.changekey\s[a-zA-Z]\s[a-zA-Z]', ctx.message.content):
                if ctx.message.content.split(' ')[1] in self.button_dict and ctx.message.content.split(' ')[2] not in self.button_dict:
                    self.button_dict[ctx.message.content.split(' ')[2]] = self.button_dict.pop(ctx.message.content.split(' ')[1])
                    await ctx.send('{} を {} に設定したよ :heart:'.format(self.button_dict[ctx.message.content.split(' ')[2]], ctx.message.content.split(' ')[2]))

    @commands.command()
    async def attack(self, ctx):
        if (ctx.channel.id == int(self.channel_id)):
            if re.match(r'.attack\s[a-zA-Z]\s[1-4]', ctx.message.content):
                button = ctx.message.content.split(' ')[1]
                group_num = ctx.message.content.split(' ')[2]
                attack_button = self.keyconf_dict[self.button_dict[button]][group_num]
                threading.Thread(
                    target=key_push,
                    args=('dummy_0', attack_button,self.sleep_time,
                )).start()

    @commands.command()
    async def resetkey(self, ctx):
        self.button_dict = BUTTON_DICT
        await ctx.send('キー設定をデフォルト値に設定したよ :heart:')

    @commands.command()
    async def automode(self, ctx):
        if (ctx.channel.id == int(self.channel_id)):
            if self.auto_mode_flag == False:
                self.switchauto.start()
                for button in self.button_dict.values():
                    if self.auto_button in self.keyconf_dict[button]:
                        group_num = self.keyconf_dict[button].index(self.auto_button) + 1
                        button = button.split('_')[0]
                        await ctx.send("{}Pの{}ボタンのオートモードをオンにしたよ :heart:".format(group_num, button))
                        break
            else:
                self.auto_mode_flag = False
                self.switchauto.cancel()
                await ctx.send("オートモードをオフにしたよ :heart:")

    @commands.command()
    async def autobutton(self, ctx):
        if (ctx.channel.id == int(self.channel_id)) and ctx.author.name in self.group:
            msg = (ctx.message.content + ' l').split(' ')[1]
            if msg in self.button_dict:
                self.auto_button = self.keyconf_dict[self.button_dict[msg]][self.group[ctx.author.name]]
                await ctx.send("オートボタンを" + self.group[ctx.author.name] + "Pの" + self.button_dict[msg] + "に設定したよ :heart:")

    @tasks.loop(seconds=0.2)
    async def switchauto(self):
        threading.Thread(
            target=key_push,
            args=('dummy_0', self.auto_button,self.sleep_time,
        )).start()

    @commands.command()
    async def setsec(self, ctx):
        if (ctx.channel.id == int(self.channel_id)):
            msg = ctx.message.content + ' ' + str(self.sleep_time)
            self.sleep_time=toNumber(msg.split(' ')[1])
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
            await ctx.send(str(ctx.author.name) + 'くんが4Pになったよ :perple_heart:')

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        elif message.channel.id != int(self.channel_id):
            return
        elif message.author.name not in self.group:
            self.group[message.author.name] = 0

        #### ボタン押下の一般化
        if message.content[0] in self.button_dict:
            threading.Thread(
                target=key_push_of_array,   
                args=(message.content, self.group[message.author.name], self.sleep_time, self.keyconf_dict, self.button_dict
            )).start()

        """
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
        elif message.content.startswith('l'):
            threading.Thread(
                target=key_push,
                args=(message.content, A_BUTTON[self.group[message.author.name]],self.sleep_time,
            )).start()
        elif message.content.startswith('k'):
            threading.Thread(
                target=key_push,
                args=(message.content, B_BUTTON[self.group[message.author.name]],self.sleep_time,
            )).start()
        elif message.content.startswith('i'):
            threading.Thread(
                target=key_push,
                args=(message.content, X_BUTTON[self.group[message.author.name]],self.sleep_time,
            )).start()
        elif message.content.startswith('j'):
            threading.Thread(
                target=key_push,
                args=(message.content, Y_BUTTON[self.group[message.author.name]],self.sleep_time,
            )).start()
        elif message.content.startswith('u'):
            threading.Thread(
                target=key_push,
                args=(message.content, L_BUTTON[self.group[message.author.name]],self.sleep_time,
            )).start()
        elif message.content.startswith('o'):
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
            """
        if message.content == '236p':
            pidx = self.group[message.author.name]
            pyautogui.keyDown(DOWN_BUTTON[pidx])
            pyautogui.keyDown(RIGHT_BUTTON[pidx])
            pyautogui.keyUp(DOWN_BUTTON[pidx])
            pyautogui.keyDown(Y_BUTTON[pidx])
            pyautogui.keyUp(RIGHT_BUTTON[pidx])
            pyautogui.keyUp(Y_BUTTON[pidx])
        elif message.content ==  '214p':
            pidx = self.group[message.author.name]
            pyautogui.keyDown(DOWN_BUTTON[pidx])
            pyautogui.keyDown(LEFT_BUTTON[pidx])
            pyautogui.keyUp(DOWN_BUTTON[pidx])
            pyautogui.keyDown(Y_BUTTON[pidx])
            pyautogui.keyUp(LEFT_BUTTON[pidx])
            pyautogui.keyUp(Y_BUTTON[pidx])


    @commands.Cog.listener()
    async def on_ready(self):
        print('Connected to Discord.')


def setup(bot):
    bot.add_cog(Commands(bot))
