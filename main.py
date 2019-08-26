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
    executable_path=r'/Users/farhanpirzada/PycharmProjects/Express-matting/geckodriver')

driver.get("https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin")

# driver.delete_all_cookies()

product_list = []

def mainWeb(re_enter):
    global product_list
    if re_enter == False:

        try:
            # import mysql.connector
        #
        #     mydb = mysql.connector.connect(host='localhost',
        #                                    database='feedOPT',
        #                                    user='root',
        #                                    password='root')
        #
        #     mycursor = mydb.cursor()
        #
        #     sql = "DELETE FROM datta"
        #
        #     mycursor.execute(sql)
        #
        #     mydb.commit()
        #
        #     print(mycursor.rowcount, "record(s) affected")
        #
        #     print('--------- DELETED ---------- OH ITS DELETED NOW ---------- ')


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
        except:
            print("Can't enter into the account LOGIN ERROR!!")
            mainWeb()

    try:
        ## end
        driver.get("https://ads.google.com/aw/productgroups")

        WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".base-root-body"))
            )
        all_product = driver.find_element_by_css_selector(".base-root-body")
        all_product = all_product.get_attribute("class")
        all_product = all_product.replace("base-root-body _ngcontent", "")
        all_product = all_product.replace("1", "43")

        print(all_product)
        time.sleep(1)

        # WebDriverWait(driver, 10).until(
        #     EC.visibility_of_element_located((By.CSS_SELECTOR, ".name-label.with-info"))
        # )
        el = driver.find_element_by_xpath("//a[@navi-id='ProductGroups-tab']")
        driver.execute_script("arguments[0].click();", el)

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div._ngcontent" + all_product))
        )
        p = driver.find_element_by_css_selector("div._ngcontent" + all_product+" span").click()
        pro = driver.find_element_by_css_selector(
            "product-group-name-cell._nghost" + all_product + " div._ngcontent" + all_product + " div span")
        print(pro.get_attribute("class"))
        time.sleep(1)
        #
        #
        # # all_p = all_product.find_element_by_xpath("//ess-cell[2]/product-group-name-cell/div")
        hover = ActionChains(driver).move_to_element(pro)
        hover.perform()

        all_product_11 = all_product.replace("41", "11")
        print(all_product_11)

        time.sleep(1)
        data = driver.find_element_by_xpath("//div[@focuscontentwrapper]")
        # print(data.get_attribute("innerHTML"))
        # dat = driver.find_element_by_css_selector("div.section.top._ngcontent" + all_product_11)

        # WebDriverWait(driver, 10).until(
        #     EC.visibility_of_element_located((By.CSS_SELECTOR, "div.section.top"))
        # )

        p = data.find_element_by_tag_name("a").click()
        # print(p)
        # data = content.find_element_by_xpath("//root[@class='_nghost-fij-0']")
        # print(content.get_attribute("innerHTML"))
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.particle-table-row"))
        )
        time.sleep(2)
    except BaseException as e:
        print(e)
        print("Something went wrong. Lets try again :)")
        re_enter = True
        mainWeb(re_enter)
    # driver.execute_script("window.scrollTo(0, 44338px)")
    # last_height = driver.execute_script("document.getElementsByClassName('base-root-body');")
    # driver.execute_script("window.scrollTo(0,document.getElementsByClassName('base-root-body').scrollHeight);")


    # element = driver.find_element_by_css_selector("div.base-root")
    # i = 0
    # for x in range(1, 180):
    #
    #     print("-"+str(x))
    #     i += 1
    #     if i == 10:
    #         time.sleep(1)
    #         print("wait")
    #         i = 0
    #     # eula = driver.find_element_by_css_selector('div.mouse-active')
    #     # driver.execute_script('arguments[0].scrollTo(0, '+x+');', eula)
    #     # try:/
    #     element.send_keys(Keys.PAGE_DOWN)

        # except:
        #     pass
            # time.sleep(1)
        # ActionChains(driver).move_to_element(element[x]).perform()

        # element = driver.findElement(By.id("id_of_element"));
        # elements = driver.find_elements_by_css_selector("div.particle-table-row")
    # for element in elements:
    #     element = element.text
    # driver.find_element_by_xpath("//dropdown-button[@popuptype='listbox']").click()
    # driver.find_element_by_xpath("//material-select-dropdown-item[6]").click()

    time.sleep(2)

    # products = driver.find_elements_by_css_selector("div.particle-table-row")
    isTrue = True

    i = 0
    # try:
    while isTrue is True:
        element = driver.find_element_by_css_selector("div.base-root")
        i = 0

        for x in range(1, 250):

            print("-" + str(x))
            i += 1
            if i == 10:
                time.sleep(1)
                print("wait")
                i = 0
            element.send_keys(Keys.PAGE_DOWN)
        products = driver.find_elements_by_css_selector("div.particle-table-row")
        product_loop(products)
        next = driver.find_element_by_css_selector("material-button.next")
        if "is-disabled" in next.get_attribute("class"):
            break
        else:
            next.click()
            time.sleep(4)



    for pro in product_list:
        print(pro)

    driver.quit()

    return product_list

    # except:
    #     print("no loop in pages")


    #
    # products = driver.find_elements_by_css_selector(".particle-table-row")
    # for product in products:
    #     print(product.text)


    # for link in links:
    #     print(link)
    # print(links)
    # print(content.text)
    # body.get_attribute("")

    # driver.switch_to.window("tab1")


def product_loop(products):
    global product_list
    print("in the loop")

    # products = driver.find_elements_by_css_selector("div.particle-table-row")
    for product in products:
        # print("*--*")
        # print(product.text)
        # print("*--*")

        pro = product.text
        product_list.append([s.strip() for s in pro.splitlines()])

        #
        # try:
        #     o = [s.strip() for s in pro.splitlines()]
        #     id = o[0]
        #     title = o[1]
        #     status = o[2]
        #     price = o[3]
        #     status_click = o[4]
        #     stats_imp = o[5]
        #     ctr = o[6]
        #     cpc = o[7]
        #     stats_cost = o[8]
        #
        #     import mysql.connector
        #
        #     mydb = mysql.connector.connect(host='localhost',
        #                                    database='feedOPT',
        #                                    user='root',
        #                                    password='root')
        #
        #     mycursor = mydb.cursor()
        #     print("here")
        #     sql = "INSERT INTO datta(feed_id,title,status,price,stats_clicks,stats_impressions,ctr,cpc,stats_cost) " \
        #           "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        #
        #     args = (id,title,status,price,status_click,stats_imp,ctr,cpc,stats_cost)
        #
        #     print(args)
        #     print("new")
        #     mycursor.execute(sql, args)
        #
        #     mydb.commit()
        #
        #     print(mycursor.rowcount, "record(s) affected")
        #
        #     print('--------- ADDED ----------')
        # except:
        #     print("no ===--------------===")

def main():

    next_url = 'https://ads.google.com/intl/en_gb/getstarted/?subid=gb-en-ha-aw-sk-c-bau!o3~EAIaIQobChMIksfE3fng4wIVBbDtCh3KsQWFEAAYASAAEgLUY_D_BwE~57785785819~aud-590153514920:kwd-94527731~1485447575~284259843514&utm_source=aw&utm_medium=ha&utm_campaign=gb-en-ha-aw-sk-c-bau!o3~EAIaIQobChMIksfE3fng4wIVBbDtCh3KsQWFEAAYASAAEgLUY_D_BwE~57785785819~aud-590153514920:kwd-94527731~1485447575~284259843514&gclid=EAIaIQobChMIksfE3fng4wIVBbDtCh3KsQWFEAAYASAAEgLUY_D_BwE&gclsrc=aw.ds'
    # print(next_url)
    Category = '553'

    re_enter = False

    mainWeb(re_enter)
    # test()

if __name__ == '__main__':
    main()

