#!/usr/bin/env python3
# - coding: utf-8 -
#
# ビット・トレード・ワン絶縁入力HATサンプルプログラム
# 　著作権者:(C) 2022 ビット・トレード・ワン社
# 　ライセンス: ADL(Assembly Desk License)
#
#  実行方法： python3 sample.py
#  機能　　：4つの入力ポートのON/OFF状態を1秒毎に表示

import RPi.GPIO as GPIO
import time

# Raspberry pi GPIO setting
DI1 = 5
DI2 = 6
DI3 = 16
DI4 = 26

# GPIO setup
def setupGPIO() :
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(DI1, GPIO.IN)
    GPIO.setup(DI2, GPIO.IN)
    GPIO.setup(DI3, GPIO.IN)
    GPIO.setup(DI4, GPIO.IN)

# GPIO read
def readGPIO() :
    di1 = GPIO.input(DI1)
    di2 = GPIO.input(DI2)
    di3 = GPIO.input(DI3)
    di4 = GPIO.input(DI4)
    return di1, di2, di3, di4

# main
if __name__ == "__main__":

    setupGPIO()
    while True:
        result = readGPIO()
        print ('DI0:', result[0], ',', 'DI1:', result[1], ',', 'DI2:', result[2], ',', 'DI3:', result[3])
        time.sleep(1)
