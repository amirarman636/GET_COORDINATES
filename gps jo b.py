import os
import cv2
L = []
image = cv2.imread("111.jpeg")
def timer():
    t = 0

    # t = t + 1
    while True:
            cv2.imshow("gps is on",image)     
            os.system("adb shell dumpsys location > meminfo%ds.txt")

# os.system("nc -q 2 20175 50000> meminfo.txt")
            our_file = open("meminfo%ds.txt")  
            f = open("attempts.txt","w+")
            lines_to_read = [52]
            for position, line in enumerate(our_file):
                if position in lines_to_read:
                    L.append([t,line])
                    # print(line)
            print(L[t])
            t = t + 1
    # os.system("adb shell dumpsys location > meminfo %d s.txt")
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    cv2.destroyAllWindows()
                    
timer()