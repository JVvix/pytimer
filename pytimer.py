import time

seconds = int(input("how many seconds you want to wait?"))

for i in range(seconds):
    if seconds == 1:
        print(str(seconds - i) + "second remaining")
    else:
        print(str(seconds - i) + "seconds remaining")
    time.sleep(1)
