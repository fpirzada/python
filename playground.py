from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import urllib.request
import time
import mysql.connector

options = Options()
options.headless = True
caps = DesiredCapabilities().FIREFOX
caps["marionette"] = True

driver = webdriver.Firefox(
    capabilities=caps,
    options=options,
    executable_path=r'/Users/farhanpirzada/PycharmProjects/Express-matting/geckodriver'
)

driver.get("https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin")

# driver.delete_all_cookies()

def mainWeb(re_enter):
    test = "test"
    if re_enter == False:
        try:
            pass
            # driver.execute_script("window.open('about:blank','tab2');")
            # driver.switch_to.window("tab2")
            # driver.maximize_window()
            # driver.get(
            #     "https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
        except:
            pass

        driver.quit()
    print("hello")
    return test


def main():

    next_url = 'https://ads.google.com/intl/en_gb/getstarted/?subid=gb-en-ha-aw-sk-c-bau!o3~EAIaIQobChMIksfE3fng4wIVBbDtCh3KsQWFEAAYASAAEgLUY_D_BwE~57785785819~aud-590153514920:kwd-94527731~1485447575~284259843514&utm_source=aw&utm_medium=ha&utm_campaign=gb-en-ha-aw-sk-c-bau!o3~EAIaIQobChMIksfE3fng4wIVBbDtCh3KsQWFEAAYASAAEgLUY_D_BwE~57785785819~aud-590153514920:kwd-94527731~1485447575~284259843514&gclid=EAIaIQobChMIksfE3fng4wIVBbDtCh3KsQWFEAAYASAAEgLUY_D_BwE&gclsrc=aw.ds'
    # print(next_url)
    Category = '553'

    re_enter = False
    test  = " test "
    return test
    # test()

if __name__ == '__main__':
    main()