import os
import cv2
L = []
import re
errors = []

def timer():
    t = 0
    linenum = 0

    # t = t + 1
    while True:
        os.system("adb shell dumpsys location Last Known Locations> meminfo%ds.txt")

        pattern = re.compile("Last Known Locations:", re.IGNORECASE)  # Compile a case-insensitive regex
        our_file = open("meminfo%ds.txt")  
        with open ('meminfo%ds.txt', 'rt') as myfile:    
            for line in myfile:
                linenum += 1
                if pattern.search(line) != None:      # If a match is found 
                    errors.append((linenum, line.rstrip('\n')))
                for err in errors:          
                    
            # f = open("attempts.txt","w+")
                    lines_to_read = [err[0] + 1]
                    for position, line in enumerate(our_file):
                        if position in lines_to_read:
                            L.append([t,line])# Iterate over the list of tuples
                            print(line)
                    # print("Line " + str(err[0]) + ": " + err[1])
            image = cv2.imread("111.jpeg")  
            cv2.imshow("gps is on",image)     

# os.system("nc -q 2 20175 50000> meminfo.txt")
            
                    
            # print(L[t])
            t = t + 1
    # os.system("adb shell dumpsys location > meminfo %d s.txt")
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    cv2.destroyAllWindows()
                    
timer()