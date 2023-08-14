import random
import time
import threading
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


thread_count = 1
file = open('logins.txt').read().split('\n')

abobus = 0
skip = 0
cl = 0


def thread():
    while file:
        to_check = file[0]
        file.remove(to_check)
        try:
            token(to_check)
        except Exception as e:
            print("Ошибка:", e)


def token(account):
    global abobus, skip, cl
    username = account.split(";")[0]
    pwd = account.split(";")[1]
    while True:

        useragent = random.SystemRandom().choice([
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
            'Mozilla/5.0 (Windows NT 8.0; Win32; x32) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
            # 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0',
            # 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 OPR/94.0.4606.65',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 16_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/109.0.5414.112 Mobile/15E148 Safari/604.1',
            # 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.117 Mobile Safari/537.36',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 16_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Mobile/15E148 Safari/604.1',
            # 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Vivaldi/5.6.2867.62',
            # 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Safari/605.1.15',
            # 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 EdgiOS/108.1462.77 Mobile/15E148 Safari/605.1.15'
        ])
        options = webdriver.ChromeOptions()
        PROXY = "89.187.185.237:10000"
        options.add_argument('--proxy-server=%s' % PROXY)
        options.add_argument(f'user-agent={useragent}')
        options.add_argument("--disable-blink-features=AutomationControlled")
        # options.headless = True
        options.add_argument("--mute-audio")
        options.add_experimental_option('prefs', {
            'profile.managed_default_content_settings.images': 2,
            'profile.managed_default_content_settings.mixed_script': 2,
            'profile.managed_default_content_settings.media_stream': 2,
            'profile.managed_default_content_settings.stylesheets': 2})
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument("--lang=EN")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        wait = WebDriverWait(driver, 26)

        driver.get(url='https://rumble.com/v2cust6-idiots-in-cars-2023.html')
        driver.find_element(By.XPATH, '//*[@id="vid_v2a9d4e"]/div[1]/div').click()

        driver.switch_to.frame(0)
        wait.until(ec.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[4]')))
        wait.until(ec.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[3]/div/div[2]/button')))
        driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[4]').click()
        driver.switch_to.default_content()
        time.sleep(0.1)
        driver.switch_to.window(driver.window_handles[0])

        driver.switch_to.frame(0)
        time.sleep(0.1)
        driver.execute_script("document.querySelector('.videoAdUiSkipButtonExperimentalText').click();")
        time.sleep(10)

        abobus = abobus + 1
        cl = cl + 1

        print(f'{abobus} | {skip}({cl})')

        driver.close()
        driver.quit()



for _ in range(thread_count):
    t = threading.Thread(target=thread)
    t.start()
