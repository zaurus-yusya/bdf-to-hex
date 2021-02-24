import json
import re

ROW = 11

def make_bin():
    #jsonファイル読み込み
    f = open('./out.json')
    data = json.load(f)
    f.close()

    #2進数を入れるファイル 縦11px分 横は空文字で初期化
    out = [''] * 11
    print(out)

    with open('./in.txt', 'r') as f:
        txt_data = f.readlines()
        for i in range(len(txt_data)):
            print(txt_data[i])
            jisCode = txt_data[i].rstrip()

            for j in range(len(data[jisCode])):
                print(data[jisCode][j][0:10])
                out[j] += data[jisCode][j][0:10]

    for l in out:
        print(l)

    #1byteで割り切れるように0埋め
    print(len(out[0]))
    size = len(out[0])
    if len(out[0]) % 8 != 0:
        for i in range(len(out)):
            out[i] += '0'*(8 - (size % 8))
    
    print(len(out[0]))
    for l in out:
        print(l)


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
    make_bin()