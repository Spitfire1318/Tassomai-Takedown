from time import time
from os import system
from validate_email import validate_email
import funcs
def main(func=False, email = ''):
    if func == False:
        email = input("Email: ")
        input("Press any button to start!")
    if (validate_email(email) != True):
        raise Exception("Email is not valid!")
    start_time = time()
    b = funcs.openfile("dict.txt", "r+")
    new_b = b.readlines()
    linenum = 0
    tries = 0
    for line in new_b:
        linenum += 1
        line = line.strip()
        checked = funcs.check(line,email)
        tries +=1
        if func == False:
            print ("num: " + str(linenum) + " " + line + " Time: " + str(checked[1]))
        if checked[0]:
            if func == False:
                funcs.found(line, time(), start_time, tries) 
            else:
                return (line, float(time()-start_time), tries)
            break     
if __name__ == "__main__":
    main()

        
