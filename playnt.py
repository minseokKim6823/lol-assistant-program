import time
from win10toast import ToastNotifier
import tkinter as tk
import threading
import requests
import json




riot_token ='RGAPI-63ae5d03-629a-44d6-aada-7598869c0272'
input_text = ""
nickname =[]

def check():
    global input_text
    input_text = en1.get()
    l1 = tk.Label(window, text=input_text, fg='white', border=0, bg="#404040",
                  font=('티머니 둥근바람 ExtraBold', 20))
    l1.place(x=60, y=80)
    b2 = tk.Button(window, text='해당 소환사를 알림목록에 추가하기', command=check2, fg='white', border=1, bg="#404040", font=('티머니 둥근바람 ExtraBold', 11))
    b2.place(x=300, y=85)
    threading.Thread(target=run).start()

def check2():
    global nickname
    nickname.append(input_text)
    print(input_text)
    threading.Thread(target=notice).start()


def notice():
    l7 = tk.Label(window, text="알림 받는 소환사 목록", fg='white', border=1, bg="#404040", font=('티머니 둥근바람 ExtraBold', 14))
    l7.place(x=60, y=250)
    l8 = tk.Label(window, text=nickname, fg='white', border=1, bg="#404040", font=('티머니 둥근바람 ExtraBold', 11))
    l8.place(x=60, y=280)
    for i in range(len(nickname)):
        if nickname :
            UserInfoUrl = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + nickname[i]
            res = requests.get(UserInfoUrl, headers={"X-Riot-Token": riot_token})
            resjs = json.loads(res.text)
            print(resjs["id"])
            UserInfoUrl_2 = "https://kr.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/" + resjs["id"]
            res2 = requests.get(UserInfoUrl_2, headers={"X-Riot-Token": riot_token})
            print(res2.status_code)
            while True:
                try:
                    if res2.status_code == 200:
                        icon = "icon.ico"
                        t = ToastNotifier()
                        t.show_toast("플레이 알림", "%s님이 현재 플레이중 입니다." % input_text, duration=10, icon_path=icon)
                except:
                    pass
                time.sleep(60)



def run():
    if input_text :
        UserInfoUrl = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + input_text
        res = requests.get(UserInfoUrl, headers={"X-Riot-Token": riot_token})
        resjs = json.loads(res.text)
        UserInfoUrl_2 = "https://kr.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/" + resjs["id"]
        res2 = requests.get(UserInfoUrl_2, headers={"X-Riot-Token": riot_token})
        URL3 = "https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/" + resjs["id"]
        res3 = requests.get(URL3, headers={"X-Riot-Token": riot_token})
        rankinfo = json.loads(res3.text)
        for i in rankinfo:
            if i["queueType"] == "RANKED_SOLO_5x5":
                l3 = tk.Label(window,text="솔로랭크",fg='white', border=0, bg="#404040", font=('티머니 둥근바람 ExtraBold', 11), anchor="w")
                l3.place(x=60, y=130)
                l4 = tk.Label(window, text="티어 : {} {} {}점   승률 : {}승 {}패".format(i["tier"], i["rank"],i["leaguePoints"],i["wins"], i["losses"]),fg='white', border=0, bg="#404040", font=('티머니 둥근바람 ExtraBold', 11),anchor="w")
                l4.place(x=60, y=150)
            if i["queueType"] == "RANKED_FLEX_SR":
                l5 = tk.Label(window,text="자유랭크",fg='white', border=0, bg="#404040", font=('티머니 둥근바람 ExtraBold', 11), anchor="w")
                l5.place(x=60, y=170)
                l6 = tk.Label(window, text="티어 : {} {} {}점   승률 : {}승 {}패".format(i["tier"], i["rank"],i["leaguePoints"], i["wins"], i["losses"]),fg='white', border=0, bg="#404040", font=('티머니 둥근바람 ExtraBold', 11),anchor="w")
                l6.place(x=60, y=190)


    else:
        print("소환사가 존재하지 않습니다.")

window=tk.Tk()
window.title("LOL Assistant")
window.iconbitmap('icon.ico')
window.geometry("640x400+200+200")
window.resizable(False, False)



f= tk.Frame(window, width=640, height=400, bg="#404040").place(x=0, y=0)

l1= tk.Label(window, text='전적을 검색할 소환사 닉네임을 입력하세요', width=30, height=3,fg='white', border=0, bg="#404040", font=('티머니 둥근바람 ExtraBold', 11))
l1.pack()
en1=tk.Entry(window, width=25)
en1.place(x=200,y=50)
b1=tk.Button(window, text='확인', command=check, fg='white', border=1, bg="#404040", font=('티머니 둥근바람 ExtraBold', 11))
b1.place(x=400,y=45)
window.mainloop()