from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import urllib.request
import time
import mysql.connector


chrome_options = Options()
# chrome_options.add_argument("user-data-dir=selenium")
chrome_options.headless = True

driver = webdriver.Chrome(
    executable_path="/Users/farhanpirzada/PycharmProjects/Electron-Python/OFF-WHITE/chromedriver",
    chrome_options=chrome_options
   )
driver.delete_all_cookies()

bb = 0
prvious_link = "test"


def nextPage(href, Category):

    try:
        print(Category)

        driver.execute_script("window.open('about:blank','tab2');")
        driver.switch_to.window("tab2")
        driver.get(href)

        Title = driver.find_element_by_css_selector(".product__title")
        Title = Title.text
        Title = Title.title()
        print(Title)

        price = driver.find_element_by_id("ProductPrice")
        price = price.text
        price = price.replace("Only","")
        price = price.replace("exc VAT", "")
        price = price.replace(" ", "")
        price = price.replace("£","")
        print(price)

        try:
            product_code = driver.find_element_by_css_selector(".product__skuWrap")
            product_code = product_code.text
            print(product_code)
        except:
            product_code = ""

        try:
            des = driver.find_element_by_css_selector(".product-description.rte")
            des = des.get_attribute("innerHTML")
            print(des)
        except:
            des = ""

        print("inside the img")
        imgs = driver.find_element_by_id("ProductPhoto")
        img = imgs.find_element_by_tag_name("img")
        # img = imgs.find_element_by_tag_name("img")
        print(img.get_attribute("src"))
        print("inside the for")
        img_scr = img.get_attribute("src")
        print(img_scr)

        image_name = Title.replace("/", "")
        image_url = image_name.replace(" ", "")
        image_url = ''.join(e for e in image_url if e.isalnum())
        image_name = image_name.replace(" ", "") + '.jpg'
        urllib.request.urlretrieve(img_scr, image_name)

        print(image_name)

        complete_des = des
        # print(complete_des)
        NULL_VALUE = None
        # backend direct into db
        import mysql.connector

        mydb = mysql.connector.connect(host='localhost',
                                       database='viking',
                                       user='root',
                                       password='root')

        mycursor = mydb.cursor()

        sql = "INSERT INTO products(product_name,product_description,meta_title,meta_description,status,rank,category_id,created_by,updated_by,feature_image,IsHome,IsFeature,IsSpecial,product_url,views,google_description,feed_status,warranty,pro_price,matting_text,minimum_qty,model_id) " \
              "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

        args = (
            Title, complete_des, Title, Title, 'Yes', NULL_VALUE, Category, '1', '1', image_name, 'Yes', 'Yes',
            'Yes', image_url, '0', NULL_VALUE, 'Yes', 'No Warranty', price, NULL_VALUE, 1, product_code)

        mycursor.execute(sql, args)

        mydb.commit()

        print(mycursor.rowcount, "record(s) affected")

        print('--------- ADDED ----------')

        driver.switch_to.window("tab1")

    except:
        print("No link")



def mainWeb(next_url, Category, prvious_link):
    driver.execute_script("window.open('about:blank','tab1');")
    driver.switch_to.window("tab1")
    driver.get(next_url)

    print(Category)

    try:
        print("inside")
        try:
            WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".rte.rte--header.colldesc.collectiondescription"))
            )
            data = driver.find_element_by_css_selector(".rte.rte--header.colldesc.collectiondescription")
            print(data)
        except:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".rte.rte--header.colldesc"))
            )
            data = driver.find_element_by_css_selector(".rte.rte--header.colldesc")
            print(data)

        Links = data.find_elements_by_tag_name("table")
        Links = Links[1]
        print(Links)
        Links = data.find_elements_by_tag_name("a")
        print("a")
        for table in Links:
            # table = table.find_element_by_tag_name("a")
            try:
                table = table.get_attribute("href")
                if ".aspx" in table:
                    print(table)
                    nextPage(table,Category)
                else:
                    pass
            except:
                print("No Link ex")

    except:

        print("except")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".grid-uniform"))
        )
        data = driver.find_element_by_css_selector(".grid-uniform")

        # products = data.find_elements_by_css_selector(".grid__item.large--one-third.medium--one-half")

        products = data.find_elements_by_css_selector("a.grid__image")

        for product in products:
            product = product.get_attribute("href")
            print(product)
            nextPage(product,Category)



    try:

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "row"))
        )
        next_page = driver.find_element_by_css_selector(".toolbar.toolbar-products")
        next_page = next_page.find_element_by_css_selector(".pages")
        next_page = next_page.find_element_by_xpath("//li[@class='item pages-item-next']")
        next = next_page.find_element_by_tag_name("a")
        next = next.get_attribute("href")

        print(next)
        print(prvious_link)
        if prvious_link != next:
            prvious_link = next
            mainWeb(next, Category, prvious_link)
    except:
        pass


    driver.switch_to.window("tab1")

def main():

    prvious_link = ''
    next_url = 'https://www.vikingtapes.co.uk/collections/3M-4957-VHB-Acrylic-Foam-tape'
    print(next_url)
    Category = '553'

    mainWeb(next_url, Category, prvious_link)
    # test()

if __name__ == '__main__':
    main()

