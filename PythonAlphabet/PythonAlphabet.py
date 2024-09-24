# 入力されたアルファベットの順番を出力するプログラム

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

a = input("アルファベットの大文字を1文字入力してください")

if a in alphabet:
  print(alphabet.index(a) + 1)
else:
  print("入力されたのはアルファベットの大文字ではありません！！")
