import requests

games = []
sus = "%"
class Game():
    def __init__(self, id, name, link, desc):
        self.id = id
        self.name = name
        self.link = link
        self.desc = desc
    def download(self):
        response = requests.get(self.link)
        open("game.zip", "wb").write(response.content)

class GlobShooter(Game):
    def __init__(self):
        super().__init__(id=0,name="Glob Shooter",link=f"https://github.com/Globers-Team/game-builds/raw/main/Glob{sus}20shooter/globusek.zip",desc="A fast-paced FPS game.")

games.append(GlobShooter())

print("Welcome to Globers Team GameLauncher!")
print("Here You can download all sorts of our games!")
print("Note: You are currently using TUI/shell mode. To exit, just type: WIP")

games[0].download()
for i in games:
    print(f"{i.id + 1}. {i.name}")
    cmd = input("Enter command: ")
    cmd = cmd.split()
    if cmd[0] == "install":
        for i in games:
            if i.id + 1 == cmd[1]:
                i.download()
