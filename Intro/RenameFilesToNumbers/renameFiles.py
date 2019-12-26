import os

path = 'D:/DiscordBot/images'
i = 0
for filename in os.listdir(path):
    os.rename(os.path.join(path, filename), os.path.join(path, str(i) + ".png"))
    i = i + 1
