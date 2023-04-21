import requests
import keyboard

games = []

class Game():
    def __init__(self, id, name, link, desc):
        self.id = id
        self.name = name
        self.link = link
        self.desc = desc
        response = requests.get(self.link)
        open("game.zip", "wb").write(response.content)

class GlobShooter(Game):
    def __init__(self):
        super().__init__(id=0,name="Glob Shooter",link="🤓",desc="A fast-paced FPS game.")

games.append(GlobShooter())

print("Welcome to Globers Team GameLauncher!")
print("Here You can download all sorts of our games!")

for i in games:
    print(f"{i.id + 1}. {i.name}")
