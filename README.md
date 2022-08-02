# ADRSINS-RaspberryPi-insulation
### ラズベリーパイ絶縁入力HAT
![タイトル画像のURLを右のカッコに]()

ラズベリーパイに5~24Vの信号を入力できるADRSINSのページです。  

## [HPリンク](http://bit-trade-one.co.jp/) 

### [サンプルプログラムの実行方法](#サンプルプログラムの実行方法)  

### [サンプルコード](https://github.com/bit-trade-one/-ADXXXXX-Template/raw/master/Sample)  

### [Q&A](FAQ.md)

### [基板図](https://github.com/bit-trade-one/-ADXXXXX-Template/blob/master/Dimensions/-ADXXXXX-Template-Dimensions.pdf)

### [回路図](https://github.com/bit-trade-one/-ADXXXXX-Templateo/blob/master/Schematics/-ADXXXXX-Template-Schematics.pdf)

---

# サンプルプログラムの実行方法


## ライブラリ関連のインストール

```
$ sudo apt-get update
$ sudo apt-get install -y python-dev
$ sudo apt-get install -y python-pip
$ sudo pip install RPi.GPIO

```

## サンプルソフトをダウンロード

```
$ git clone https://github.com/bit-trade-one/ADRSINS-RaspberryPi-insulation.git
```

## 使用方法
sample.pyを起動すると、1秒周期でDI0～DI3の4つの接点の入力を1秒周期で実施します。  
接点がHighレベル（5V～24V)の場合、GPIOの値は'0'になり、Lowレベルの場合は'1'となります。  
終了する場合は「Ctrl」＋「C」を押下してください。  

```
$ python3 sample.py
DI0: 1 , DI1: 1 , DI2: 1 , DI3: 1
DI0: 1 , DI1: 1 , DI2: 1 , DI3: 1
DI0: 1 , DI1: 1 , DI2: 1 , DI3: 1
DI0: 0 , DI1: 1 , DI2: 1 , DI3: 1
DI0: 1 , DI1: 1 , DI2: 1 , DI3: 1
DI0: 1 , DI1: 0 , DI2: 1 , DI3: 1
DI0: 1 , DI1: 0 , DI2: 1 , DI3: 1
DI0: 1 , DI1: 1 , DI2: 0 , DI3: 1
DI0: 1 , DI1: 1 , DI2: 0 , DI3: 1
DI0: 1 , DI1: 1 , DI2: 1 , DI3: 1
DI0: 1 , DI1: 1 , DI2: 1 , DI3: 0
DI0: 1 , DI1: 1 , DI2: 1 , DI3: 1
DI0: 1 , DI1: 1 , DI2: 1 , DI3: 1
DI0: 1 , DI1: 1 , DI2: 1 , DI3: 1
DI0: 1 , DI1: 1 , DI2: 1 , DI3: 1
DI0: 1 , DI1: 1 , DI2: 1 , DI3: 1
```
  
<!--
## 作例

[BTO公式]()  
[Twitter作例1]()  
[Twitter作例2]()  
[ブログ作例1]()  
[ブログ作例1]()  

## 雑誌掲載情報

[ラズパイマガジンXX年Y月号]()  
[Pc Watch]()

## 製品仕様
    【対応OS】Windows7以降
    【サイズ】W16×D20×H5mm
    【重量】約1g
    【入力点数】12(デジタル)
    【コネクタ】USBマイクロB
    【電源】5V (USBマイクロB)
    【使用温度】0 ～ 40℃（結露なきこと）
    【保証期間】 1年間
    【付属品】保証書 1部
    【生産国】Made in Japan
-->
