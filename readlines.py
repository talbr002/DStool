import os
import re
import traceback
import sys
import time

DURATION = 600

#sys.setdefaultencoding('utf8')
x = r'C:\\'
alist = ["destruction", "copyright", "export"]
startTime = round(time.time())
endTime = round(time.time() + DURATION)
for root, dirs, files in os.walk(x):
##    print('This is the root: {} '.format(root))
    if (round(time.time()) >= endTime):
        break
    for file in files:
        try:
            f = open((os.path.join(root,file)), 'r', encoding="latin-1")
            for num, line in enumerate(f, 1):
                for item in alist:
                    pattern = re.compile(item)
                    match = pattern.search(line.lower())
                    if match:
                        print("match found for {}".format(item))
                        print("location = {}".format(os.path.join(root, file)))
                        print(line.strip())
                        print(num)
                        print("\n")
        except:
            print("Unexpected error:", sys.exc_info()[0])
            print("location = {}".format( os.path.join(root, file) ))
            
            

