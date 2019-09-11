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
import sys
sys.setrecursionlimit(100000)

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

driver.delete_all_cookies()

product_list = []

all_product = None

import mysql.connector

mydb = mysql.connector.connect(host='localhost',
                               database='feedOPT',
                               user='root',
                               password='root')

mycursor = mydb.cursor()

def database_cleanner_Today():


    sql = "DELETE FROM Today"

    mycursor.execute(sql)

    mydb.commit()

    print(mycursor.rowcount, "record(s) affected")

    print('--------- DELETED ---------- OH Today PRODUCT IS DELETED NOW ---------- ')

def database_cleanner_Yesterday():

    sql = "DELETE FROM Yesterday"

    mycursor.execute(sql)

    mydb.commit()

    print(mycursor.rowcount, "record(s) affected")

    print('--------- DELETED ---------- OH Yesterday PRODUCT DATA IS DELETED NOW ---------- ')

def database_cleanner_This_week():
    sql = "DELETE FROM This_week"

    mycursor.execute(sql)

    mydb.commit()

    print(mycursor.rowcount, "record(s) affected")

    print('--------- DELETED ---------- OH This_week PRODUCT DATA IS DELETED NOW ---------- ')

def database_cleanner_Last7days():
    sql = "DELETE FROM Last7days"

    mycursor.execute(sql)

    mydb.commit()

    print(mycursor.rowcount, "record(s) affected")

    print('--------- DELETED ---------- OH Last7days PRODUCT DATA IS DELETED NOW ---------- ')

def database_cleanner_Lastweek_Sun_Sat():
    sql = "DELETE FROM Lastweek_Sun_Sat"

    mycursor.execute(sql)

    mydb.commit()

    print(mycursor.rowcount, "record(s) affected")

    print('--------- DELETED ---------- OH Lastweek_Sun_Sat PRODUCT DATA IS DELETED NOW ---------- ')

def database_cleanner_Last14days():
    sql = "DELETE FROM Last14days"

    mycursor.execute(sql)

    mydb.commit()

    print(mycursor.rowcount, "record(s) affected")

    print('--------- DELETED ---------- OH Last14days PRODUCT DATA IS DELETED NOW ---------- ')

def database_cleanner_Thismonth():
    sql = "DELETE FROM Thismonth"

    mycursor.execute(sql)

    mydb.commit()

    print(mycursor.rowcount, "record(s) affected")

    print('--------- DELETED ---------- OH Thismonth PRODUCT DATA IS DELETED NOW ---------- ')

def database_cleanner_Last30days():
    sql = "DELETE FROM Last30days"

    mycursor.execute(sql)

    mydb.commit()

    print(mycursor.rowcount, "record(s) affected")

    print('--------- DELETED ---------- OH Last30days PRODUCT DATA IS DELETED NOW ---------- ')

def database_cleanner_Lastmonth():
    sql = "DELETE FROM Lastmonth"

    mycursor.execute(sql)

    mydb.commit()

    print(mycursor.rowcount, "record(s) affected")

    print('--------- DELETED ---------- OH Lastmonth PRODUCT DATA IS DELETED NOW ---------- ')

def database_cleanner_Alltime():
    sql = "DELETE FROM Alltime"

    mycursor.execute(sql)

    mydb.commit()

    print(mycursor.rowcount, "record(s) affected")

    print('--------- DELETED ---------- OH Alltime PRODUCT DATA IS DELETED NOW ---------- ')

    #
    # sql = "DELETE FROM product_group"
    #
    # mycursor.execute(sql)
    #
    # mydb.commit()
    #
    # print(mycursor.rowcount, "record(s) affected")
    #
    # print('--------- DELETED ---------- OH PRODUCT DATA IS DELETED NOW ---------- ')
    #
    #
    # sql = "DELETE FROM product_group"
    #
    # mycursor.execute(sql)
    #
    # mydb.commit()
    #
    # print(mycursor.rowcount, "record(s) affected")
    #
    # print('--------- DELETED ---------- OH PRODUCT DATA IS DELETED NOW ---------- ')
    #
    #
    # sql = "DELETE FROM product_group"
    #
    # mycursor.execute(sql)
    #
    # mydb.commit()
    #
    # print(mycursor.rowcount, "record(s) affected")
    #
    # print('--------- DELETED ---------- OH PRODUCT DATA IS DELETED NOW ---------- ')
    #
    #
    # sql = "DELETE FROM product_group"
    #
    # mycursor.execute(sql)
    #
    # mydb.commit()
    #
    # print(mycursor.rowcount, "record(s) affected")
    #
    # print('--------- DELETED ---------- OH PRODUCT DATA IS DELETED NOW ---------- ')
    #
    #
    # sql = "DELETE FROM product_group"
    #
    # mycursor.execute(sql)
    #
    # mydb.commit()
    #
    # print(mycursor.rowcount, "record(s) affected")
    #
    # print('--------- DELETED ---------- OH PRODUCT DATA IS DELETED NOW ---------- ')
    #
    #
    # sql = "DELETE FROM product_group"
    #
    # mycursor.execute(sql)
    #
    # mydb.commit()
    #
    # print(mycursor.rowcount, "record(s) affected")
    #
    # print('--------- DELETED ---------- OH PRODUCT DATA IS DELETED NOW ---------- ')
    #
    #
    # sql = "DELETE FROM product_group"
    #
    # mycursor.execute(sql)
    #
    # mydb.commit()
    #
    # print(mycursor.rowcount, "record(s) affected")
    #
    # print('--------- DELETED ---------- OH PRODUCT DATA IS DELETED NOW ---------- ')
    #
    #
    # sql = "DELETE FROM product_group"
    #
    # mycursor.execute(sql)
    #
    # mydb.commit()
    #
    # print(mycursor.rowcount, "record(s) affected")
    #
    # print('--------- DELETED ---------- OH PRODUCT DATA IS DELETED NOW ---------- ')
    #
    #
    # sql = "DELETE FROM product_group"
    #
    # mycursor.execute(sql)
    #
    # mydb.commit()
    #
    # print(mycursor.rowcount, "record(s) affected")
    #
    # print('--------- DELETED ---------- OH PRODUCT DATA IS DELETED NOW ---------- ')
    #
    #
    # sql = "DELETE FROM product_group"
    #
    # mycursor.execute(sql)
    #
    # mydb.commit()
    #
    # print(mycursor.rowcount, "record(s) affected")
    #
    # print('--------- DELETED ---------- OH PRODUCT DATA IS DELETED NOW ---------- ')
    #
    #
    # sql = "DELETE FROM product_group"
    #
    # mycursor.execute(sql)
    #
    # mydb.commit()
    #
    # print(mycursor.rowcount, "record(s) affected")
    #
    # print('--------- DELETED ---------- OH PRODUCT DATA IS DELETED NOW ---------- ')




def mainWeb(re_enter,InThePage):

    # print("HELLLOOOOOOO ---")
    global product_list
    global all_product

    while True:
        if re_enter == False:

            while True:

                try:
                    if driver.current_url == "https://ads.google.com/aw/productgroups?ocid=349883671&euid=350506243&__u=5549915307&uscid=349883671&__c=8672891679&authuser=0":
                        break
                    else:

                        database_cleanner_Today()
                        database_cleanner_Yesterday()
                        database_cleanner_This_week()
                        database_cleanner_Last7days()
                        database_cleanner_Lastweek_Sun_Sat()
                        database_cleanner_Last14days()
                        database_cleanner_Thismonth()
                        database_cleanner_Last30days()
                        database_cleanner_Lastmonth()
                        database_cleanner_Alltime()

                        driver.execute_script("window.open('about:blank','tab2');")
                        driver.switch_to.window("tab2")
                        driver.maximize_window()
                        # driver.get(
                            # "https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
                        driver.get("https://ads.google.com/aw/productgroups")
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
                except Exception as e:
                    print(e)
                    print("Can't enter into the account LOGIN ERROR!!")
                    mainWeb(re_enter,InThePage)

        else:
            pass
        listbox = None
        # for blocking the code to go back to main page and then go to the products page
        if InThePage == False:
            pass
        try:
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
            all_product = all_product.replace("base-root-body _ngcontent", "")
            all_product = all_product.replace("1", "43")

            print(all_product)
            time.sleep(2)

            el = driver.find_element_by_xpath("//a[@navi-id='ProductGroups-tab']")
            driver.execute_script("arguments[0].click();", el)

            p = driver.find_element_by_css_selector("div._ngcontent" + all_product + " span").click()
            pro = driver.find_element_by_css_selector(
                "product-group-name-cell._nghost" + all_product + " div._ngcontent" + all_product + " div span")
            print(pro.get_attribute("class"))
            time.sleep(2)

            hover = ActionChains(driver).move_to_element(pro)
            hover.perform()

            all_product_11 = all_product.replace("41", "11")
            print(all_product_11)
            print("wait for 3 sec")
            time.sleep(1)

            data = driver.find_element_by_xpath("//div[@focuscontentwrapper]")

            data.find_element_by_tag_name("a").click()
            all_product = all_product.replace("43", "")

        except BaseException as e:
            print("Something went wrong. Lets try again :) ---- mainWeb(re_enter,False)")
            print(e)
            re_enter = True
            # breakpoint()
            mainWeb(re_enter,False)
        try:

            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "div.particle-table-row"))
            )
            time.sleep(2)

            click_dropdown = driver.find_element_by_tag_name("dropdown-button")
            print(click_dropdown.get_attribute("class"))
            click_dropdown.click()

            material_list = driver.find_element_by_tag_name("material-list")
            listbox = material_list.find_element_by_xpath("div[@role='listbox']")
            listbox = listbox.find_elements_by_tag_name("material-select-item")

            for list in listbox:
                dat_list = list.text
                list.click()
                time.sleep(3)

                isTrue = True

                i = 0
                # try:
                while isTrue is True:
                    WebDriverWait(driver, 10).until(
                        EC.visibility_of_element_located((By.CSS_SELECTOR, "div.base-root"))
                    )
                    element = driver.find_element_by_css_selector("div.base-root")
                    i = 0
                    time.sleep(10)

                    for x in range(1, 200):

                        print("-" + str(x))
                        i += 1
                        if i == 5:
                            time.sleep(1)
                            print("wait")
                            i = 0
                        element.send_keys(Keys.PAGE_DOWN)
                    WebDriverWait(driver, 10).until(
                        EC.visibility_of_element_located((By.CSS_SELECTOR, "div.particle-table-row"))
                    )
                    products = driver.find_elements_by_css_selector("div.particle-table-row")
                    type = "product"
                    number_product = len(products)
                    print(number_product)
                    if number_product > 0:
                        product_loop(products, type,dat_list)

                        next = driver.find_element_by_css_selector("material-button.next")
                        # break
                        if "is-disabled" in next.get_attribute("class"):
                            break
                        else:
                            next.click()
                            time.sleep(2)
                            pro = element.find_element_by_css_selector(
                                "material-button._ngcontent" + all_product + "20._nghost" + all_product + "22")
                            driver.execute_script("arguments[0].scrollIntoView();", pro)
                            print("page from top")
                            time.sleep(10)
                            # breakpoint()
                    else:
                        print("no product on the list ---")



                # for timer in range(600):
                #     print("TIMER :" + str(timer))
                #     time.sleep(1)
                try:
                    next = driver.find_element_by_css_selector("material-button.first")
                    # break
                    if "is-disabled" in next.get_attribute("class"):
                        print("nothing to do with it.")
                    else:
                        next.click()
                        print("next page")


                    click_dropdown = driver.find_element_by_tag_name("dropdown-button")
                    print(click_dropdown.get_attribute("class"))
                    click_dropdown.click()
                except:
                    print("in the last section of the code..")

            print("end of the game from the product section lets move on to the product group section..")


        except Exception as e:
            print(e)
            print("Complete script ERRORRRR..")
            # breakpoint()
            re_enter = True
            # mainWeb(re_enter,True)
            if listbox == None:
                mainWeb(re_enter, True)
            elif list == "Today":
                database_cleanner_Today()
                mainWeb(re_enter, True)
            elif list == "Yesterday":
                database_cleanner_Yesterday()
                mainWeb(re_enter, True)
            elif list == "This week (Sun – Today)":
                database_cleanner_This_week()
                mainWeb(re_enter, True)
            elif list == "Last 7 days":
                database_cleanner_Last7days()
                mainWeb(re_enter, True)
            elif list == "Last week (Sun – Sat)":
                database_cleanner_Lastweek_Sun_Sat()
                mainWeb(re_enter, True)
            elif list == "Last 14 days":
                database_cleanner_Last14days()
                mainWeb(re_enter, True)
            elif list == "This month":
                database_cleanner_Thismonth()
                mainWeb(re_enter, True)
            elif list == "Last 30 days":
                database_cleanner_Last30days()
                mainWeb(re_enter, True)
            elif list == "Last month":
                database_cleanner_Lastmonth()
                mainWeb(re_enter)
            elif list == "All time":
                database_cleanner_Alltime()
                mainWeb(re_enter, True)
            mainWeb(re_enter,True)
        product_group()
        break



def product_group():

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
        print("wait for 2 sec")
        time.sleep(2)

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
            try:
                WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, "div.particle-table-row"))
                )
                time.sleep(2)
                try:
                    driver.find_element_by_css_selector("material-button.nub.nub-nav-opened").click()
                    print("end -- first part")
                except:
                    print("Side bar is closed already !!")
            except Exception as e:
                print(e)
                print("Something went wrong. Lets try again :)")
                re_enter = True
                product_group()
            isTrue = True

            i = 0
            # try:

            # First of all get all the header column span IDs
            current_tab_info = driver.find_elements_by_xpath(
                "//div[@class='GMHeadMid']/table[@class='GMSection']/tbody/tr[@class='GMHeaderRow']/td/div/span")
            current_tab_header_list = [x.get_attribute('id') for x in current_tab_info]

            # Then get element text against each ID
            current_tab_header_label_list = []
            for i in current_tab_header_list:
                # will scroll until that element is not appeared on page
                current_header_info = driver.find_elements_by_xpath(
                    "//div[@class='GMHeadMid']/table[@class='GMSection']/tbody/tr[@class='GMHeaderRow']/td/div/span[@id='" + str(
                        i) + "']")
                driver.execute_script("arguments[0].scrollIntoView(true);", current_header_info[0])
                current_tab_header_label_list.append(current_header_info[0].text)

            # move_to_lef = driver.find_elements_by_css_selector("div.particle-table-header-cell.data-numeric.with-label-wrapper.particle-sortable.resizable")
            # for move in move_to_lef:
            #     target = move.find_element_by_link_text('Avg. CPC')
            #     driver.execute_script('arguments[0].scrollIntoView(true);', target)

            # e = driver.find_element_by_css_selector("div.particle-row-scroll-container")


            while isTrue is True:



                element = driver.find_element_by_css_selector("div.base-root")
                # driver.execute_script("arguments[0].scrollLeft(400);", element)

                i = 0

                for x in range(1, 5):

                    print("-" + str(x))
                    i += 1
                    if i == 10:
                        time.sleep(1)
                        print("wait")
                        i = 0
                    element.send_keys(Keys.PAGE_DOWN)

                products = driver.find_elements_by_css_selector("div.particle-table-row")
                type = "product_group"
                product_loop(products, type,dat_list)
                next = driver.find_element_by_css_selector("material-button.next")
                # break
                if "is-disabled" in next.get_attribute("class"):
                    break
                else:
                    next.click()
                    # time.sleep()
                    pro = element.find_element_by_css_selector(
                        "material-button._ngcontent" + all_product + "20._nghost" + all_product + "22")
                    driver.execute_script("arguments[0].scrollIntoView();", pro)
                    print("page from top")
                    time.sleep(4)
            try:
                next = driver.find_element_by_css_selector("material-button.first")
                # break
                if "is-disabled" in next.get_attribute("class"):
                    print("nothing to do with it.")
                else:
                    next.click()
                    print("next page")
                click_dropdown = driver.find_element_by_tag_name("dropdown-button")
                print(click_dropdown.get_attribute("class"))
                click_dropdown.click()
            except:
                print("in the last section of the code..")
    except:
        print("Complete script..")


    driver.quit()


def product_loop(products,type,dat_list):
    global product_list
    print("in the loop")
    x = 0
    # products = driver.find_elements_by_css_selector("div.particle-table-row")
    for product in products:
        # x += 1
        # if x == 2:
        #     break
        # pro = product.text
        # set_product = [s.strip() for s in pro.splitlines()]
        # # set_product = set(set_product)
        # product_list.append(set_product)

        ### complete product detail in the product page
        pro = product.text
        print(pro)

        ### going into the selected product page

        product_link = product.find_element_by_tag_name("a")
        product_link.send_keys(Keys.COMMAND + Keys.RETURN)
        time.sleep(2)
        # product_link.send_keys(Keys.CONTROL + Keys.TAB)
        driver.switch_to.window(driver.window_handles[2])
        main_window = driver.current_window_handle
        driver.switch_to.window(main_window)
        time.sleep(4)

        ### getting the dynamic variable of the google class
        try:
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "table-row"))
            )

            table_row = driver.find_element_by_css_selector("div.attributes-card")
            table_row = table_row.get_attribute("class")
            print(table_row)
            all_product = table_row.replace("attributes-card _ngcontent-", "")
            all_product = all_product.replace("-13", "")
            print(all_product)
            time.sleep(1)
        except:
            print("no table row is available")

        ### fetch the link of the product which lead us to the website
        try:
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "div.centering-container._ngcontent-"+all_product+"-13"))
            )
            proo = driver.find_element_by_css_selector("div.centering-container._ngcontent-"+all_product+"-13")

            product_table = proo.find_element_by_css_selector("product-viewer-attribute-list._ngcontent-"+all_product+"-13._nghost-"+all_product+"-23")
            product_a_link = product_table.find_element_by_tag_name("a")
            product_a_link = product_a_link.text
            print(product_a_link)
        except:
            while True:
                try:
                    print("except part of the code ----- need to refresh the page")
                    driver.get(driver.current_url)
                    WebDriverWait(driver, 10).until(
                        EC.visibility_of_element_located((By.CLASS_NAME, "table-row"))
                    )

                    table_row = driver.find_element_by_css_selector("div.attributes-card")
                    table_row = table_row.get_attribute("class")
                    print(table_row)
                    all_product = table_row.replace("attributes-card _ngcontent-", "")
                    all_product = all_product.replace("-13", "")
                    print(all_product)
                    WebDriverWait(driver, 10).until(
                        EC.visibility_of_element_located(
                            (By.CSS_SELECTOR, "div.centering-container._ngcontent-" + all_product + "-13"))
                    )
                    proo = driver.find_element_by_css_selector("div.centering-container._ngcontent-" + all_product + "-13")

                    product_table = proo.find_element_by_tag_name(
                        "product-viewer-link-attribute")
                    product_a_link = product_table.find_element_by_tag_name("a")
                    product_a_link = product_a_link.text
                    print(product_a_link)
                    break
                except:
                    print("error while refreshing the page in the single product section --- trying agian")
        driver.close()
        driver.switch_to.window(driver.window_handles[1])
        main_window = driver.current_window_handle
        driver.switch_to.window(main_window)
        # breakpoint()
        print("product link -----")
        try:

            if type == "product":

                if "Today" in dat_list:
                    o = [s.strip() for s in pro.splitlines()]
                    id = o[0]
                    title = o[1]
                    status = o[2]
                    price = o[3]
                    status_click = o[4]
                    stats_imp = o[5]
                    ctr = o[6]
                    cpc = o[7]
                    stats_cost = o[8]

                    import mysql.connector

                    mydb = mysql.connector.connect(host='localhost',
                                                   database='feedOPT',
                                                   user='root',
                                                   password='root')

                    mycursor = mydb.cursor()
                    print("here")
                    sql = "INSERT INTO Today(feed_id,title,status,price,stats_clicks,stats_impressions,ctr,cpc,stats_cost,product_a_link) " \
                          "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

                    args = (id, title, status, price, status_click, stats_imp, ctr, cpc, stats_cost, product_a_link)

                    print(args)
                    print("new")
                    mycursor.execute(sql, args)

                    mydb.commit()

                    print(mycursor.rowcount, "record(s) affected")

                    print('--------- ADDED ----------')
                elif "Yesterday" in dat_list:
                    o = [s.strip() for s in pro.splitlines()]
                    id = o[0]
                    title = o[1]
                    status = o[2]
                    price = o[3]
                    status_click = o[4]
                    stats_imp = o[5]
                    ctr = o[6]
                    cpc = o[7]
                    stats_cost = o[8]

                    import mysql.connector

                    mydb = mysql.connector.connect(host='localhost',
                                                   database='feedOPT',
                                                   user='root',
                                                   password='root')

                    mycursor = mydb.cursor()
                    print("here")
                    sql = "INSERT INTO Yesterday(feed_id,title,status,price,stats_clicks,stats_impressions,ctr,cpc,stats_cost,product_a_link) " \
                          "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

                    args = (id, title, status, price, status_click, stats_imp, ctr, cpc, stats_cost, product_a_link)

                    print(args)
                    print("new")
                    mycursor.execute(sql, args)

                    mydb.commit()

                    print(mycursor.rowcount, "record(s) affected")

                    print('--------- ADDED ----------')
                elif "This week (Sun – Today)" in dat_list:
                    o = [s.strip() for s in pro.splitlines()]
                    id = o[0]
                    title = o[1]
                    status = o[2]
                    price = o[3]
                    status_click = o[4]
                    stats_imp = o[5]
                    ctr = o[6]
                    cpc = o[7]
                    stats_cost = o[8]

                    import mysql.connector

                    mydb = mysql.connector.connect(host='localhost',
                                                   database='feedOPT',
                                                   user='root',
                                                   password='root')

                    mycursor = mydb.cursor()
                    print("here")
                    sql = "INSERT INTO This_week(feed_id,title,status,price,stats_clicks,stats_impressions,ctr,cpc,stats_cost,product_a_link) " \
                          "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

                    args = (id, title, status, price, status_click, stats_imp, ctr, cpc, stats_cost, product_a_link)

                    print(args)
                    print("new")
                    mycursor.execute(sql, args)

                    mydb.commit()

                    print(mycursor.rowcount, "record(s) affected")

                    print('--------- ADDED ----------')

                elif "Last 7 days" in dat_list:
                    o = [s.strip() for s in pro.splitlines()]
                    id = o[0]
                    title = o[1]
                    status = o[2]
                    price = o[3]
                    status_click = o[4]
                    stats_imp = o[5]
                    ctr = o[6]
                    cpc = o[7]
                    stats_cost = o[8]

                    import mysql.connector

                    mydb = mysql.connector.connect(host='localhost',
                                                   database='feedOPT',
                                                   user='root',
                                                   password='root')

                    mycursor = mydb.cursor()
                    print("here")
                    sql = "INSERT INTO Last7days(feed_id,title,status,price,stats_clicks,stats_impressions,ctr,cpc,stats_cost,product_a_link) " \
                          "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

                    args = (id, title, status, price, status_click, stats_imp, ctr, cpc, stats_cost, product_a_link)

                    print(args)
                    print("new")
                    mycursor.execute(sql, args)

                    mydb.commit()

                    print(mycursor.rowcount, "record(s) affected")

                    print('--------- ADDED ----------')
                elif "Last week (Sun – Sat)" in dat_list:
                    o = [s.strip() for s in pro.splitlines()]
                    id = o[0]
                    title = o[1]
                    status = o[2]
                    price = o[3]
                    status_click = o[4]
                    stats_imp = o[5]
                    ctr = o[6]
                    cpc = o[7]
                    stats_cost = o[8]

                    import mysql.connector

                    mydb = mysql.connector.connect(host='localhost',
                                                   database='feedOPT',
                                                   user='root',
                                                   password='root')

                    mycursor = mydb.cursor()
                    print("here")
                    sql = "INSERT INTO Lastweek_Sun_Sat(feed_id,title,status,price,stats_clicks,stats_impressions,ctr,cpc,stats_cost,product_a_link) " \
                          "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

                    args = (id, title, status, price, status_click, stats_imp, ctr, cpc, stats_cost, product_a_link)

                    print(args)
                    print("new")
                    mycursor.execute(sql, args)

                    mydb.commit()

                    print(mycursor.rowcount, "record(s) affected")

                    print('--------- ADDED ----------')
                elif "Last 14 days" in dat_list:
                    o = [s.strip() for s in pro.splitlines()]
                    id = o[0]
                    title = o[1]
                    status = o[2]
                    price = o[3]
                    status_click = o[4]
                    stats_imp = o[5]
                    ctr = o[6]
                    cpc = o[7]
                    stats_cost = o[8]

                    import mysql.connector

                    mydb = mysql.connector.connect(host='localhost',
                                                   database='feedOPT',
                                                   user='root',
                                                   password='root')

                    mycursor = mydb.cursor()
                    print("here")
                    sql = "INSERT INTO Last14days(feed_id,title,status,price,stats_clicks,stats_impressions,ctr,cpc,stats_cost,product_a_link) " \
                          "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

                    args = (id, title, status, price, status_click, stats_imp, ctr, cpc, stats_cost, product_a_link)

                    print(args)
                    print("new")
                    mycursor.execute(sql, args)

                    mydb.commit()

                    print(mycursor.rowcount, "record(s) affected")

                    print('--------- ADDED ----------')
                elif "This month" in dat_list:
                    o = [s.strip() for s in pro.splitlines()]
                    id = o[0]
                    title = o[1]
                    status = o[2]
                    price = o[3]
                    status_click = o[4]
                    stats_imp = o[5]
                    ctr = o[6]
                    cpc = o[7]
                    stats_cost = o[8]

                    import mysql.connector

                    mydb = mysql.connector.connect(host='localhost',
                                                   database='feedOPT',
                                                   user='root',
                                                   password='root')

                    mycursor = mydb.cursor()
                    print("here")
                    sql = "INSERT INTO Thismonth(feed_id,title,status,price,stats_clicks,stats_impressions,ctr,cpc,stats_cost,product_a_link) " \
                          "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

                    args = (id, title, status, price, status_click, stats_imp, ctr, cpc, stats_cost, product_a_link)

                    print(args)
                    print("new")
                    mycursor.execute(sql, args)

                    mydb.commit()

                    print(mycursor.rowcount, "record(s) affected")

                    print('--------- ADDED ----------')
                elif "Last 30 days" in dat_list:
                    o = [s.strip() for s in pro.splitlines()]
                    id = o[0]
                    title = o[1]
                    status = o[2]
                    price = o[3]
                    status_click = o[4]
                    stats_imp = o[5]
                    ctr = o[6]
                    cpc = o[7]
                    stats_cost = o[8]

                    import mysql.connector

                    mydb = mysql.connector.connect(host='localhost',
                                                   database='feedOPT',
                                                   user='root',
                                                   password='root')

                    mycursor = mydb.cursor()
                    print("here")
                    sql = "INSERT INTO Last30days(feed_id,title,status,price,stats_clicks,stats_impressions,ctr,cpc,stats_cost,product_a_link) " \
                          "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

                    args = (id, title, status, price, status_click, stats_imp, ctr, cpc, stats_cost, product_a_link)

                    print(args)
                    print("new")
                    mycursor.execute(sql, args)

                    mydb.commit()

                    print(mycursor.rowcount, "record(s) affected")

                    print('--------- ADDED ----------')
                elif "Last month" in dat_list:
                    o = [s.strip() for s in pro.splitlines()]
                    id = o[0]
                    title = o[1]
                    status = o[2]
                    price = o[3]
                    status_click = o[4]
                    stats_imp = o[5]
                    ctr = o[6]
                    cpc = o[7]
                    stats_cost = o[8]

                    import mysql.connector

                    mydb = mysql.connector.connect(host='localhost',
                                                   database='feedOPT',
                                                   user='root',
                                                   password='root')

                    mycursor = mydb.cursor()
                    print("here")
                    sql = "INSERT INTO Lastmonth(feed_id,title,status,price,stats_clicks,stats_impressions,ctr,cpc,stats_cost,product_a_link) " \
                          "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

                    args = (id, title, status, price, status_click, stats_imp, ctr, cpc, stats_cost, product_a_link)

                    print(args)
                    print("new")
                    mycursor.execute(sql, args)

                    mydb.commit()

                    print(mycursor.rowcount, "record(s) affected")

                    print('--------- ADDED ----------')
                elif "All time" in dat_list:
                    o = [s.strip() for s in pro.splitlines()]
                    id = o[0]
                    title = o[1]
                    status = o[2]
                    price = o[3]
                    status_click = o[4]
                    stats_imp = o[5]
                    ctr = o[6]
                    cpc = o[7]
                    stats_cost = o[8]

                    import mysql.connector

                    mydb = mysql.connector.connect(host='localhost',
                                                   database='feedOPT',
                                                   user='root',
                                                   password='root')

                    mycursor = mydb.cursor()
                    print("here")
                    sql = "INSERT INTO Alltime(feed_id,title,status,price,stats_clicks,stats_impressions,ctr,cpc,stats_cost,product_a_link) " \
                          "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

                    args = (id, title, status, price, status_click, stats_imp, ctr, cpc, stats_cost, product_a_link)

                    print(args)
                    print("new")
                    mycursor.execute(sql, args)

                    mydb.commit()

                    print(mycursor.rowcount, "record(s) affected")

                    print('--------- ADDED ----------')

            #### product_group database

            elif type == "product_group":
                o = [s.strip() for s in pro.splitlines()]
                product = o[0]
                group_id = o[1]
                w_HPLB = o[2]
                Adgroup = o[3]
                cpc = o[4]
                Cost_all_conv = o[5]
                Avg_cpc = o[6]
                Conversions = o[7]
                Conversion_value_per_cost = o[8]
                import mysql.connector

                mydb = mysql.connector.connect(host='localhost',
                                               database='feedOPT',
                                               user='root',
                                               password='root')

                mycursor = mydb.cursor()
                print("here")
                sql = "INSERT INTO product_group(group_id,product,w_HPLB,Adgroup,cpc,Cost_all_conv,Avg_cpc,Conversions,Conversion_value_per_cost) " \
                      "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"

                args = (group_id,product,w_HPLB,Adgroup,cpc,Cost_all_conv,Avg_cpc,Conversions,Conversion_value_per_cost)

                print(args)
                print("new")
                mycursor.execute(sql, args)

                mydb.commit()

                print(mycursor.rowcount, "record(s) affected")

                print('--------- ADDED ----------')

        except:
            print("no ===--------------===")




def main():

    next_url = 'https://ads.google.com/intl/en_gb/getstarted/?subid=gb-en-ha-aw-sk-c-bau!o3~EAIaIQobChMIksfE3fng4wIVBbDtCh3KsQWFEAAYASAAEgLUY_D_BwE~57785785819~aud-590153514920:kwd-94527731~1485447575~284259843514&utm_source=aw&utm_medium=ha&utm_campaign=gb-en-ha-aw-sk-c-bau!o3~EAIaIQobChMIksfE3fng4wIVBbDtCh3KsQWFEAAYASAAEgLUY_D_BwE~57785785819~aud-590153514920:kwd-94527731~1485447575~284259843514&gclid=EAIaIQobChMIksfE3fng4wIVBbDtCh3KsQWFEAAYASAAEgLUY_D_BwE&gclsrc=aw.ds'
    # print(next_url)
    Category = '553'

    re_enter = False

    mainWeb(re_enter,False)
    # test()

if __name__ == '__main__':
    main()
