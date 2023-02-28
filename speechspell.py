import speech_recognition as s
import requests
import json
from win10toast import ToastNotifier
import datetime
import tkinter as tk
import threading as th
from tkinter import messagebox
import asyncio

riot_token = "RGAPI-63ae5d03-629a-44d6-aada-7598869c0272"
input_text = ""
flash = ""
heal = ""
barrier = ""
ghost = ""
ignite = ""


remainingsecond = 10 #스펠 남은 시간 알림 기본값 10
flashcommand = " 노플" #플래쉬 음성인식 커맨드
healcommand = " 노힐" #플래쉬 음성인식 커맨드
ghostcommand = "노유체화" #플래쉬 음성인식 커맨드
barriercommand = "노베리어" #플래쉬 음성인식 커맨드
ignitecommand = " 노점화"
#teleportcommand = ""


def check1():
    global input_text
    input_text = en1.get()
    if input_text:
        UserInfoUrl = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + input_text
        res = requests.get(UserInfoUrl, headers={"X-Riot-Token": riot_token})
        resstatus = res.status_code
        print(res.status_code)
        if resstatus == 200:
            resjs = json.loads(res.text)
            UserInfoUrl_2 = "https://kr.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/" + resjs["id"]
            res2 = requests.get(UserInfoUrl_2, headers={"X-Riot-Token": riot_token})
            res2status = res2.status_code
            print(res2.status_code)
            if res2status == 200:
                loop = asyncio.get_event_loop()
                loop.run_until_complete(speechrun())
                loop.close()
            else:
                messagebox.showinfo("error", "사용자의 게임정보를 가져올 수 없습니다.")

        else:
            messagebox.showinfo("error", "사용자를 찾을 수 없습니다.")
    else:
        messagebox.showinfo("error", "사용자명을 입력하세요")

async def setremainseconds():
    global remainingsecond
    remainingsecond = en2.get()
    print(remainingsecond)
    print(remaintoast(" 탑"," 플래쉬"))



async def remaintoast(pos,spell):
    icon = "icon.ico"
    t = ToastNotifier()
    content = str(remainingsecond) + "초 뒤"+pos+spell+"가 돕니다"
    notice = t.show_toast("스펠체크", content, duration=10, icon_path=icon)
    return notice

# def getingamedata(sp):
#     global flash
#     global heal
#     global barrier
#     global ghost
#     global ignite
#     #global teleport
#     UserInfoUrl = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + input_text
#     res = requests.get(UserInfoUrl, headers={"X-Riot-Token": riot_token})
#     resjs = json.loads(res.text)
#     UserInfoUrl_2 = "https://kr.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/" + resjs["id"]
#     res2 = requests.get(UserInfoUrl_2, headers={"X-Riot-Token": riot_token})
#     res2js = json.loads(res2.text)
#     st = datetime.datetime.fromtimestamp(res2js["gameStartTime"] / 1000)
#     nt = datetime.datetime.now()
#     gtm = (nt - st).seconds // 60
#     gts = (nt - st).seconds % 60
#     flash = str(gtm + 5) + "분" + str(gts) + "초에 쿨타임이 종료됩니다"
#     heal = str(gtm + 4) + "분" + str(gts) + "초에 쿨타임이 종료됩니다"
#     barrier = str(gtm + 3) + "분" + str(gts) + "초에 쿨타임이 종료됩니다"
#     ghost = str(gtm + 3) + "분" + str(gts + 30) + "초에 쿨타임이 종료됩니다"
#     ignite = str(gtm + 3) + "분" + str(gts) + "초에 쿨타임이 종료됩니다"


    #teleport = 쿨타임이 420 - (레벨*10)


async def speechrun():
    global flash
    global heal
    global barrier
    global ghost
    global ignite
    # global teleport
    UserInfoUrl = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + input_text
    res = requests.get(UserInfoUrl, headers={"X-Riot-Token": riot_token})
    resjs = json.loads(res.text)
    UserInfoUrl_2 = "https://kr.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/" + resjs["id"]
    res2 = requests.get(UserInfoUrl_2, headers={"X-Riot-Token": riot_token})
    res2js = json.loads(res2.text)
    st = datetime.datetime.fromtimestamp(res2js["gameStartTime"] / 1000)
    nt = datetime.datetime.now()
    gtm = (nt - st).seconds // 60
    gts = (nt - st).seconds % 60
    flash = str(gtm + 5) + "분" + str(gts) + "초에 쿨타임이 종료됩니다"
    heal = str(gtm + 4) + "분" + str(gts) + "초에 쿨타임이 종료됩니다"
    barrier = str(gtm + 3) + "분" + str(gts) + "초에 쿨타임이 종료됩니다"
    ghost = str(gtm + 3) + "분" + str(gts + 30) + "초에 쿨타임이 종료됩니다"
    ignite = str(gtm + 3) + "분" + str(gts) + "초에 쿨타임이 종료됩니다"
    r = s.Recognizer()
    run = True
    while run:
        with s.Microphone() as source:
            print('Speack Anything :')
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio, language='ko-KR')
                print(text)
                print("탑"+flashcommand)
                print(remainingsecond)
                if text == "멈춰":
                    run = False
                    print("음성인식을 종료합니다")
                else:
                    ################################################################
                    #플래쉬
                    if text == "탑"+flashcommand:
                        icon = "icon.ico"
                        t = ToastNotifier()
                        content = "탑 플래쉬가" + str(flash)
                        t.show_toast("스펠체크", content, duration=10, icon_path=icon)
                        timer = th.Timer(300, await remaintoast("탑","플래쉬"))
                        timer.start()
                    if text == "정글" + flashcommand:
                        icon = "icon.ico"
                        t = ToastNotifier()
                        content = "정글 플래쉬가" + str(flash)
                        t.show_toast("스펠체크", content, duration=10, icon_path=icon)
                        timer = th.Timer(300-remainingsecond, await remaintoast("정글","플래쉬"))
                        timer.start()
                    if text == "미드" + flashcommand:
                        icon = "icon.ico"
                        t = ToastNotifier()
                        content = "미드 플래쉬가" + str(flash)
                        t.show_toast("스펠체크", content, duration=10, icon_path=icon)
                        timer = th.Timer(300-remainingsecond, await remaintoast("미드","플래쉬"))
                        timer.start()
                    if text == "원딜" + flashcommand:
                        icon = "icon.ico"
                        t = ToastNotifier()
                        content = "원딜 플래쉬가" + str(flash)
                        t.show_toast("스펠체크", content, duration=10, icon_path=icon)
                        timer = th.Timer(300-remainingsecond, await remaintoast("원딜","플래쉬"))
                        timer.start()
                    if text == "서폿" + flashcommand:
                        icon = "icon.ico"
                        t = ToastNotifier()
                        content = "서폿 플래쉬가" + str(flash)
                        t.show_toast("스펠체크", content, duration=10, icon_path=icon)
                        timer = th.Timer(300-remainingsecond, await remaintoast("서폿","플래쉬"))
                        timer.start()
                    #################################################################
                    #유체화
                    if text == "탑" + ghostcommand:
                        icon = "icon.ico"
                        t = ToastNotifier()
                        content = "탑 유체화가" + str(ghost)
                        t.show_toast("스펠체크", content, duration=10, icon_path=icon)
                        timer = th.Timer(300-remainingsecond, await remaintoast("탑","유체화"))
                        timer.start()
                    if text == "정글" + ghostcommand:
                        icon = "icon.ico"
                        t = ToastNotifier()
                        content = "정글 유체화가" + str(ghost)
                        t.show_toast("스펠체크", content, duration=10, icon_path=icon)
                        timer = th.Timer(300-remainingsecond, await remaintoast("정글","유체화"))
                        timer.start()
                    if text == "미드" + ghostcommand:
                        icon = "icon.ico"
                        t = ToastNotifier()
                        content = "미드 유체화가" + str(ghost)
                        t.show_toast("스펠체크", content, duration=10, icon_path=icon)
                        timer = th.Timer(300-remainingsecond, await remaintoast("미드","유체화"))
                        timer.start()
                    if text == "원딜" + ghostcommand:
                        icon = "icon.ico"
                        t = ToastNotifier()
                        content = "원딜 유체화가" + str(ghost)
                        t.show_toast("스펠체크", content, duration=10, icon_path=icon)
                        timer = th.Timer(300-remainingsecond, await remaintoast("원딜","유체화"))
                        timer.start()
                    if text == "서폿" + ghostcommand:
                        icon = "icon.ico"
                        t = ToastNotifier()
                        content = "서폿 유체화가" + str(ghost)
                        t.show_toast("스펠체크", content, duration=10, icon_path=icon)
                        timer = th.Timer(300-remainingsecond, await remaintoast("서폿","유체화"))
                        timer.start()


            except:
                print('알아들을수 없습니다')




window=tk.Tk()
window.geometry("380x700")
window.title("LOL Assistant")
window.iconbitmap('icon.ico')
window.resizable(False, False)
f= tk.Frame(window, width=380, height=700, bg="#404040").place(x=0, y=0)

l1= tk.Label(window, text='게임 시작 후 자신의 닉네임을 입력하세요', width=50, height=3,fg='white', border=0, bg="#404040", font=('티머니 둥근바람 ExtraBold', 10))
l1.pack()

en1=tk.Entry(window,fg='white', border=1, bg="#404040", font=('티머니 둥근바람 ExtraBold', 10))
en1.pack(ipadx=10, pady=10)

b1=tk.Button(window, text='확인', command=check1,fg='white', border=0, bg="#404040", font=('티머니 둥근바람 ExtraBold', 10))
b1.place(x=310,y=60)

l2= tk.Label(window, text='스펠이 해당 초만큼 남았을때 알림을 보냅니다.(기본값 : 10초)', width=50, height=3,fg='white', border=0, bg="#404040", font=('티머니 둥근바람 ExtraBold', 10))
l2.pack()

en2=tk.Entry(window,fg='white', border=1, bg="#404040", font=('티머니 둥근바람 ExtraBold', 10))
en2.pack(ipadx=10, pady=10)

b2=tk.Button(window, text='확인', command=setremainseconds,fg='white', border=0, bg="#404040", font=('티머니 둥근바람 ExtraBold', 10))
b2.place(x=310,y=155)


l3= tk.Label(window, text='플래쉬 음성인식 커맨드(기본값 노플)', width=50, height=3,fg='white', border=0, bg="#404040", font=('티머니 둥근바람 ExtraBold', 10))
l3.pack()

en3=tk.Entry(window,fg='white', border=1, bg="#404040", font=('티머니 둥근바람 ExtraBold', 10))
en3.pack(ipadx=10, pady=10)

b3=tk.Button(window, text='저장',fg='white', border=0, bg="#404040", font=('티머니 둥근바람 ExtraBold', 10))
b3.place(x=310,y=250)

l4= tk.Label(window, text='점화 음성인식 커맨드(기본값 노점화)', width=50, height=3,fg='white', border=0, bg="#404040", font=('티머니 둥근바람 ExtraBold', 10))
l4.pack()

en4=tk.Entry(window,fg='white', border=1, bg="#404040", font=('티머니 둥근바람 ExtraBold', 10))
en4.pack(ipadx=10, pady=10)

b4=tk.Button(window, text='저장',fg='white', border=0, bg="#404040", font=('티머니 둥근바람 ExtraBold', 10))
b4.place(x=310,y=340)

l5= tk.Label(window, text='유체화 음성인식 커맨드(기본값 노유체화)', width=50, height=3,fg='white', border=0, bg="#404040", font=('티머니 둥근바람 ExtraBold', 10))
l5.pack()

en5=tk.Entry(window,fg='white', border=1, bg="#404040", font=('티머니 둥근바람 ExtraBold', 10))
en5.pack(ipadx=10, pady=10)

b5=tk.Button(window, text='저장',fg='white', border=0, bg="#404040", font=('티머니 둥근바람 ExtraBold', 10))
b5.place(x=310,y=430)

l6= tk.Label(window, text='힐 음성인식 커맨드(기본값 노힐)', width=50, height=3,fg='white', border=0, bg="#404040", font=('티머니 둥근바람 ExtraBold', 10))
l6.pack()

en6=tk.Entry(window,fg='white', border=1, bg="#404040", font=('티머니 둥근바람 ExtraBold', 10))
en6.pack(ipadx=10, pady=10)

b6=tk.Button(window, text='저장',fg='white', border=0, bg="#404040", font=('티머니 둥근바람 ExtraBold', 10))
b6.place(x=310,y=530)

l7= tk.Label(window, text='베리어 음성인식 커맨드(기본값 노베리어)', width=50, height=3,fg='white', border=0, bg="#404040", font=('티머니 둥근바람 ExtraBold', 10))
l7.pack()

en7=tk.Entry(window,fg='white', border=1, bg="#404040", font=('티머니 둥근바람 ExtraBold', 10))
en7.pack(ipadx=10, pady=10)

b7=tk.Button(window, text='저장',fg='white', border=0, bg="#404040", font=('티머니 둥근바람 ExtraBold', 10))
b7.place(x=310,y=620)



window.mainloop()