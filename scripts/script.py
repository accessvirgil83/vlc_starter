import subprocess
import webbrowser
from plyer import uniqueid, notification

def launch_vlc_rtsp_stream(rtsp_url):
# Запуск VLC плеера с RTSP потоком на Android
    package_name = 'org.videolan.vlc'
    intent_uri = rtsp_url
    vlc_command = f'am start -n {package_name}/{package_name}.gui.video.VideoPlayerActivity -d {intent_uri}'
    subprocess.Popen(vlc_command, shell=True)
# Открытие браузера с адресом RTSP потока
    webbrowser.open(rtsp_url)

if __name__ == "__main__":
    rtsp_url = "Udp://@238.0.0.2:1234" # Замените на ваш RTSP поток
    launch_vlc_rtsp_stream(rtsp_url)
