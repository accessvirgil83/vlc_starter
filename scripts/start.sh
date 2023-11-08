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
chmod +x ~/script.py
termux-job-scheduler --period-ms 18000000 -s ~/script.py
 
