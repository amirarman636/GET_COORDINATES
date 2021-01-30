# GET_COORDINATES

I used an android phone and a python script and by using adb package in ubuntu and connecting the phone to any sat service like google
1_First we should available developer mode on cellphone
2_Open any navigation service you want
3_Install adb package in your pc
4_See if pc connected to pc properly by entering adb devices in terminal
5_Remember to load an image by cv2.imread shortest way too break out of while
6_The text file that saved in you dic is the location history and of cource live if you opened any map srvc on your phone that i named meminfo%ds.txt
7_Find the line of that txt file i said which can be easily found by searching srvc we'r using and there is lat and alt and some other stuff about coordinate somthing like 
[90, '    passive: Location[gps 35.797883,51.396456 hAcc=13 et=+1d2h50m40s273ms alt=1681.94384765625 vel=0.0 vAcc=8 sAcc=1 bAcc=??? {Bundle[{satellites=9, maxCn0=29, noGPSLocation=Location[network 35.797687,51.396567 hAcc=13 et=+1d2h50m39s366ms alt=1674.4000244140625 vAcc=3 sAcc=??? bAcc=??? {Bundle[{networkLocationType=wifi}]}], meanCn0=20}]}]\n']
Which is coordinates we want .
Run the code its ready !
