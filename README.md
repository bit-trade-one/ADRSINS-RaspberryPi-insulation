# ADRSINS-RaspberryPi-insulation
### ラズベリーパイ絶縁入力HAT
![タイトル画像のURLを右のカッコに]()

ラズベリーパイに5~24Vの信号を絶縁して入力できるADRSINSのページです。  

## [製品HPリンク](http://bit-trade-one.co.jp/) 

### [配線方法](#配線方法-1)
### [サンプルプログラムの実行方法](#サンプルプログラムの実行方法-1)
#### [サンプルコード](https://github.com/bit-trade-one/ADRSINS-RaspberryPi-insulation/blob/master/sample/sample.py)  
### [本体ピンヘッダの設定について](#本体ピンヘッダの設定について-1)
### [Q&A](FAQ.md)

#### [回路図](https://github.com/bit-trade-one/ADRSINS-RaspberryPi-insulation/blob/master/Schematics/ADRSINS_SchematicsV0.pdf)

#### [基板図](https://github.com/bit-trade-one/ADRSINS-RaspberryPi-insulation/blob/master/Dimensions/ADRSINS_DimensionsV0.pdf)

---

# 配線方法

INの側に入力  
OUTの側が出力になるように線をユーロブロックに接続ください。

![image](https://user-images.githubusercontent.com/85532743/185038917-152967ac-f973-4599-a638-1b6d8dfdfc89.png)

---

# サンプルプログラムの実行方法
ラズベリーパイのターミナルを起動し、下記スクリプトを入力してください。  

## ライブラリ関連のインストール

```
$ sudo apt-get update
$ sudo apt-get install -y python-dev
$ sudo apt-get install -y python-pip
$ sudo pip install RPi.GPIO
```

## 保存場所へ移動(各自お好みで)
```
$ cd Desktop 
```


## 本リポジトリをクローン

```
$ git clone https://github.com/bit-trade-one/ADRSINS-RaspberryPi-insulation.git
```

この後GtiHubのユーザ名・個人用アクセストークンを求められる事があります。  
その場合は表示に従ってください。  
[Githubドキュメント_個人アクセストークンを使用する](https://docs.github.com/ja/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)  

## クローンした場所へ移動
```
$ cd ADRSINS-RaspberryPi-insulation
$ cd Sample
```

## 使用方法
sample.pyを起動すると、1秒周期でDI0～DI3の4つの接点の入力を1秒周期で表示します。  
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
  
---
# 本体ピンヘッダの設定について 
ショートピンを0側に接続すると、ブリーダ抵抗が無効になり、   
ショートピンを1側に接続すると、ブリーダ抵抗が有効になります。  
  
ブリーダ抵抗が無効の場合  
DC5Vを入力すると5mA，DC24Vを入力すると24mA電流が流れます。  　
  
ブリーダ抵抗が有効の場合  
DC5Vを入力すると12.5mA，DC24Vを入力すると60mA電流が流れます。  
  
接続する接点に合わせて設定ください。  　
![image](https://user-images.githubusercontent.com/85532743/183619286-286e93cf-ce0b-4bc1-b537-99b3e18852fe.png)  
[ADRSINS上面図] 

--- 

ブリーダ抵抗とは電流を多く流すために回路に並列に接続された抵抗です。  
接続する機器の接点定格の最小適用負荷に応じて、流れる電流を調整するために挿入されます。
![image](https://user-images.githubusercontent.com/85532743/183622705-1f38d537-4aed-4358-9b29-71b9f893b3b6.png)  
［ADRSINS内部回路] 

--- 

機器の接点が劣化し酸化膜が生成され小信号が伝達できなくなることを防ぐために  
接点部にメッキなどを施した製品は微小負荷接点対策品などと呼ばれます。  
  
接点に施しが無い、微小負荷接点対策がされていない機器は要求する最小負荷が大きく、  
接点に対してある程度大きな電流を流す必要があります。  
  
例えば富士電機製スーパータイマ MS4Sシリーズは、  
接点の最小適用負荷が	DC5V10mAとなっています。  
この接点にはDC5V10mA以上の電圧・電流を流さないと、タイマ接点に発生する酸化皮膜などの絶縁が破壊できず、  
タイマ接点を閉じても電気信号が伝わらない可能性があります。  
  
ADRSINSのブリーダ抵抗を有効にすると、5Vの電源の場合約12mAを流すことが出来るので、   
タイマ接点からの信号を問題なく受け取ることが出来ます。  
![image](https://user-images.githubusercontent.com/85532743/183629607-2aeb35b5-9fd0-400a-bd8b-93b3fec605ab.png)
