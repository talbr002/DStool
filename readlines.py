import os
import re
import traceback
import sys
import time

DURATION = 60

output = open("OF.txt", 'w')
output.close()
x = r'C:\\'
alist = ["copyright", "export", "destruction"]
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
                        output = open("OF.txt", 'a+', encoding="latin-1")
                        output.seek(0, 2)
                        output.write("\n\nmatch found for {}\n".format(item))
                        output.write("location = {}\n\n".format(os.path.join(root, file)))
                        output.write("index location = {}\n".format(match.endpos))
                        output.write("line length = {}\n".format(len(line)))
                        if ((match.start()) > 50) & (len(line) > (match.end() + 50)):
                            output.write(line[(match.start() - 50):(match.end()+ 50)])
                        else:
                            output.write(line.strip())

                        output.write("\n\nline number = {}\n".format(num))
##                        print("match found for {}".format(item))
##                        print("location = {}".format(os.path.join(root, file)))
##                        print(line.strip())
##                        print("line number = {}".format(num))
##                        print("\n")
        except:
            print("Unexpected error:", sys.exc_info()[0])
            print("location = {}".format( os.path.join(root, file) ))
            
            

