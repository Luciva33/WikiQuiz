import wikipedia
import random
import tkinter as tk
from tkinter import ttk
import time

wikipedia.set_lang("ja") # 日本語版Wikipediaをセット
correct=0 # 正解数
r='' # 問題文
root=tk.Tk()
root.geometry('400x600')
index = 1 # 進行状況

answers = [ # 回答欄
    '東京駅','神田駅 (東京都)','秋葉原駅','御徒町駅','上野駅','鶯谷駅',
    '日暮里駅','西日暮里駅','田端駅','駒込駅','巣鴨駅','大塚駅 (東京都)',
    '池袋駅','目白駅','高田馬場駅','新大久保駅','新宿駅','代々木駅','原宿駅',
    '渋谷駅','恵比寿駅','目黒駅','五反田駅','大崎駅','品川駅','高輪ゲートウェイ駅',
    '田町駅','浜松町駅','新橋駅','有楽町駅',
]

num = 0 # 問題番号
s = '' # Wiki本文
btn=None
s_btn=None
combo=None
start_time=''
l_result=None
re_btn=None

def clear_result():
    global l_result
    l_result['text']=''

def creat_que():
    global num,r,s,answers,combo,start_time,l_result
    que.delete(0.,tk.END)
    combo.delete(0, last=None)
    num = random.randint(0,len(answers)-1) # ランダムに正答を決定
    s = wikipedia.page(answers[num]).content # Wiki本文を取得
    target = 'は、' # 概要の冒頭を削除（読み仮名や英名などを削除）
    idx = s.find(target)
    r = s[idx+2:]
    ans_word = str(answers[num])
    if ans_word.endswith(' (東京都)'):
        ans_word.replace(' (東京都)','')
    r = r.replace(ans_word,'☆☆') # 本文中に正答が入っていれば消去
    r = r.replace(ans_word[:-1],'☆☆') 
    que.insert(0.,r)   

def btn_click():
    global correct,num,r,answers,l_result,btn,re_btn
    user_ans=combo.get()
    if user_ans==answers[num]:
        correct+=1
        msg='正解!'
        creat_que()
        root.after(1500,clear_result)
    else:
        msg='不正解'
        root.after(1500,clear_result)
    if correct==5:
        index=2
        clear_time = int(time.time() - start_time)
        clear_minute = clear_time // 60
        clear_second = (clear_time % 3600 % 60)
        #msg+=f'お疲れさまでした! \n今回のタイムは{clear_minute}分{clear_second}秒でした'
        que.delete(0.,tk.END)
        que.insert(1.0,f'お疲れさまでした! \n今回のタイムは{clear_minute}分{clear_second}秒でした')
        btn.destroy()
        combo.destroy()
        re_btn=tk.Button(text='もう一度あそぶ',font=('Arial',14,'bold'),fg='blue',bg='powderblue',command=game_main)
        re_btn.pack()

    l_result['text']=msg
    #root.after(1500,clear_result)

def game_main():
    global correct,r,index,answers,num,s_btn,re_btn
    if index==2:
        que.delete(0.,tk.END)
        re_btn.destroy()
    index=0
    que.insert(1.0,"WikiQuizは、Wikpediaの本文だけをみて、ページタイトルを当てるクイズです。\n\n\n表示される文章に、解答と全く同じ文字列が含まれる場合は「☆☆☆」に置き換わりますが、漢字/ひらがな/カタカナ/ローマ字など表記が異なる場合は置き換わりません。\n\nタイトルを特定できる情報を素早く見つけ、回答欄から正しい答えを選択し、5問正解したらクリアです\n\n\n準備ができたら、出題カテゴリを選択し【スタート】ボタンをクリックしてください。")
    s_btn=tk.Button(text='スタート',font=('Arial',14,'bold'),fg='red',bg='mistyrose',command=game_start)
    s_btn.pack()

def game_start():
    global correct,r,index,answers,num,s,s_btn,start_time,combo,l_result,btn
    index = 1
    s_btn.destroy()
    que.insert(1.0,r)
    combo=ttk.Combobox(root,values=answers,font=('Arial',14),justify="center",state="readonly")
    combo.pack()
    btn=tk.Button(text='答える',font=('Arial',14,'bold'),fg='red',bg='mistyrose',command=btn_click)
    btn.pack()
    l_result=tk.Label(text='',font=('Arial',20))
    l_result.pack()
    creat_que()
    start_time = time.time()


fnt=('Arial',30)
title=tk.Label(text='WikiQuiz',font=fnt)
title.pack(side=tk.TOP)
category=tk.Label(text='出題カテゴリ：山手線の駅',font=('Arial',14))
category.pack(side=tk.TOP)
que = tk.Text(background='lightblue')
que.pack()
"""
#que.insert(1.0,r)
que.pack()
combo=ttk.Combobox(root,values=answers,font=('Arial',14),justify="center",state="readonly")
combo.pack()
btn=tk.Button(text='答える',font=('Arial',14,'bold'),fg='red',bg='mistyrose',command=btn_click)
btn.pack()
l_result=tk.Label(text='',font=('Arial',20))
l_result.pack()
creat_que()
start_time = time.time()
"""
game_main()
root.mainloop()