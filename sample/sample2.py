#!/usr/bin/env python3
# - coding: utf-8 -
#
# ビット・トレード・ワンADRSINS絶縁入力HATサンプルプログラム
# 　著作権者:(C) 2024 ビット・トレード・ワン社
# 　ライセンス: ADL(Assembly Desk License)
#
#  実行方法： python3 sample.py
#  機能　　：4つの入力ポートのON/OFF状態を1秒毎に表示

from gpiozero import Button
from time import sleep

# Raspberry Pi GPIO setting
DI1 = 5
DI2 = 6
DI3 = 16
DI4 = 26

# GPIO setup
def setupGPIO():
    global di1, di2, di3, di4
    di1 = Button(DI1)
    di2 = Button(DI2)
    di3 = Button(DI3)
    di4 = Button(DI4)

# GPIO read
def readGPIO():
    return di1.is_pressed, di2.is_pressed, di3.is_pressed, di4.is_pressed

# main
if __name__ == "__main__":

    setupGPIO()
    while True:
        result = readGPIO()
        print('DI1:', result[0], ',', 'DI2:', result[1], ',', 'DI3:', result[2], ',', 'DI4:', result[3])
        sleep(1)
