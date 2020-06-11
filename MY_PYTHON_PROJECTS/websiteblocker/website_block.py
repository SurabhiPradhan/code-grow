import time
from datetime import datetime as dat

hostp = "hosts"
host_path="/etc/hosts"
redirect = "127.0.0.1"
websites = ["www.facebook.com", "facebook.com", "www.primevideo.com", "primevideo.com"]

while True:
    #creating datetime object
    if dat(dat.now().year, dat.now().month, dat.now().day, 8) < dat.now() < dat(dat.now().year, dat.now().month, dat.now().day, 17,15):
        print("Study hours.....")
        with open(host_path,'r+') as file:
            info = file.read()
            for website in websites:
                if website in info:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")

    else:
        with open(host_path,'r+') as file:
            info = file.readlines()
            file.seek(0)
            for line in info:
                if not any(website in line for website in websites):
                    file.write(line)
            # deletes the content of the file from current point and downwards
            file.truncate()
        print("Time to relax..")


    time.sleep(5)
