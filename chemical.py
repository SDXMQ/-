from tkinter import * #창을 만드는데 필요한 라이브러리
Ingpage = 1           #왼쪽 재료 창 페이지 수

win = Tk() #창 함수
win.geometry("1000x600") # 창 크기
win.title("나만의 화학실") # 창 제목
win.option_add("*font", "System 25") # 창 기본 폰트
win.resizable(width=False, height=False) # 창 넓이 조정 금지

TitleLabel = Label(win, text='★멋있는 화학 조합게임★', font="System 50") # 메인 화면 제목

Ings = ['H', 'He',
        'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne',
        'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar',
        'K', 'Ca']  # 왼쪽 재료 목록에 추가될 기본 재료

Combined = {                                            # 레시피 목록
    'HH': {'Name': '수소 분자', 'DisplayName': 'H₂'},    #Name: 조합시 보이는 글씨
    'H₂O': {'Name': '물', 'DisplayName': 'H₂O'},        #DisplayName: 버튼에 보이는 글씨
    'LiCl': {'Name': '염화 리튬', 'DisplayName': 'LiCl'},
    'LiOH': {'Name': '수산화 리튬', 'DisplayName': 'LiOH'},
    'BeO': {'Name': '산화 베릴륨', 'DisplayName': 'BeO'},
    'BeCl₂': {'Name': '염화 베릴륨', 'DisplayName': 'BeCl₂'},
    'B₂O₃': {'Name': '산화 붕소', 'DisplayName': 'B₂O₃'},
    'CO₂': {'Name': '이산화탄소', 'DisplayName': 'CO₂'},
    'CH₄': {'Name': '메테인', 'DisplayName': 'CH₄'},
    'NN': {'Name': '질소 분자', 'DisplayName': 'N₂'},
    'OO': {'Name': '산소 분자', 'DisplayName': 'O₂'},
    'OH': {'Name': '수산화이온', 'DisplayName': 'OH'},
    'O₂O₂': {'Name': '오존', 'DisplayName': 'O₃'},
    'HF': {'Name': '플루오르화 수소', 'DisplayName': 'HF'},
    'FF': {'Name': '플루오르 분자', 'DisplayName': 'F₂'},
    'NaCl': {'Name': '염화 나트륨', 'DisplayName': 'NaCl'},
    'NaOH': {'Name': '수산화 나트륨', 'DisplayName': 'NaOH'},
    'MgO': {'Name': '산화 마그네슘', 'DisplayName': 'MgO'},
    'MgCl₂': {'Name': '염화 마그네슘', 'DisplayName': 'MgCl₂'},
    'SiO₂': {'Name': '이산화 실리콘', 'DisplayName': 'SiO₂'},
    'SO₂': {'Name': '이산화황', 'DisplayName': 'SO₂'},
    'H₂S': {'Name': '황화수소', 'DisplayName': 'H₂S'},
    'ClCl': {'Name': '염소 분자', 'DisplayName': 'Cl₂'},
    'HCl': {'Name': '염화수소', 'DisplayName': 'HCl'},
    'KCl': {'Name': '염화 칼륨', 'DisplayName': 'KCl'},
    'KOH': {'Name': '수산화 칼륨', 'DisplayName': 'KOH'},
    'CaO': {'Name': '산화 칼슘', 'DisplayName': 'CaO'},
    'CaCl₂': {'Name': '염화 칼슘', 'DisplayName': 'CaCl₂'}
          }

def IngOnTable(btn):  # 재료 버튼을 눌렀을때 재료가 조합창 위로 올라가게 하는 커스텀 함수
    BtnText = btn.cget("text") # 버튼의 텍스트를 가져옴
    if CombiTable2.size() == 0: # 2번 조합창이 비었을때
        if CombiTable1.size() == 0: # 1번 조합창이 비었으면
            CombiTable1.insert(END, BtnText) # 1번 조합창에 원소 올림
        else: # 아니면(1번 조합창이 안비었으면)
            CombiTable2.insert(END, BtnText) # 2번 조합창에 원소 올림

IngBtn = [] # 재료 버튼들을 모아둘 리스트
for x in range(6): # 6번 반복
    btn = Button(win, text=f"{Ings[x]}", width=10, height=1) # 버튼 생성(텍스트를 기본재료로 함)
    btn.config(command = lambda b=btn: IngOnTable(b)) # 버튼이 작동할 함수 지정(IngOnTable)
    btn.place(x=10, y=5 + 75 * (x + 1)) # 버튼을 위치시키고 보이게 함
    IngBtn.append(btn) # 생성된 버튼을 리스트 안에 넣음

CombiTable1 = Listbox(win, height=1, width=4, font="System 200") # 조합창 1번칸
CombiTable2 = Listbox(win, height=1, width=4, font="System 200") # 조합창 2번칸

def ClearCombiTable(): # 지우기 버튼 커스텀 함수
    CombiTable1.delete(END) # 조합창 1번칸 지움
    CombiTable2.delete(END) # 조합창 2번칸 지움

ClearButton = Button(win, text="지우기", # 지우기 버튼 만들기
                     width = 10, height = 1, command=ClearCombiTable)

def Combine(): # 조합하기 버튼 커스텀 함수
    EasterEggList = {'H₂OH₂O':'물을 너무 많이 마시지 마세요.', # 이스터에그
                     'N₂N₂':'질소는 과자 포장만 해도 충분합니다.',
                     'LiLi':'당신은 방금 리튬을 쌓았습니다!',
                     'O₃O₃':'오존층이 건강해졌습니다.',
                     'NaClNaCl':"너무 짜요"}
    CombiIng1 = CombiTable1.get(END) # 조합창 1번칸의 함수를 가져옴
    CombiIng2 = CombiTable2.get(END) # 조합창 2번칸의 함수를 가져옴
    if CombiIng1 + CombiIng2 in Combined: # 조합창 1번+2번이 레시피 안에 있을때
        CombiInfo.config(text=f'{Combined[CombiIng1 + CombiIng2]['Name']}(이)가 합성되었습니다!') # 합성되었다는 말 띄우기
        Ings.append(Combined[CombiIng1 + CombiIng2]['DisplayName']) # 합성된 원소 추가
        PageShift() # 새로고침
        CombiTable1.delete(END)# 조합창 1번칸 지움
        CombiTable2.delete(END)# 조합창 2번칸 지움

    elif CombiIng1 + CombiIng2 in EasterEggList: # 근데 만약 이스터에그 목록에 있으면
        CombiInfo.config(text=EasterEggList[CombiIng1 + CombiIng2]) # 그에 맞는 텍스트 띄우기
        CombiTable1.delete(END) # 조합창 1번칸 지움
        CombiTable2.delete(END) # 조합창 2번칸 지움

    elif CombiIng1 + CombiIng2 == "": # 빈칸이면
        CombiInfo.config(text="원소가 추가되지 않았습니다.") # 텍스트 띄우기

    else: # 그것도 아니면
        CombiInfo.config(text="잘못된 조합입니다. 순서나 원소를 확인하세요.") # 텍스트 띄우기
        CombiTable1.delete(END) # 조합창 1번칸 지움
        CombiTable2.delete(END) # 조합창 2번칸 지움

CombiButton = Button(win, text="합성하기!", # 합치기버튼
                     width = 10, height = 1, command=Combine)

JustPlus = Label(win, text="+", font="System 200") # 더하기 장식

CombiInfo = Label(win, text="아직 합성된 원소가 없습니다.", anchor='center') # 정보 띄우는 텍스트

def PageShift(): # 새로고침 커스텀 함수
    start = 6 * (Ingpage - 1)
    for x in range(6): # 6번 반복
        if start + x < len(Ings):
            IngBtn[x].config(text=Ings[start + x]) # 다음 원소에 맞게 글씨 변경
        else:
            IngBtn[x].config(text="") # 없으면 빈칸

def UpClick(): # 페이지 위버튼 커스텀 함수
    global Ingpage
    if Ingpage != 1:
        Ingpage = Ingpage-1
        PageShift()
    print(Ingpage)

UpButton = Button(win, text = "▲", # 위버튼
            width = 10, height = 1, command=UpClick)

def LowClick(): # 페이지 아래버튼 커스텀 함수
    global Ingpage
    if Ingpage != len(Ings)//6+1:
        Ingpage = Ingpage+1
        PageShift()
    print(Ingpage)

LowButton = Button(win, text = "▼", # 아래버튼
            width = 10, height = 1, command=LowClick)

#============================= 버튼 최종 처리
# 제목
TitleLabel.place(x=250, y=20)

# 페이지 버튼 배치
UpButton.pack(anchor=NW, pady=10)
# 요소 버튼 배치
for btn in IngBtn:
    btn.pack(anchor=NW, pady=10)
# 페이지 버튼 배치2
LowButton.pack(anchor=NW, pady=10)

CombiTable1.place(x=300, y=230)
JustPlus.place(x=565, y=230)
CombiTable2.place(x=700, y=230)

# Clear 및 Combi 버튼 배치
ClearButton.place(x=375, y=400)
CombiButton.place(x=625, y=400)
CombiInfo.place(x=350, y=500)

win.mainloop()