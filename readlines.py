import os
import re
import traceback
import sys

sys.setdefaultencoding('utf8')
x = 'C:\\'
alist = ["destruction", "copyright", "export"]
for root, dirs, files in os.walk(x):
    for file in files:
        try:
            f = open((os.path.join(root,file)), 'r')
            for num, line in enumerate(f, 1):
                for item in alist:
                    pattern = re.compile(item)
                    match = pattern.search(line.lower())
                    if match:
                        print("match found for {}".format(item))
                        print("location = {}".format( os.path.join(root, file) ))
                        print(line.strip())
                        print(num)
                        print("\n")
        except:
            print("Unexpected error:", sys.exc_info()[0])
            print("location = {}".format( os.path.join(root, file) ))
            
            

