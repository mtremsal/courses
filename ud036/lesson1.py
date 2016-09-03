# Lesson 1
import webbrowser
import time

n = 0
while n<3:
    print("Time is: {}".format(time.ctime()))
    time.sleep(10)
    webbrowser.open("test.com")
    print("test.com")
    n += 1
