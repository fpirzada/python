import time
for timer in range(600):
    min = 0
    if timer < 10:
        print(str(min) + " : 0" + str(timer))
    elif timer < 60:
        print(str(min) + " : " + str(timer))
    elif timer == 60 or timer == 120 or timer == 180 or timer == 240 or timer == 300 or timer == 360 or timer == 420 or timer == 480 or timer == 540 or timer == 600:
        min += 1
    elif timer > 60:
        print(str(min) + " : " + str(timer))
    # print(timer)


    time.sleep(1)