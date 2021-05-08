#!/usr/bin/python3
import socket as soc

import threading as thread
import os
import subprocess

your_ip = subprocess.getoutput("hostname -i")
your_port = 12345
# TO CREATE A SOCKET AND BIND IP AND PORT NUMBER :

skt2 = soc.socket(soc.AF_INET, soc.SOCK_DGRAM)
skt2.bind((your_ip, your_port))


# WE CAN USE THIS FUNCTION TO RECIEVING AND PRINTING THE MESSAGE :

def recieve_msg():
    while True:
        os.system("tput setaf 2")
        msgRcv = skt2.recvfrom(1024)
        if msgRcv[0].decode() == "quit" or msgRcv[0].decode() == "bye bye" or msgRcv[0].decode() == "exit":
            print("NOW YOUR FRIEND GOES OFFLINE.....")
            os._exit(1)
        print("\n\t\t\t The values from device is as follow: --->" + msgRcv[0].decode())
        xy =  msgRcv[0].decode()
        subprocess.getoutput("echo {} >> new.txt".format(xy))




# WE CAN USE THIS THREAD FOR RECIVING THE MESSAGE FUNCTION :

t4 = thread.Thread(target=recieve_msg)

# WE CAN USE THIS FUNCTION TO STARTING OUR THREADS :

t4.start()
