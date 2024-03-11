import time

# 设置工作时间和休息时间(以秒为单位)
work_duration = 25 * 60  # 25分钟
break_duration = 5 * 60  # 5分钟

while True:
    print("开始工作!")
    start_time = time.time()
    end_time = start_time + work_duration

    while time.time() < end_time:
        remaining_time = end_time - time.time()
        mins, secs = divmod(remaining_time, 60)
        timer = '{:02d}:{:02d}'.format(int(mins), int(secs))
        print(timer, end="\r")
        time.sleep(1)

    print("工作时间到!休息一下吧。")

    start_time = time.time()
    end_time = start_time + break_duration

    while time.time() < end_time:
        remaining_time = end_time - time.time()
        mins, secs = divmod(remaining_time, 60)
        timer = '{:02d}:{:02d}'.format(int(mins), int(secs))
        print(timer, end="\r")
        time.sleep(1)

    print("休息时间到!继续工作吧。")
