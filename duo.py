from tkinter import *
import requests
import json

#봇듀오
a1=''
root1 = Tk()
root1.title("LOL Assistant")
root1.iconbitmap('icon.ico')
champ1 = ''
dic1 = {"자야": "498", "진": "202", "베인": "67", "미스포츈": "21", "직스": "115", "케이틀린": "51", "징크스": "222", "드레이븐": "119",
        "루시안": "236", "애쉬": "22", "스웨인": "50", "야스오": "157", "트리스타나": "18", "칼리스타": "429", "코그모": "96", "시비르": "15",
        "제라스": "101", "이즈리얼": "81", "카이사": "145", "바루스": "110", "아펠리오스": "523"}

dic2 = {"트린다미어": "23", "카밀": "164", "피오라": "114", "요네": "777", "쉔": "98", "요릭": "83", "우르곳": "6", "칼리스타": "429",
        "탐 켄치": "223", "그레이브즈": "104", "베인": "67", "워윅": "19", "사이온": "14", "아트록스": "266", "뽀삐": "78", "아칼리": "84",
        "세트": "875", "나서스": "75", "다리우스": "122", "문도 박사": "36", "릴리아": "876", "나르": "150", "빅토르": "112", "레넥톤": "58",
        "이렐리아": "39", "제이스": "126", "잭스": "24"}

dic3 = {"갈리오": "3", "그레이브즈": "104", "누누와 윌럼프": "20", "니코": "518", "다이애나": "131", "라이즈": "13", "럭스": "99", "럼블": "68",
        "레넥톤": "58", "루시안": "236", "르블랑": "7", "리산드라": "127", "마스터 이": "11", "말자하": "90", "말파이트": "54", "베이가": "45",
        "벡스": "711", "블라디미르": "8", "비에고": "234", "빅토르": "112", "사일러스": "517", "세트": "875", "신드라": "134", "신지드": "110",
        "아리": "103", "아우렐리온 솔": "136", "아지르": "268", "아칼리": "84", "아크샨": "166", "아트록스": "266", "애니": "1", "애니비아": "34",
        "야스오": "157", "에코": "245", "오리아나": "61", "요네": "777", "이렐리아": "39", "제드": "238", "제라스": "101", "제이스": "126",
        "조이": "142", "카사딘": "38", "카시오페아": "69", "카타리나": "55", "코르키": "42", "키아나": "246", "탈론": "91", "트린다미어": "23",
        "트위스티드 페이트": "4", "판테온": "80", "피즈": "105"}


def enter1():
    global champ1
    champ1 = str(e.get())
    global a1
    if champ1 in dic1:
        info1()
        text1 = Label(root1, text=a1)
        text1.pack()
        info2()
        text2 = Label(root1, text=a2)

        text2.pack()
        info3()
        text3 = Label(root1, text=a3)
        text3.pack()

    elif champ1 in dic2:
        info4()
        text1 = Label(root1, text=a1)
        text1.pack()
        info5()
        text2 = Label(root1, text=a2)

        text2.pack()
        info6()
        text3 = Label(root1, text=a3)
        text3.pack()

    elif champ1 in dic3:
        info7()
        text1 = Label(root1, text=a1)
        text1.pack()
        info8()
        text2 = Label(root1, text=a2)

        text2.pack()
        info9()
        text3 = Label(root1, text=a3)
        text3.pack()

def info1():
    global champ1
    dic1 ={"자야": "498", "진": "202", "베인": "67", "미스포츈": "21", "직스": "115", "케이틀린": "51", "징크스": "222","드레이븐": "119", "루시안": "236", "애쉬": "22", "스웨인": "50", "야스오": "157", "트리스타나": "18", "칼리스타": "429","코그모": "96", "시비르": "15", "제라스": "101", "이즈리얼": "81", "카이사": "145", "바루스": "110", "아펠리오스": "523"}
    duo_champ = dic1[champ1]
    url = "https://lol.ps/lol/duo_synergy/?duo=0&duo_champ={}&format=json&order_by=-synergy_score&version=35".format(duo_champ)
    content = requests.get(url).content
    json_data = json.loads(content)
    for i in range(1):
        global a1
        a1 = '[봇 듀오] 시너지 점수 1위인 서포터:'+json_data['results'][i]['champion_id2']['name']+"  "+json_data['results'][i]['champion_id1']['name']+"  "+"듀오 승률:"+json_data['results'][i]['duo_winrate']+"  "+"시너지 점수:"+json_data['results'][i]['synergy_score']+"  "+"픽률:"+json_data['results'][i]['pickrate']

def info2():
    global champ1
    dic1 = {"자야": "498", "진": "202", "베인": "67", "미스포츈": "21", "직스": "115", "케이틀린": "51", "징크스": "222","드레이븐": "119", "루시안": "236", "애쉬": "22", "스웨인": "50", "야스오": "157", "트리스타나": "18", "칼리스타": "429","코그모": "96", "시비르": "15", "제라스": "101", "이즈리얼": "81", "카이사": "145", "바루스": "110", "아펠리오스": "523"}
    duo_champ = dic1[champ1]
    url = "https://lol.ps/lol/duo_synergy/?duo=0&version=35&order_by=-duo_winrate&duo_champ={}".format(duo_champ)
    content = requests.get(url).content
    json_data = json.loads(content)
    for i in range(1):
        global a2
        a2 = '[봇 듀오] 승률 1위인 서포터:'+json_data['results'][i]['champion_id2']['name']+"  "+json_data['results'][i]['champion_id1']['name']+"  "+"듀오 승률:"+json_data['results'][i]['duo_winrate']+"  "+"시너지 점수:"+json_data['results'][i]['synergy_score']+"  "+"픽률:"+json_data['results'][i]['pickrate']


def info3():
    global champ1
    dic1 ={"자야": "498", "진": "202", "베인": "67", "미스포츈": "21", "직스": "115", "케이틀린": "51", "징크스": "222","드레이븐": "119", "루시안": "236", "애쉬": "22", "스웨인": "50", "야스오": "157", "트리스타나": "18", "칼리스타": "429","코그모": "96", "시비르": "15", "제라스": "101", "이즈리얼": "81", "카이사": "145", "바루스": "110", "아펠리오스": "523"}
    duo_champ = dic1[champ1]
    url = "https://lol.ps/lol/duo_synergy/?duo=0&version=35&order_by=-pickrate&duo_champ={}".format(duo_champ)
    content = requests.get(url).content
    json_data = json.loads(content)
    for i in range(1):
        global a3
        a3 = '[봇 듀오]픽률 1위인 서포터:'+json_data['results'][i]['champion_id2']['name']+"  "+json_data['results'][i]['champion_id1']['name']+"  "+"듀오 승률:"+json_data['results'][i]['duo_winrate']+"  "+"시너지 점수:"+json_data['results'][i]['synergy_score']+"  "+"픽률:"+json_data['results'][i]['pickrate']

def info4():
    global champ1
    dic2 = {"트린다미어": "23", "카밀": "164", "피오라": "114", "요네": "777", "쉔": "98", "요릭": "83", "우르곳": "6", "칼리스타": "429", "탐 켄치": "223","그레이브즈": "104", "베인": "67", "워윅": "19", "사이온": "14", "아트록스": "266", "뽀삐": "78", "아칼리": "84", "세트": "875", "나서스": "75","다리우스": "122", "문도 박사": "36", "릴리아": "876", "나르": "150", "빅토르": "112", "레넥톤": "58", "이렐리아": "39", "제이스": "126","잭스": "24"}
    duo_champ = dic2[champ1]
    url = "https://lol.ps/lol/duo_synergy/?duo=2&duo_champ={}&format=json&order_by=-synergy_score&version=35".format(duo_champ)
    content = requests.get(url).content
    json_data = json.loads(content)
    for i in range(1):
        global a1
        a1 = '[탑정글]시너지 점수 1위인 정글러:'+json_data['results'][i]['champion_id2']['name']+"  "+json_data['results'][i]['champion_id1']['name']+"  "+"듀오 승률:"+json_data['results'][i]['duo_winrate']+"  "+"시너지 점수:"+json_data['results'][i]['synergy_score']+"  "+"픽률:"+json_data['results'][i]['pickrate']

def info5():
    global champ1
    dic2 = {"트린다미어": "23", "카밀": "164", "피오라": "114", "요네": "777", "쉔": "98", "요릭": "83", "우르곳": "6", "칼리스타": "429", "탐 켄치": "223","그레이브즈": "104", "베인": "67", "워윅": "19", "사이온": "14", "아트록스": "266", "뽀삐": "78", "아칼리": "84", "세트": "875", "나서스": "75","다리우스": "122", "문도 박사": "36", "릴리아": "876", "나르": "150", "빅토르": "112", "레넥톤": "58", "이렐리아": "39", "제이스": "126","잭스": "24"}
    duo_champ = dic2[champ1]
    url = "https://lol.ps/lol/duo_synergy/?duo=2&version=35&order_by=-duo_winrate&duo_champ={}".format(duo_champ)
    content = requests.get(url).content
    json_data = json.loads(content)
    for i in range(1):
        global a2
        a2 = '[탑정글]승률 1위인 정글러:'+json_data['results'][i]['champion_id2']['name']+"  "+json_data['results'][i]['champion_id1']['name']+"  "+"듀오 승률:"+json_data['results'][i]['duo_winrate']+"  "+"시너지 점수:"+json_data['results'][i]['synergy_score']+"  "+"픽률:"+json_data['results'][i]['pickrate']


def info6():
    global champ1
    dic2 = {"트린다미어": "23", "카밀": "164", "피오라": "114", "요네": "777", "쉔": "98", "요릭": "83", "우르곳": "6", "칼리스타": "429", "탐 켄치": "223","그레이브즈": "104", "베인": "67", "워윅": "19", "사이온": "14", "아트록스": "266", "뽀삐": "78", "아칼리": "84", "세트": "875", "나서스": "75","다리우스": "122", "문도 박사": "36", "릴리아": "876", "나르": "150", "빅토르": "112", "레넥톤": "58", "이렐리아": "39", "제이스": "126","잭스": "24"}
    duo_champ = dic2[champ1]
    url = "https://lol.ps/lol/duo_synergy/?duo=2&version=35&order_by=-pickrate&duo_champ={}".format(duo_champ)
    content = requests.get(url).content
    json_data = json.loads(content)
    for i in range(1):
        global a3
        a3= '[탑정글]픽률 1위인 정글러:'+json_data['results'][i]['champion_id2']['name']+"  "+json_data['results'][i]['champion_id1']['name']+"  "+"듀오 승률:"+json_data['results'][i]['duo_winrate']+"  "+"시너지 점수:"+json_data['results'][i]['synergy_score']+"  "+"픽률:"+json_data['results'][i]['pickrate']

def info7():
    global champ1
    dic3 = {"갈리오":"3","그레이브즈":"104","누누와 윌럼프":"20","니코":"518","다이애나":"131","라이즈":"13","럭스":"99","럼블":"68","레넥톤":"58","루시안":"236","르블랑":"7","리산드라":"127","마스터 이":"11","말자하":"90","말파이트":"54","베이가":"45","벡스":"711","블라디미르":"8","비에고":"234","빅토르":"112","사일러스":"517","세트":"875","신드라":"134","신지드":"110","아리":"103","아우렐리온 솔":"136","아지르":"268","아칼리":"84","아크샨":"166","아트록스":"266","애니":"1","애니비아":"34","야스오":"157","에코":"245","오리아나":"61","요네":"777","이렐리아":"39","제드":"238","제라스":"101","제이스":"126","조이":"142","카사딘":"38","카시오페아":"69","카타리나":"55","코르키":"42","키아나":"246","탈론":"91","트린다미어":"23","트위스티드 페이트":"4","판테온":"80","피즈":"105"}
    duo_champ = dic3[champ1]
    url = "https://lol.ps/lol/duo_synergy/?duo=1&duo_champ={}&format=json&order_by=-synergy_score&version=35".format(duo_champ)
    content = requests.get(url).content
    json_data = json.loads(content)
    for i in range(1):
        global a1
        a1 = '[미드정글]시너지 점수 1위인 정글러:'+json_data['results'][i]['champion_id2']['name']+"  "+json_data['results'][i]['champion_id1']['name']+"  "+"듀오 승률:"+json_data['results'][i]['duo_winrate']+"  "+"시너지 점수:"+json_data['results'][i]['synergy_score']+"  "+"픽률:"+json_data['results'][i]['pickrate']

def info8():
    global champ1
    dic3 = {"갈리오":"3","그레이브즈":"104","누누와 윌럼프":"20","니코":"518","다이애나":"131","라이즈":"13","럭스":"99","럼블":"68","레넥톤":"58","루시안":"236","르블랑":"7","리산드라":"127","마스터 이":"11","말자하":"90","말파이트":"54","베이가":"45","벡스":"711","블라디미르":"8","비에고":"234","빅토르":"112","사일러스":"517","세트":"875","신드라":"134","신지드":"110","아리":"103","아우렐리온 솔":"136","아지르":"268","아칼리":"84","아크샨":"166","아트록스":"266","애니":"1","애니비아":"34","야스오":"157","에코":"245","오리아나":"61","요네":"777","이렐리아":"39","제드":"238","제라스":"101","제이스":"126","조이":"142","카사딘":"38","카시오페아":"69","카타리나":"55","코르키":"42","키아나":"246","탈론":"91","트린다미어":"23","트위스티드 페이트":"4","판테온":"80","피즈":"105"}
    duo_champ = dic3[champ1]
    url = "https://lol.ps/lol/duo_synergy/?duo=1&version=35&order_by=-duo_winrate&duo_champ={}".format(duo_champ)
    content = requests.get(url).content
    json_data = json.loads(content)
    for i in range(1):
        global a2
        a2 = "[미드정글]승률 1위인 정글러:"+json_data['results'][i]['champion_id2']['name']+" "+json_data['results'][i]['champion_id1']['name']+"  "+"듀오 승률:"+json_data['results'][i]['duo_winrate']+"  "+"시너지 점수:"+json_data['results'][i]['synergy_score']+"  "+"픽률:"+json_data['results'][i]['pickrate']


def info9():
    global champ1
    dic3 = {"갈리오":"3","그레이브즈":"104","누누와 윌럼프":"20","니코":"518","다이애나":"131","라이즈":"13","럭스":"99","럼블":"68","레넥톤":"58","루시안":"236","르블랑":"7","리산드라":"127","마스터 이":"11","말자하":"90","말파이트":"54","베이가":"45","벡스":"711","블라디미르":"8","비에고":"234","빅토르":"112","사일러스":"517","세트":"875","신드라":"134","신지드":"110","아리":"103","아우렐리온 솔":"136","아지르":"268","아칼리":"84","아크샨":"166","아트록스":"266","애니":"1","애니비아":"34","야스오":"157","에코":"245","오리아나":"61","요네":"777","이렐리아":"39","제드":"238","제라스":"101","제이스":"126","조이":"142","카사딘":"38","카시오페아":"69","카타리나":"55","코르키":"42","키아나":"246","탈론":"91","트린다미어":"23","트위스티드 페이트":"4","판테온":"80","피즈":"105"}
    duo_champ = dic3[champ1]
    url = "https://lol.ps/lol/duo_synergy/?duo=1&version=35&order_by=-pickrate&duo_champ={}".format(duo_champ)
    content = requests.get(url).content
    json_data = json.loads(content)
    for i in range(1):
        global a3
        a3 = "[미드정글]픽률 1위인 정글러:"+json_data['results'][i]['champion_id2']['name']+"  "+json_data['results'][i]['champion_id1']['name']+"  "+"듀오 승률:"+json_data['results'][i]['duo_winrate']+"  "+"시너지 점수:"+json_data['results'][i]['synergy_score']+"  "+"픽률:"+json_data['results'][i]['pickrate']



text = Label(root1, text="챔피언 이름을 입력하세요")
text.pack()

e = Entry(root1)
e.pack()

b1 = Button(root1, text="입력",command=enter1)

b1.pack()

root1.mainloop()