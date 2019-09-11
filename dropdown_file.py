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
    # options=options,
    executable_path=r'/Users/farhanpirzada/PycharmProjects/Express-matting/geckodriver')

driver.get("https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin")

driver.delete_all_cookies()

product_list = []

def mainWeb(re_enter):
    global product_list



    while True:
        if re_enter == False:

            try:

                driver.execute_script("window.open('about:blank','tab2');")
                driver.switch_to.window("tab2")
                driver.maximize_window()
                driver.get(
                    "https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")

                WebDriverWait(driver, 20).until(
                    EC.visibility_of_element_located((By.ID,"identifierId"))
                )
                # breakpoint()
                # time.sleep(20)
                user = driver.find_element_by_id("identifierId")
                user.clear()
                user = driver.find_element_by_id("identifierId")
                user = user.send_keys("aquasolutionsuk1@gmail.com")
                user = driver.find_element_by_id("identifierId")
                user.send_keys(Keys.ENTER)
                # time.sleep()
                WebDriverWait(driver,10).until(
                    EC.visibility_of_element_located((By.NAME,"password"))
                )
                # time.sleep(2)
                # user = user.clear()
                user = driver.find_element_by_name("password")
                user = user.send_keys("Allahone")
                user = driver.find_element_by_name("password")
                user.send_keys(Keys.ENTER)
                time.sleep(5)
                print("------- logged in -------")
            except:
                print("Can't enter into the account LOGIN ERROR!!")
                mainWeb(re_enter)

        ## end
        print("hello")
        driver.get("https://ads.google.com/aw/productgroups")
        print("hel")
        WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".base-root-body"))
            )
        print("h")
        all_product = driver.find_element_by_css_selector(".base-root-body")
        all_product = all_product.get_attribute("class")
        all_product = all_product.replace("base-root-body _ngcontent-", "")
        all_product = all_product.replace("-1", "")

        print(all_product)
        time.sleep(2)


        el = driver.find_element_by_xpath("//a[@navi-id='ProductGroups-tab']")
        driver.execute_script("arguments[0].click();", el)

        click_dropdown = driver.find_element_by_tag_name("dropdown-button")
        print(click_dropdown.get_attribute("class"))
        click_dropdown.click()

        material_list = driver.find_element_by_tag_name("material-list")
        listbox = material_list.find_element_by_xpath("div[@role='listbox']")
        listbox = listbox.find_elements_by_tag_name("material-select-item")
        for list in listbox:
            list.click()
            print(list.text)
            time.sleep(3)
            next = driver.find_element_by_css_selector("material-button.last")
            # break
            if "is-disabled" in next.get_attribute("class"):
                print("nothing to do with it.")
            else:
                next.click()
                print("next page")
            click_dropdown = driver.find_element_by_tag_name("dropdown-button")
            print(click_dropdown.get_attribute("class"))
            click_dropdown.click()

        print("end")


        break
    time.sleep(5)
    driver.quit()
def main():

    next_url = 'https://ads.google.com/intl/en_gb/getstarted/?subid=gb-en-ha-aw-sk-c-bau!o3~EAIaIQobChMIksfE3fng4wIVBbDtCh3KsQWFEAAYASAAEgLUY_D_BwE~57785785819~aud-590153514920:kwd-94527731~1485447575~284259843514&utm_source=aw&utm_medium=ha&utm_campaign=gb-en-ha-aw-sk-c-bau!o3~EAIaIQobChMIksfE3fng4wIVBbDtCh3KsQWFEAAYASAAEgLUY_D_BwE~57785785819~aud-590153514920:kwd-94527731~1485447575~284259843514&gclid=EAIaIQobChMIksfE3fng4wIVBbDtCh3KsQWFEAAYASAAEgLUY_D_BwE&gclsrc=aw.ds'
    # print(next_url)
    Category = '553'

    re_enter = False

    mainWeb(re_enter)
    # test()

if __name__ == '__main__':
    main()
