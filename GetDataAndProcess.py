import os
import requests
import re
import cv2
import numpy as np

import queue




def main():
    dir_path = "./From"
    #파일들의 정보가 저장된 리스트를 만들때 사용한다.
    #fileDic = create_directory_dict(dir_path)
    #해당 파일들을 파싱해서 변경해야할 이름들을 불러온다

    dir_path = "./GER.txt"
    file = open(dir_path)
    leaders = processTextToData(file)

    #for key, value in leaders.items():
        #print(key, value)

    print("end")


def processTextToData(text):
    nameImageDic = {}
    nameIdeologyDic = {} 
    line = text.readline()
    count = 20
    q = queue.Queue()
    currentNameFirst = ""
    currentNameSecond = ""
    currentFileName = ""
    currentIdeology = ""
    formerNum = 0
    formerLine = ""
    while line and q.empty  :
        if(formerNum < q.qsize()):
            formerNum = q.qsize()
        elif formerNum > q.qsize():
            if(q.qsize() ==1):
                currentNameFirst = ""
                currentNameSecond = ""
                currentFileName = ""
                currentIdeology = ""
                #print("end")
            formerNum = q.qsize()
        if '{' in line :
            q.put("a")
        if '}' in line:
            q.get()
        
        if 'name' in line :

            first_last = line.split("=") # 스페이스를 기준으로 문자열을 나눔
            first_last_str = first_last[1] # 나눈 문자열을 조합하여 필요한 부분만 추출
            if '/' in  first_last_str:
                first_both = first_last_str.split("/") # 스페이스를 기준으로 문자열을 나눔
                currentNameFirst = first_both[0]+"\""
                currentNameSecond = "\""+first_both[1]
                print(currentNameFirst , "+",currentNameSecond)
                nameImageDic[currentNameFirst] = ""
                nameIdeologyDic[currentNameFirst] = ""

            else:
                currentNameFirst = first_last_str
                nameImageDic[currentNameFirst] = ""
                nameIdeologyDic[currentNameFirst] = ""
                print(currentNameFirst , "+",currentNameSecond)
                
        elif 'ideology' in line :
            first_last = line.split("=") # 스페이스를 기준으로 문자열을 나눔
            first_last_str = first_last[1] # 나눈 문자열을 조합하여 필요한 부분만 추출
            currentIdeology = first_last_str
            nameIdeologyDic[currentNameFirst] = currentIdeology
            if currentNameSecond != "":
                nameIdeologyDic[currentNameSecond] = currentIdeology
                #print(currentNameSecond, currentIdeology)    
                
            #print(currentNameFirst, currentIdeology)    
        elif("gfx/leaders" in line and "civilian" in formerLine ):
            first_last = line.split("=") # 스페이스를 기준으로 문자열을 나눔
            first_last_str = first_last[1] # 나눈 문자열을 조합하여 필요한 부분만 추출
            currentFileName = first_last_str
            nameImageDic[currentNameFirst] = currentFileName
            #print(currentNameFirst, currentFileName)
        formerLine = line 
        line = text.readline()




    directory_dict = {}
    for key,value in nameImageDic.items():
        if value =="" or nameIdeologyDic[key] == "":
            continue
        directory_dict[nameIdeologyDic[key]] = value



    return directory_dict


def create_directory_dict(directory):
    directory_dict = {}
    for root, dirs, files in os.walk(directory):
        for dir in dirs:
            directory_dict[dir] = []
            for file in os.listdir(os.path.join(root, dir)):
                if os.path.isfile(os.path.join(root, dir, file)):
                    directory_dict[dir].append(file)
    return directory_dict





def ProcessRemoveBG(targetfile):
    end_path = "./To"
    targetfile = ""; 
    response = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        files={'image_file': open( targetfile, 'rb')},
        data={'size': 'auto'},
        headers={'X-Api-Key': 'CRDUHz4d3KDDwu7YD3uimrzE'},
    )

    if response.status_code == requests.codes.ok:
        with open('no-bg.png', 'wb') as out:
            out.write(response.content)
    else:
        print("Error:", response.status_code, response.text)


if __name__ == "__main__":
    main()
