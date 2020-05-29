from discord.ext import tasks, commands

# class, メンバにdefaultSEC, 詰めて書いて同時押し, spaceで連続押下, 1p2pオブジェクト, ボタン連打

conf = []
with open('./input_config.txt') as f:
    for line in f:
        conf.append(line.rstrip('\n').split(', '))

# Input Config
DEFAULT_SLEEP_TIME=0.0
KEYCONF_DICT = {}
for str in conf:
    KEYCONF_DICT[str[0]] = str[1:5]

print(KEYCONF_DICT)