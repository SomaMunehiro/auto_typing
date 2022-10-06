# auto_typing
 とある勉強会で使ったプログラム


# 環境
```
Mac BigSur 11.7
Python 3.7.8
PyAutoGUI 0.9.53
selenium 3.141.0
webdriver-manager 3.8.3
```

# pip コマンド
```
pip install pyautogui
pip install selenium
pip install webdriver-manager
```

# 実行時に気をつけること
* ***絶対に実行中に他のウィンドウを開かないこと(終了処理を書いていないので終了が難しくなる)***
* ***sudo コマンドをつけて実行すること (webdriverをインストールする際に権限が必要なことがある)***
* ***seleniumのバージョンに応じて実行するプログラムを切り替えること***