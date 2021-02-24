import json
import re

#jiscodeの実際の値をjson化
def jis_json():

    f = open('../out.json')
    data = json.load(f)
    f.close()

    out = {}
    with open('./injis.txt', 'r') as f:
        txt_data = f.readlines()
        cnt = 0
        for i in range(len(txt_data)):
            #print(txt_data[i])
            if txt_data[i] == '\n':
                continue
            jiscode = "0x" + txt_data[i].split(',')[2]
            char = txt_data[i].split(',')[7].rstrip()
            
            try:
                out[char] = data[jiscode]
            except KeyError:
                pass
    
    #jsonの書き出し
    with open('out2.json', mode='wt', encoding='utf-8') as file:
        json.dump(out, file, ensure_ascii=False, indent=2)
            

if __name__ == '__main__':
    jis_json()