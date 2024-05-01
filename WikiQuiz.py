import wikipedia
import random
import tkinter as tk
from tkinter import ttk,messagebox
import time
import rank_dao

wikipedia.set_lang("ja") # 日本語版Wikipediaをセット
correct=0 # 正解数
r='' # 問題文
root=tk.Tk()
root.title("WikiQuiz")
root.geometry('500x600')
index = 1 # 進行状況

answers = [ # 回答一覧
    ['東京駅','神田駅 (東京都)','秋葉原駅','御徒町駅','上野駅','鶯谷駅',
    '日暮里駅','西日暮里駅','田端駅','駒込駅','巣鴨駅','大塚駅 (東京都)',
    '池袋駅','目白駅','高田馬場駅','新大久保駅','新宿駅','代々木駅','原宿駅',
    '渋谷駅','恵比寿駅','目黒駅','五反田駅','大崎駅','品川駅','高輪ゲートウェイ駅',
    '田町駅','浜松町駅','新橋駅','有楽町駅'],
    ['ゼルダの伝説 ティアーズ オブ ザ キングダム','スーパーマリオブラザーズ ワンダー',
     'ピクミン4','ポケットモンスター スカーレット・バイオレット','桃太郎電鉄ワールド 〜地球は希望でまわってる!〜',
     'マリオカート8 デラックス','星のカービィ Wii デラックス','ドラゴンクエストモンスターズ3 魔族の王子とエルフの旅',
     'スプラトゥーン3','スーパーマリオRPG'],
    ['Mrs. GREEN APPLE','Vaundy','YOASOBI','back number','Official髭男dism',
     'BTS (音楽グループ)','優里','米津玄師','Ado','あいみょん'],
    ['呪術廻戦','ONE PIECE','SPY×FAMILY','東京卍リベンジャーズ','僕のヒーローアカデミア',
     'チェンソーマン','キングダム (漫画)','ブルーロック','転生したらスライムだった件','怪獣8号'],
    ['金融庁','消費者庁','こども家庭庁','デジタル庁','復興庁','総務省','法務省','外務省','財務省','文部科学省','厚生労働省','農林水産省','経済産業省',
     '国土交通省','環境省','防衛省',]
]

cate = [
    '山手線の駅','2023年家庭用ゲームソフト販売本数TOP10','2023年Spotify Japanで最も再生されたアーティストTOP10',
    '2023年コミック年間ベストセラーTOP10(日販調べ)','日本の行政機関'
] # 出題カテゴリ
cate_num = 0 # 選択されたカテゴリ
num = 0 # 問題番号
s = '' # 取得したWiki本文
btn=None # 解答ボタン
s_btn=None # スタートボタン
combo=None # 回答選択欄
start_time='' # タイマー用
l_result=None # メッセージ文
re_btn=None # もう一度遊ぶボタン
rank_btn=None # Rankingに登録ボタン
crear_time=0 # クリア時間

# 正誤判定を表示
def clear_result():
    global l_result
    l_result['text']=''

# Wiki本文から問題文を生成し表示
def creat_que():
    global num,r,s,answers,combo,start_time,l_result,cate_num
    que.delete(0.,tk.END)
    combo.delete(0, last=None)
    num = random.randint(0,len(answers[cate_num])-1) # ランダムに正答を決定
    s = wikipedia.page(answers[cate_num][num]).content # Wiki本文を取得
    target = 'は、' # 概要の冒頭を削除（読み仮名や英名などを削除）
    idx = s.find(target)
    r = s[idx+2:]
    ans_word = str(answers[cate_num][num])
    if ans_word.endswith(' (東京都)'):
        ans_word.replace(' (東京都)','')
    if ans_word.endswith(' (音楽グループ)'):
        ans_word.replace(' (音楽グループ)','')
    if ans_word.endswith(' (漫画)'):
        ans_word.replace(' (漫画)','')
    r = r.replace(ans_word,'☆☆') # 本文中に解答が入っていれば消去
    if cate_num==0:
        r = r.replace(ans_word[:-1],'☆☆') # 本文中に解答-1文字が入っていれば消去(〇〇駅や〇〇県を消す用)
    que.insert(0.,r)   

# 「答える」ボタンの挙動
def btn_click():
    global correct,num,r,answers,l_result,btn,re_btn,index,cate_num,rank_btn,clear_time
    user_ans=combo.get()
    if user_ans==answers[cate_num][num]:
        correct+=1
        msg='正解!'
        creat_que()
        root.after(1500,clear_result)
    else:
        msg='不正解'
        root.after(1500,clear_result)
    if correct==5:
        clear_time = int(time.time() - start_time)
        clear_minute = clear_time // 60
        clear_second = (clear_time % 3600 % 60)
        #msg+=f'お疲れさまでした! \n今回のタイムは{clear_minute}分{clear_second}秒でした'
        que.delete(0.,tk.END)
        que.insert(1.0,f'お疲れさまでした! \n今回のタイムは{clear_minute}分{clear_second}秒でした')
        btn.destroy()
        combo.destroy()
        index=2
        re_btn=tk.Button(text='もう一度あそぶ',font=('メイリオ',14,'bold'),fg='blue',bg='powderblue',command=game_main)
        re_btn.pack()
        rank_btn=tk.Button(text='ランキングに登録',font=('メイリオ',14,'bold'),fg='gold',bg='lemonchiffon',command=rank_entry)
        rank_btn.pack()

    l_result['text']=msg
    root.after(1500,clear_result)

# 「ランキングに登録」ボタン
def rank_entry():
    global cate_num,cate,clear_time,rank_window,clear_time_str,entry_name
    messagebox.showinfo('お詫び','この機能は仮実装です')
    # 登録画面表示
    rank_window = tk.Toplevel(root)
    # 親ウィンドウを非アクティブに
    rank_window.grab_set()
    # 登録画面をアクティブに
    rank_window.focus_set()
    label1=tk.Label(rank_window,text='ランキングに登録',font=('Arial',12),anchor=tk.CENTER)
    label1.grid(row=0,column=0,columnspan=2)
    label_name=tk.Label(rank_window,text='Player Name',font=('Arial',12,'bold'),anchor=tk.CENTER)
    label_name.grid(row=1,column=0)
    entry_name=tk.Entry(rank_window,font=('Arial',12),justify="center",width=32)
    entry_name.insert(tk.END,'16文字以内で入力')
    entry_name.grid(row=1,column=1)
    entry_name.focus_set()
    label_category=tk.Label(rank_window,text='Category',font=('Arial',12,'bold'),anchor=tk.CENTER)
    label_category.grid(row=2,column=0)
    entry_category=tk.Label(rank_window,text=f'{cate[cate_num]}',font=('Arial',12),justify="center")
    entry_category.grid(row=2,column=1)
    label_time=tk.Label(rank_window,text='Time',font=('Arial',12,'bold'),anchor=tk.CENTER)
    label_time.grid(row=3,column=0)
    clear_time_str=f'{clear_time // 60}分{(clear_time % 3600 % 60)}秒'
    entry_time=tk.Label(rank_window,text=clear_time_str,font=('Arial',12),justify="center")
    entry_time.grid(row=3,column=1)
    entry_btn=tk.Button(rank_window,text='登録',font=('メイリオ',14,'bold'),fg='gold',bg='lemonchiffon',command=rank_entry_btn)
    entry_btn.grid(row=4,column=0,columnspan=2)

def rank_entry_btn():
    global rank_window,entry_name,cate_num,clear_time_str
    rank_dao.insert_one(rank_dao.Ranking(entry_name.get(),cate_num,clear_time_str))
    ok=messagebox.showinfo(title="ランキング登録", message="登録が完了しました")
    if ok=='ok':
        rank_window.destroy()
        game_main()

def ranking():
    global cate
    messagebox.showinfo('お詫び','この機能は仮実装です')
    # 登録画面表示
    show_rank = tk.Toplevel(root)
    # 親ウィンドウを非アクティブに
    show_rank.grab_set()
    # 登録画面をアクティブに
    show_rank.focus_set()
    rank_data=rank_dao.find_all()
    rank_label=tk.Label(show_rank,text='ランキング',font=('メイリオ',12,'bold'),anchor=tk.CENTER)
    #rank_label.grid(row=0,column=0,columnspan=0)
    rank_num=0
    label_header=tk.Label(show_rank,text='Rank',font=('Arial',12,'bold'),anchor=tk.CENTER,fg='white',bg='seagreen')
    label_header.grid(row=1,column=0)
    label_header_name=tk.Label(show_rank,text='Player Name',font=('Arial',12,'bold'),anchor=tk.CENTER,width=32,fg='white',bg='seagreen')
    label_header_name.grid(row=1,column=1)
    label_header_category=tk.Label(show_rank,text='Category',font=('Arial',12,'bold'),anchor=tk.CENTER,width=40,fg='white',bg='seagreen')
    label_header_category.grid(row=1,column=2)
    label_header_clearTime=tk.Label(show_rank,text='Clear Time',font=('Arial',12,'bold'),anchor=tk.CENTER,fg='white',bg='seagreen')
    label_header_clearTime.grid(row=1,column=3)
    label_header_date=tk.Label(show_rank,text='Entry Date',font=('Arial',12,'bold'),anchor=tk.CENTER,width=20,fg='white',bg='seagreen')
    label_header_date.grid(row=1,column=4)
    for data in rank_data:
        rank_num+=1
        label_rank=tk.Label(show_rank,text=f'{rank_num}',font=('Arial',12),anchor=tk.CENTER)
        label_rank.grid(row=rank_num+1,column=0)
        label_name=tk.Label(show_rank,text=f'{data.player_name}',font=('Arial',12),anchor=tk.CENTER,width=32)
        label_name.grid(row=rank_num+1,column=1)
        label_cate=tk.Label(show_rank,text=f'{cate[data.category][:30]}{"..." if len(cate[data.category])>30 else ""}',font=('Arial',12),anchor=tk.CENTER,width=40)
        label_cate.grid(row=rank_num+1,column=2)
        label_time=tk.Label(show_rank,text=f'{data.clear_time}',font=('Arial',12),anchor=tk.CENTER)
        label_time.grid(row=rank_num+1,column=3)
        label_date=tk.Label(show_rank,text=f'{data.updated}',font=('Arial',12),anchor=tk.CENTER,width=20)
        label_date.grid(row=rank_num+1,column=4)

# スタート画面
def game_main():
    global correct,r,index,answers,num,s_btn,re_btn,rank_btn,r_btn
    if index==2:
        que.delete(0.,tk.END)
        re_btn.destroy()
        rank_btn.destroy()
        l_result.destroy()
    index=0
    correct=0
    que.insert(1.0,"WikiQuizは、Wikpediaの本文だけをみて、ページタイトルを当てるクイズです。\n\n\n本文中に、解答と全く同じ文字列が含まれる場合は「☆☆☆」に置き換わりますが、漢字/ひらがな/カタカナ/ローマ字など表記が異なる場合は置き換わりません。\n\nまた、画像や図は表示されません。\n語句によては、リダイレクト先の記事や一覧記事が表示される場合もあります。\n\nタイトルを特定できる情報を素早く見つけて正しい答えを選択し、5問正解したらクリアです\n\n\n準備ができたら、出題カテゴリを選択し【スタート】ボタンをクリックしてください。")
    s_btn=tk.Button(text='スタート',font=('メイリオ',14,'bold'),fg='red',bg='mistyrose',command=game_start)
    s_btn.pack()
    r_btn=tk.Button(text='ランキング',font=('メイリオ',14,'bold'),fg='gold',bg='lemonchiffon',command=ranking)
    r_btn.pack()

# クイズ中の画面表示物を生成+タイマースタート
def game_start():
    global correct,r,index,answers,num,s,s_btn,start_time,combo,l_result,btn,category_combo,cate_num,r_btn
    index = 1
    correct=0
    s_btn.destroy()
    r_btn.destroy()
    cate_num=category_combo.current()
    que.insert(1.0,r)
    combo=ttk.Combobox(root,values=answers[cate_num],font=('HGｺﾞｼｯｸM',12),justify="center",state="readonly",width=40)
    combo.set("答えを選択")
    combo.pack()
    btn=tk.Button(text='答える',font=('メイリオ',14,'bold'),fg='red',bg='mistyrose',command=btn_click)
    btn.pack()
    l_result=tk.Label(text='',font=('Arial',20))
    l_result.pack()
    creat_que()
    start_time = time.time()


fnt=('Arial',30)
title=tk.Label(text='WikiQuiz',font=fnt)
title.pack(side=tk.TOP)
frame1 = tk.Frame(root)
frame1.pack(anchor=tk.CENTER)
category=tk.Label(frame1,text='出題カテゴリ：',font=('メイリオ',12))
category.pack(side=tk.LEFT)
category_combo=ttk.Combobox(frame1,values=cate,font=('Arial',12),justify="center",state="readonly",width=50)
category_combo.current(0)
category_combo.pack(side=tk.LEFT)
que = tk.Text(background='lightblue')
que.pack(fill=tk.BOTH)
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