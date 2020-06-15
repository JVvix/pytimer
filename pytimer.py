import time

seconds = int(input("how many seconds you want to wait? "))

for i in range(seconds):
    print(str(seconds - i) + " seconds remaining ")
    time.sleep(1)

print("Time is up!")
