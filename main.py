import requests
import keyboard

games = []

class Game():
    def __init__(self, id, name, link, desc):
        self.id = id
        self.name = name
        self.link = link
        self.desc = desc
    def download(self):
        pass

class GlobShooter(Game):
    def __init__(self):
        super().__init__(id=0,name="Glob Shooter",link="🤓",desc="A fast-paced FPS game.")

print("Welcome to Globers Team GameLauncher!")
print("Here You can download all sorts of our games!")

for i in games:
    print(f"{games[i]}{i}")
