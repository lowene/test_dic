import csv

dic = "dictlist-50.txt" #連想概念辞書を入れる
#連想概念辞書の文字コードを変換
with open('dictlist-50.txt', encoding='cp932') as f_in:
    with open('dictlist.txt', 'w', encoding='UTF-8') as f_out:
        f_out.write(f_in.read())
#入力された刺激語を連想概念辞書で検索、連想語をすべて出力

Noun = input('名詞 : ')#換喩の名詞を入力から受け取る
Verb = input('用言 : ')#換喩の用言を入力から受け取る
subject = ["上位概念","下位概念","部分・材料概念","属性概念","類義概念","動作概念","環境概念","関連語"]
assoN = [[0 for i in range(0)] for j in range(0)]
assoV = [[0 for i in range(0)] for j in range(0)]
with open('test2.txt',"r",encoding="UTF-8",newline="") as f:
    reader = csv.DictReader(f,delimiter="\t")
    for r in reader:
        if(r["刺激語"]==Noun):
            assoN.append([[Noun,r["距離"]]])
        if(r["刺激語"]==Verb):
            assoV.append([[Verb,r["距離"]]])
    print(assoN[0][0])
            
"""
    for i in range(len(assoN)):
        for j in range(len(a))
"""
"""
with open('dictlist.txt',"r",encoding="UTF-8",newline="") as f:
    reader = csv.DictReader(f,delimiter="\t")
    for r in reader:
        if(r["刺激語"]==shigekigo):
            print("\n")
            print("連想関係：" + subject[int(r['連想関係'])-1] )
            print("連想語：" + r['連想語'] )
            print("時間：" + r['時間'] )
            print("順位：" + r['順位'] )
            print("頻度：" + r['頻度'] )
            print("距離：" + r['距離'] )
"""
