import tkinter as tk
from tkinter import messagebox

print("당신은 용사입니다.. 게임을 하시겠습니까...?")
a = str(input("예/아니요          "))
if a != "예" :
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("나가", "나가세요!")
else:
    print("잘했어요!")
    input("누군가가 퀘스트를 걸었네요? 함께 받아봅시다!")
    input("누군가:슬라임 1마리만 잡아오게나.")
    input("당신은 퀘스트를 깨러 갔어요!")
    one_slime_hit = input("슬라임이 공격을 했다!! 공습경보!! 때리는걸 고르세요! 나뭇가지/쩌는검            ")
    if one_slime_hit == "나뭇가지" :
        input("성공!")
        input("당신은 다시 누군가한테 돌아갔다!")
        input("호호.. 용케 살아 돌아왔구나... 자 보답으로 진짜 쩌는 검을 주마!")
        input("당신은 진짜 쩌는검을 획득했다!")
        input("당신은 계속 걸어갔다!")
        input("갑자기 당신은 배가 고프다!")    
        ajrdmfrjanffhscjtqjsWo = input("무엇을 먹을까? 빵/먼지/바퀴벌레/똥/스파게티/스테이크/짬뽕/비프웰링턴        ")
        if ajrdmfrjanffhscjtqjsWo == "빵" or ajrdmfrjanffhscjtqjsWo == "먼지" or ajrdmfrjanffhscjtqjsWo == "스파게티" or ajrdmfrjanffhscjtqjsWo == "스테이크" or ajrdmfrjanffhscjtqjsWo == "짬뽕" or ajrdmfrjanffhscjtqjsWo == "비프웰링턴":
            root = tk.Tk()
            root.withdraw()
            messagebox.showinfo("없네요!", "없어요!")
        elif ajrdmfrjanffhscjtqjsWo == "똥":
            root = tk.Tk()
            root.withdraw()
            messagebox.showinfo("드러!", "윽 드러!")
        elif ajrdmfrjanffhscjtqjsWo == "바퀴벌레":
            input("당신은 맛있게 먹었다..")
            input("윽 드러...")
            wnqsms = input("당신은 누군가에 무기를 발견하고 주으려고 한다.. 줍는다/안줍는다           ")
            if wnqsms == "줍는다":
                input("잘했어요!")
                input("당신은 마왕에 성에 도달았어요!")
                input("들어 갔더니 무서워서 튀었더니 마왕이랑 발견했어요!")
                input("공격했어요!")
                input("피가20남았어요!")
                akwlakrakdhkdanrlrhfmrl = input("무슨 무기를 사용할거에요? 나뭇가지/진짜쩌는검/주은검      ")
                if akwlakrakdhkdanrlrhfmrl == "나뭇가지" or akwlakrakdhkdanrlrhfmrl == "주은검":
                    root = tk.Tk()
                    root.withdraw()
                    messagebox.showinfo("죽었네요!", "뭐하시는거죠? 허접이네요!")
                elif akwlakrakdhkdanrlrhfmrl == "진짜쩌는검":
                    root = tk.Tk()
                    root.withdraw()
                    messagebox.showinfo("안탑깝네요!!", "처음부터하세요!")
                else:
                    input("마왕을 물리쳤어요! 잘했네요!")
            else:
                root = tk.Tk()
                root.withdraw()
                messagebox.showinfo("주워야지!", "뭐하는거에요!")
        else:
            root = tk.Tk()
            root.withdraw()
            messagebox.showinfo("사망!", "죽었습니다")
    else:
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo("사망!", "죽었습니다")