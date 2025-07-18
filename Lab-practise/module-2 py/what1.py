import pywhatkit
import time

number="=+919586884895"
msg="good evening"
repeats=5
for i in range(repeats):
    try:
        pywhatkit.sendwhatmsg_instantly(number,msg,wait_time=10,tab_close=True)
        print(f"sent msg{i+1}")
        time.sleep(15)
    except Exception as e:
        print(f"failed at message{i+1}due to:{e}")
        time.sleep(5)