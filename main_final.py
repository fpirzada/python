from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

import urllib.request
import time
import mysql.connector


chrome_options = Options()
chrome_options.add_argument("user-data-dir=selenium")
# chrome_options.add_argument("--start-maximized")
chrome_options.headless = True

driver = webdriver.Chrome(
    executable_path="/Users/farhanpirzada/PycharmProjects/Electron-Python/OFF-WHITE/chromedriver",
    # chrome_options=chrome_options
   )
# driver.delete_all_cookies()

def mainWeb(next_url):
    # driver.execute_script("window.open('about:blank','tab1');")
    # driver.switch_to.window("tab1")
    # driver.maximize_window()
    # driver.get(next_url)
    #
    # WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.CSS_SELECTOR, "li.h-c-header__cta-li.h-c-header__cta-li--secondary"))
    # )
    # sign_up_link = driver.find_elements_by_css_selector("li.h-c-header__cta-li.h-c-header__cta-li--secondary")
    #
    # sign_up_link = sign_up_link[1].find_element_by_tag_name("a")
    # # sign_up_link.click()
    #
    # sign_up_link = sign_up_link.get_attribute("href")
    driver.execute_script("window.open('about:blank','tab2');")
    driver.switch_to.window("tab2")
    driver.maximize_window()
    driver.get("https://accounts.google.com/signin/v2/identifier?service=adwords&continue=https%3A%2F%2Fads.google.com%2Fum%2Fidentity%3Fsubid%3Dgb-en-ha-aw-sk-c-bau!o3~EAIaIQobChMIksfE3fng4wIVBbDtCh3KsQWFEAAYASAAEgLUY_D_BwE~57785785819~aud-590153514920%3Akwd-94527731~1485447575~284259843514&hl=en_US&ltmpl=signin&passive=0&skipvpage=true&flowName=GlifWebSignIn&flowEntry=ServiceLogin")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'identifierId'))
    )
    # breakpoint()
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
    time.sleep(2)

    driver.get("https://ads.google.com/aw/productgroups")

    WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".name-label.with-info"))
        )
    all_product = driver.find_element_by_css_selector(".name-label.with-info")
    all_product = all_product.get_attribute("class")
    all_product = all_product.replace("name-label with-info _ngcontent", "")

    print(all_product)
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div.particle-table-row"))
    )
    element = driver.find_element_by_css_selector("div.show-rows")
    ActionChains(driver).move_to_element(element).perform()
    products = driver.find_elements_by_css_selector("div.particle-table-row")
    for product in products:
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.particle-table-row"))
        )
        print(product.text)
        pro = product.find_element_by_css_selector("product-group-name-cell._nghost" + all_product + " div._ngcontent" + all_product + " div span")
        print(pro.get_attribute("class"))
        #
        #
        # # all_p = all_product.find_element_by_xpath("//ess-cell[2]/product-group-name-cell/div")
        hover = ActionChains(driver).move_to_element(pro)
        hover.perform()
        WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.TAG_NAME, "product-viewer-link"))
                )
        data = driver.find_elements_by_tag_name("product-viewer-link")
        print("**--hover data--**")
        for s_data in data:
            print(s_data.text)
        print("**--end- hover data--**")





    # isTrue = True

    # try:
    #     while isTrue is True:
    #
    #         pro = driver.find_element_by_css_selector(
    #             "product-group-name-cell._nghost" + all_product + " div._ngcontent" + all_product + " div span")
    #         print(pro.get_attribute("class"))
    #         #
    #         #
    #         # # all_p = all_product.find_element_by_xpath("//ess-cell[2]/product-group-name-cell/div")
    #         hover = ActionChains(driver).move_to_element(pro)
    #         hover.perform()
    #
    #         # all_product_11 = all_product.replace("41", "47")
    #         # print(all_product_11)
    #
    #         time.sleep(1)
    #         data = driver.find_element_by_xpath("//div[@focuscontentwrapper]")
    #         data = data.find_element_by_xpath("//td[@class='product-title']").text
    #         print(data)
    #         # print(data.get_attribute("innerHTML"))
    #         # dat = driver.find_element_by_css_selector("div.section.top._ngcontent" + all_product_11)
    #
    #         # WebDriverWait(driver, 10).until(
    #         #     EC.visibility_of_element_located((By.CSS_SELECTOR, "div.section.top"))
    #         # )
    #
    #         # p = data.find_element_by_tag_name("a").click()
    #         # print(p)
    #         # data = content.find_element_by_xpath("//root[@class='_nghost-fij-0']")
    #         # print(content.get_attribute("innerHTML"))
    #
    #         element = driver.find_element_by_css_selector("div.show-rows")
    #         ActionChains(driver).move_to_element(element).perform()
    #
    #         driver.find_element_by_xpath("//dropdown-button[@popuptype='listbox']").click()
    #         driver.find_element_by_xpath("//material-select-dropdown-item[6]").click()
    #
    #         time.sleep(3)
    #
    #         # products = driver.find_elements_by_css_selector("div.particle-table-row")
    #
    #
    #
    #         products = driver.find_elements_by_css_selector("div.particle-table-row")
    #         product_loop(products)
    #         next = driver.find_element_by_css_selector("material-button.next")
    #         if "is-disabled" in next.get_attribute("class"):
    #             break
    #         else:
    #             next.click()
    #             time.sleep(5)
    #
    # except:
    #     print("no loop in pages")



def product_loop(products):
    for product in products:
        print(product.text)



def main():

    next_url = 'https://ads.google.com/intl/en_gb/getstarted/?subid=gb-en-ha-aw-sk-c-bau!o3~EAIaIQobChMIksfE3fng4wIVBbDtCh3KsQWFEAAYASAAEgLUY_D_BwE~57785785819~aud-590153514920:kwd-94527731~1485447575~284259843514&utm_source=aw&utm_medium=ha&utm_campaign=gb-en-ha-aw-sk-c-bau!o3~EAIaIQobChMIksfE3fng4wIVBbDtCh3KsQWFEAAYASAAEgLUY_D_BwE~57785785819~aud-590153514920:kwd-94527731~1485447575~284259843514&gclid=EAIaIQobChMIksfE3fng4wIVBbDtCh3KsQWFEAAYASAAEgLUY_D_BwE&gclsrc=aw.ds'
    # print(next_url)
    Category = '553'

    mainWeb(next_url)
    # test()

if __name__ == '__main__':
    main()

