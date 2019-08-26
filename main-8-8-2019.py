from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains

import urllib.request
import time
import mysql.connector

options = Options()
options.headless = True
driver = webdriver.Firefox(
    options=options,
    executable_path=r'/Users/farhanpirzada/PycharmProjects/Express-matting/geckodriver'
)

driver.get("https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin")

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
    driver.get("https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
    #
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
    #
    # WebDriverWait(driver, 10).until(
    #     EC.visibility_of_element_located((By.CSS_SELECTOR, ".ps-aw"))
    # )
    # body = driver.find_element_by_css_selector(".ps-aw")
    # print(body.get_attribute("innerHTML"))
    # wait = WebDriverWait(driver, 10)
    # wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".ps-aw")))

    # body = driver.find_element_by_xpath("//*[@class='ps-aw']")

    # content = body.find_element_by_xpath("//div[@ng-app]/root/div/div/div/awsm-left-nav/div[3]/div/awsm-campaign-tree/div/awsm-campaign-section/div[2]/div[2]")
    # a_href = content.find_element_by_tag_name("a")
    # print(a_href.get_attribute("class"))
    # a_href.click()


    #product details start

    # driver.find_element_by_xpath("//a[@navi-id='AdGroups-tab']").click()
    # # for ad_group in ad_groups:
    # WebDriverWait(driver, 10).until(
    #     EC.visibility_of_element_located((By.CSS_SELECTOR, ".particle-table-row"))
    # )
    # ad_groups = driver.find_element_by_css_selector(".particle-table-row")
    # # ActionChains(firefox).move_to_element(ad_groups)
    # # hover.perform()
    # # print(ad_groups.get_attribute("class"))
    # ad_groups.find_element_by_tag_name("a").click()
    # # print(ad_groups.text)
    #
    # WebDriverWait(driver, 10).until(
    #     EC.visibility_of_element_located((By.CSS_SELECTOR, ".name-label.with-info"))
    # )
    # # all_product = driver.find_element_by_xpath("//span[@class='name-label with-info']")
    # all_pro = driver.find_element_by_css_selector(".name-label.with-info")
    # all_product = driver.find_element_by_css_selector(".name-label.with-info")
    # all_product = all_product.get_attribute("class")
    # all_product = all_product.replace("name-label with-info _ngcontent", "")
    #
    # print(all_product)
    #
    # driver.find_element_by_xpath("//a[@navi-id='ProductGroups-tab']").click()
    # WebDriverWait(driver, 10).until(
    #     EC.visibility_of_element_located((By.CSS_SELECTOR, "div._ngcontent"+all_product))
    # )
    # p = driver.find_element_by_css_selector("div._ngcontent"+all_product)
    # p.click()
    # pro = driver.find_element_by_css_selector("product-group-name-cell._nghost"+all_product +" div._ngcontent"+all_product+" div span")
    # print(pro.get_attribute("class"))
    # #
    # #
    # # # all_p = all_product.find_element_by_xpath("//ess-cell[2]/product-group-name-cell/div")
    # hover = ActionChains(driver).move_to_element(pro)
    # hover.perform()
    #
    # all_product_11 = all_product.replace("41","11")
    # WebDriverWait(driver, 10).until(
    #     EC.visibility_of_element_located((By.CSS_SELECTOR, "a.summary-link._ngcontent"+all_product_11))
    # )
    # driver.find_element_by_css_selector("a.summary-link._ngcontent"+all_product_11).click()
    # # data = content.find_element_by_xpath("//root[@class='_nghost-fij-0']")
    # # print(content.get_attribute("innerHTML"))
    #
    # products = driver.find_elements_by_css_selector("div.particle-table-row")
    # for product in products:
    #     print(product.text)



    ## end
    driver.get("https://ads.google.com/aw/productgroups")

    WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".name-label.with-info"))
        )
    all_product = driver.find_element_by_css_selector(".name-label.with-info")
    all_product = all_product.get_attribute("class")
    all_product = all_product.replace("name-label with-info _ngcontent", "")

    print(all_product)
    # WebDriverWait(driver, 10).until(
    #     EC.visibility_of_element_located((By.CSS_SELECTOR, ".name-label.with-info"))
    # )
    el = driver.find_element_by_xpath("//a[@navi-id='ProductGroups-tab']")
    driver.execute_script("arguments[0].click();", el)
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div._ngcontent" + all_product))
    )
    p = driver.find_element_by_css_selector("div._ngcontent" + all_product)
    p.click()
    pro = driver.find_element_by_css_selector(
        "product-group-name-cell._nghost" + all_product + " div._ngcontent" + all_product + " div span")
    print(pro.get_attribute("class"))
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
    # driver.execute_script("window.scrollTo(0, 44338px)")
    # element = driver.find_element_by_css_selector("div.show-rows")
    # ActionChains(driver).move_to_element(element).perform()
    i = 0
    for x in range(1, 55000):
        x = str(x)
        i += 1
        if i == 100:
            time.sleep(1)
            i = 0
        print("-")
        eula = driver.find_element_by_css_selector('div.base-root-body')
        driver.execute_script('arguments[0].scrollTo(0, '+x+');', eula)


        # element = driver.findElement(By.id("id_of_element"));
        # elements = driver.find_elements_by_css_selector("div.particle-table-row")
    # for element in elements:
    #     element = element.text
    # driver.find_element_by_xpath("//dropdown-button[@popuptype='listbox']").click()
    # driver.find_element_by_xpath("//material-select-dropdown-item[6]").click()

    time.sleep(2)

    # products = driver.find_elements_by_css_selector("div.particle-table-row")
    isTrue = True

    import mysql.connector

    mydb = mysql.connector.connect(host='localhost',
                                   database='feedOPT',
                                   user='root',
                                   password='root')

    mycursor = mydb.cursor()

    sql = "DELETE FROM datta"

    mycursor.execute(sql)

    mydb.commit()

    print(mycursor.rowcount, "record(s) affected")

    print('--------- DELETED ---------- OH ITS DELETED NOW ---------- ')
    i = 0
    try:
        while isTrue is True:
            for x in range(1, 55000):
                i += 1
                if i == 100:
                    time.sleep(1)
                    i = 0
                # eula = driver.find_element_by_css_selector('.particle-table-row')
                driver.execute_script('window.scrollTo(0, 100);')
            products = driver.find_elements_by_css_selector("div.particle-table-row")
            product_loop(products)
            next = driver.find_element_by_css_selector("material-button.next")
            if "is-disabled" in next.get_attribute("class"):
                break
            else:
                next.click()
                time.sleep(2)
                element = driver.find_element_by_css_selector("svg.aplos-chart.aplos-chart-svg")
                ActionChains(driver).move_to_element(element).perform()
                time.sleep(1)
                element = driver.find_element_by_css_selector("div.show-rows")
                ActionChains(driver).move_to_element(element).perform()
                time.sleep(1)

    except:
        print("no loop in pages")


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


    # products = driver.find_elements_by_css_selector("div.particle-table-row")
    for product in products:

        # img = product.find_element_by_xpath("//ess-cell[@essfield='image_url_152_152']").text
        # title = product.find_element_by_xpath("//ess-cell[@essfield='product_title']").text
        # status = product.find_element_by_xpath("//ess-cell[@essfield='status']").text
        # price = product.find_element_by_xpath("//ess-cell[@essfield='price']").text
        # click = product.find_element_by_xpath("//ess-cell[@essfield='stats.clicks']").text
        # impr = product.find_element_by_xpath("//ess-cell[@essfield='stats.impressions']").text
        # CTR = product.find_element_by_xpath("//ess-cell[@essfield='stats.click_through_rate']").text
        # CPC = product.find_element_by_xpath("//ess-cell[@essfield='stats.cost_per_click']").text
        # cost = product.find_element_by_xpath("//ess-cell[@essfield='stats.cost']").text
        #

        print("*--*")
        # print(id,img,title,status,price,click,impr,CTR,CPC,cost)
        print("*--*")

        pro = product.text
        try:
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
            sql = "INSERT INTO datta(feed_id,title,status,price,stats_clicks,stats_impressions,ctr,cpc,stats_cost) " \
                  "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"

            args = (id,title,status,price,status_click,stats_imp,ctr,cpc,stats_cost)

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

    mainWeb(next_url)
    # test()

if __name__ == '__main__':
    main()

