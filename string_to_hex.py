import sys
import json
import re

ROW = 11

def string_to_hex():
    if len(sys.argv) != 2:
        print("コマンドは以下のようににしてください")
        print("python string_to_hex.py 文字列")
        exit()

    #jsonファイル読み込み
    f = open('./char.json')
    data = json.load(f)
    f.close()

    #2進数を入れるファイル 縦11px分 横は空文字で初期化
    out = [''] * 11

    for char in sys.argv[1]:
        print(char)
        for j in range(len(data[char])):
            out[j] += data[char][j][0:10]

    #ドット絵出力　長さがバイト単位じゃないかも
    for l in out:
        print(l)
    print(len(out[0]))

    #1byteで割り切れるように0埋め
    size = len(out[0])
    if len(out[0]) % 8 != 0:
        for i in range(len(out)):
            out[i] += '0'*(8 - (size % 8))

    #ドット絵出力　長さはバイト単位
    for l in out:
        print(l)
    print(len(out[0]))

    #1byteごとに反転して書き出し
    with open('./out.txt', mode='w') as f:
        for i in range(11):
            for j in range(len(out[0]) // 8):
                s = out[i][(0 + 8*j):(8 + 8*j)]
                s = s[::-1]
                #print('0x{:02x}'.format(int(s, 2)))
                x = '0x{:02x}'.format(int(s, 2))
                f.write(x + ',')
            f.write('\n')

if __name__ == '__main__':
    string_to_hex()