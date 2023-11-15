import schedule
import time
import os

def job():
	os.system("python vlc_starter/scripts/script.py")
    print("Работаю")

schedule.every().day.at("12:30").do(job)
schedule.every().hour.do(job)
# нужно иметь свой цикл для запуска планировщика с периодом в 1 секунду:
while True:
    schedule.run_pending()
    time.sleep(1)
