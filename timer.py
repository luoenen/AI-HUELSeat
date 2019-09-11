import time


def timer_setting():
    while True:
        now = time.localtime()
        year = now.tm_year
        month = now.tm_mon
        day = now.tm_mday
        hour = now.tm_hour
        my_time = str(year) + '-' + str(month) + '-' + str(day) + '-' + str(hour) + '-50' + '-00'
        goal = time.strptime(my_time, '%Y-%m-%d-%H-%M-%S')
        if now >= goal:

            return True
        else:
            goal = time.mktime(time.strptime(my_time, '%Y-%m-%d-%H-%M-%S'))
            print("目标时间：北京时间19:50分\t" + "预计等待：" + str(int(int(goal) - int(time.time()))) + "秒")
            time.sleep(0.1)

            #正式注释
            return True