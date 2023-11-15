#!/bin/bash 

pkg update
pkg upgrade
echo 'Пакеты обновлены!'
echo 'Устанавливаем python!'
pkg install python3
echo 'Установка pip'
pkg install python3-pip
pip install plyer
pkg install termux-api
chmod +x ~/vlc_starter/scripts/script.py
termux-job-scheduler --period-ms 180000 -s ~/vlc_starter/scripts/script.py
cat "python ~/vlc_starter/scripts/script.py" >> ~/.bashrc
 
