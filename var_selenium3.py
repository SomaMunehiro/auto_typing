from warnings import catch_warnings
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

import pyautogui
import keyboard

# driver の準備
# Option指定
# ヘッドレスモード指定
options = Options()
# options.add_argument('--headless')
# 自動制御の文言を削除
# 見栄えを良くするため
options.add_experimental_option("excludeSwitches", ['enable-automation'])
# driverのパス
driver_path = './driver/chromedriver'
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
# wait until someid is clickable
wait = WebDriverWait(driver, 10)

try:

    # 会社検索サイトを開く
    driver.get('https://manabi-gakushu.benesse.ne.jp/gakushu/typing/nihongonyuryoku.html')

    # windowを最大化
    driver.fullscreen_window()

    # 設定画面に移動
    driver.find_element(By.ID,'goSettingButton').click()

    # ゲームが終了するまでループして入力
    while True:
        # ターミナルやコマンドライン上でエスケープキーが入力されたら強制終了
        if keyboard.is_pressed('escape'):
            break

        # ゲーム終了時の画面だった場合ループを抜ける
        try:
            driver.find_element(By.CLASS_NAME,'imageLabel result')
        except:
            pass
        else:
            print('終了')
            break
        
        # 表示されている文章を取得してキーボード入力を代行
        try:
            element = wait.until(EC.element_to_be_clickable((By.ID, 'remaining')))
        except:
            continue
        else:
            pyautogui.write(element.text, interval=0.05)
except:
    print("異常終了")
else:
    print("正常終了")
finally:
    driver.close()


    