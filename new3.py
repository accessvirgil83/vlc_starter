import subprocess
import webbrowser
import signal
import time

vlc_process = None

def launch_vlc_rtsp_stream(rtsp_url, timer):
	global vlc_process
	# Запуск VLC плеера с RTSP потоком на Android
	package_name = 'org.videolan.vlc'
	intent_uri = rtsp_url
	vlc_command = f'am start -n {package_name}/{package_name}.gui.video.VideoPlayerActivity -d {intent_uri}'
	vlc_process = subprocess.Popen(vlc_command, shell=True)	
	# Открытие браузера с адресом RTSP потока
	webbrowser.open(rtsp_url)

# Установка таймера на выход из процесса
def exit_process(signum, frame):
	global vlc_process
	vlc_process.terminate()
	time.sleep(1)
	vlc_process.kill()
	signal.signal(signal.SIGALRM, exit_process)
	signal.alarm(timer)

if __name__ == "__main__":
	rtsp_url = "http://honjin1.miemasu.net/nphMotionJpeg?Resolution=640x480&Quality=Standard" # Замените на ваш RTSP поток
	timer = 60 # Таймер в секундах
	launch_vlc_rtsp_stream(rtsp_url, timer)