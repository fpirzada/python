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



def mainWeb(re_enter,cpc_amount,id):
    options = Options()
    options.headless = True
    caps = DesiredCapabilities().FIREFOX
    caps["marionette"] = True

    driver = webdriver.Firefox(
        capabilities=caps,
        options=options,
        executable_path=r'/Users/farhanpirzada/PycharmProjects/Express-matting/geckodriver')

    driver.get("https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin")

    # driver.delete_all_cookies()

    if re_enter == False:
        try:
            print("-- WELCOME TO THE CHANGE YOUR CPC PAGE --")
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
            time.sleep(3)
        except Exception as e:
            print("Can't enter into the account LOGIN ERROR!!")
            print(e)
            mainWeb(re_enter, cpc_amount, id)

    try:
        ## end
        driver.get("https://ads.google.com/aw/productgroups")

        WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".base-root-body"))
            )
        all_product = driver.find_element_by_css_selector(".base-root-body")
        all_product = all_product.get_attribute("class")
        all_product = all_product.replace("base-root-body _ngcontent", "")
        all_product = all_product.replace("1", "")

        print(all_product)
        time.sleep(1)

        i = 0
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".ess-table-wrapper"))
        )

    except Exception as e:
        print(e)
        re_enter = True
        mainWeb(re_enter)

    element = driver.find_element_by_css_selector(".ess-table-canvas.mouse-active")
    print(element.get_attribute("class"))
    isTrue = True

    while isTrue is True:
        for x in range(1, 250):

            print("-" + str(x))
            i += 1
            if i == 10:
                print("wait")
                i = 0
            element.send_keys(Keys.PAGE_DOWN)

        prods = driver.find_elements_by_css_selector(".particle-table-row")
        for prod in prods:
            #specific column select
            text = prod.find_element_by_css_selector(".name-label.with-info").text
            if text == str(id) or text == "name":
                print(prod.text)
                try:
                    p = prod.find_element_by_css_selector("._ngcontent"+all_product+"42")
                    print(p.get_attribute("class"))
                    if "included" in p.get_attribute("class") or "excluded" in p.get_attribute("class"):
                        driver.execute_script("arguments[0].setAttribute('class','particle-table-row active-row')", prod)
                        print('true')
                        plus = prod.find_element_by_css_selector(".bid-or-exclude-cell")
                        print(plus.get_attribute("class"))
                        # for pluss in plus:
                        driver.execute_script("arguments[0].scrollIntoView();", plus)
                        for x in range(1, 5):
                            print("-" + str(x))
                            i += 1
                            if i == 10:
                                print("wait")
                                i = 0
                            element.send_keys(Keys.PAGE_UP)
                        plus.click()
                        WebDriverWait(driver, 20).until(
                            EC.visibility_of_element_located((By.CSS_SELECTOR, ".input"))
                        )
                        input = driver.find_element_by_css_selector(".input")
                        input.clear()
                        input = driver.find_element_by_css_selector(".input")
                        input.send_keys(str(cpc_amount))

                        save = driver.find_element_by_css_selector(".btn.btn-yes._nghost"+all_product+"22")
                        save.send_keys(Keys.ENTER)

                        print("end")
                        isTrue = False
                        break

                except Exception as e:
                    print(e)
                    print("error: something went wrong")
                    mainWeb(re_enter, cpc_amount, id)
        print("next step")
        next = driver.find_element_by_css_selector("material-button.next")
        # break
        if "is-disabled" in next.get_attribute("class"):
            break
        else:
            next.click()
            time.sleep(4)


    print("-- WORK DONE --")
    driver.quit()

    ########### next page for expand the category as product
    #i = 0
    #
    # prods = driver.find_elements_by_css_selector(".particle-table-row")
    # for prod in prods:
    #
    #     try:
    #         p = prod.find_element_by_css_selector("._ngcontent"+all_product)
    #         print(p.get_attribute("class"))
    #         if "included" in p.get_attribute("class"):
    #             driver.execute_script("arguments[0].setAttribute('class','particle-table-row active-row')", prod)
    #
    #
    #             print('true')
    #             plus = prod.find_element_by_css_selector(".ess-layer-cell")
    #             print(plus.get_attribute("class"))
    #             # for pluss in plus:
    #             driver.execute_script("arguments[0].scrollIntoView();", plus)
    #
    #             plus = prod.find_element_by_css_selector(".ess-layer-cell div div")
    #             for x in range(1, 5):
    #
    #                 print("-" + str(x))
    #                 i += 1
    #                 if i == 10:
    #                     print("wait")
    #                     i = 0
    #                 element.send_keys(Keys.PAGE_UP)
    #             time.sleep(1)
    #             plus.click()
    #             WebDriverWait(driver, 20).until(
    #                 EC.visibility_of_element_located((By.CSS_SELECTOR, "div.label"))
    #             )
    #
    #             textfiled_next_page = driver.find_element_by_tag_name("text-field")
    #             if textfiled_next_page == "Online":
    #                 breakpoint()
    #
    #             driver.back()

                # time.sleep(5)
                # driver.back()
                # for x in range(1, 250):
                #
                #     print("-" + str(x))
                #     i += 1
                #     if i == 10:
                #         time.sleep(1)
                #         print("wait")
                #         i = 0
                #     element.send_keys(Keys.PAGE_DOWN)
        # except Exception as e:
        #     print(e)
        #     print("no included is there!!")
    ######### end


def main():

    next_url = 'https://ads.google.com/intl/en_gb/getstarted/?subid=gb-en-ha-aw-sk-c-bau!o3~EAIaIQobChMIksfE3fng4wIVBbDtCh3KsQWFEAAYASAAEgLUY_D_BwE~57785785819~aud-590153514920:kwd-94527731~1485447575~284259843514&utm_source=aw&utm_medium=ha&utm_campaign=gb-en-ha-aw-sk-c-bau!o3~EAIaIQobChMIksfE3fng4wIVBbDtCh3KsQWFEAAYASAAEgLUY_D_BwE~57785785819~aud-590153514920:kwd-94527731~1485447575~284259843514&gclid=EAIaIQobChMIksfE3fng4wIVBbDtCh3KsQWFEAAYASAAEgLUY_D_BwE&gclsrc=aw.ds'
    # print(next_url)
    Category = '553'

    re_enter = False

    mainWeb(re_enter)
    # test()

if __name__ == '__main__':
    main()