import tornado.web
import tornado.ioloop
import click
from time import sleep
import os.path
import main
import urllib3
import logging
from tornado.ioloop import IOLoop
import tornado.httpserver
import aiohttp
from tornado.platform.asyncio import AsyncIOMainLoop
import asyncio
import click

urllib3.disable_warnings()
logging.getLogger('requests.packages.urllib3.connectionpool').setLevel(logging.CRITICAL)
hn = logging.NullHandler()
hn.setLevel(logging.DEBUG)
logging.getLogger("tornado.access").addHandler(hn)
logging.getLogger("tornado.access").propagate = False

class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")
        self.callFunc()

    def callFunc(self):
        print("in basicRequest")


class AllProduct(tornado.web.RequestHandler):

    def get(self):

        while True:
            print("in the get method")
            # await self.post()
            # for direct data

            # data = False
            # product = main.mainWeb(data)
            # for pro in product:
            #     pass
            #     # print(pro)
            #     # print(type(pro))
            # product_group = main.product_group()
            # for pro in product_group:
            #     pass
            #     # print(pro)
            #     # print(type(pro))
            # print("end")
            #
            # self.render("feedPage.html",product = product, product_group = product_group)
            # # sleep(200)
            # break

            # end

            # with database
            #

            # data = False
            # await main.mainWeb(data)
            # await main.product_group()

            #
            # conn = yield tornado_mysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='feedOPT')
            # cur = conn.cursor()
            # yield cur.execute("SELECT * FROM product")
            # print(cur.description)
            # for row in cur:
            #     print(row)
            # cur.close()
            # conn.close()

            #strat database entry
            day = "Please Select"
            import mysql.connector

            mydb = mysql.connector.connect(host='localhost',
                                           database='feedOPT',
                                           user='root',
                                           password='root')

            mycursor = mydb.cursor()

            mycursor.execute("SELECT * FROM Today")
            product = mycursor.fetchall()

            # for s in product:
            #     print(s)

            mydb = mysql.connector.connect(host='localhost',
                                           database='feedOPT',
                                           user='root',
                                           password='root')

            mycursor = mydb.cursor()

            mycursor.execute("SELECT * FROM product_group")
            product_group = mycursor.fetchall()

            self.render("feedPage.html", product = product, product_group = product_group, day= day)
            # sleep(200)
            break

    def post(self):
        try:
            id = self.get_argument("id_number")
            print(id)
            cpc = self.get_argument("cpc")
            print(cpc)
            data_type = False
            click.mainWeb(data_type,cpc,id)
            self.get()


            # test = False
            # await mainWeb(test)

        except:
            print("no argument in post")
            # await self.post()

        try:
            day = self.get_argument("Day")
            print(day)
            if day == "Today":
                import mysql.connector

                mydb = mysql.connector.connect(host='localhost',
                                               database='feedOPT',
                                               user='root',
                                               password='root')

                mycursor = mydb.cursor()

                mycursor.execute("SELECT * FROM Today")
                product = mycursor.fetchall()

                # for s in product:
                #     print(s)

                mydb = mysql.connector.connect(host='localhost',
                                               database='feedOPT',
                                               user='root',
                                               password='root')

                mycursor = mydb.cursor()

                mycursor.execute("SELECT * FROM product_group")
                product_group = mycursor.fetchall()

                self.render("feedPage.html", product=product, product_group=product_group, day= day)
                # sleep(200)
            elif day == "Yesterday":
                import mysql.connector

                mydb = mysql.connector.connect(host='localhost',
                                               database='feedOPT',
                                               user='root',
                                               password='root')

                mycursor = mydb.cursor()

                mycursor.execute("SELECT * FROM Yesterday")
                product = mycursor.fetchall()

                # for s in product:
                #     print(s)

                mydb = mysql.connector.connect(host='localhost',
                                               database='feedOPT',
                                               user='root',
                                               password='root')

                mycursor = mydb.cursor()

                mycursor.execute("SELECT * FROM product_group")
                product_group = mycursor.fetchall()

                self.render("feedPage.html", product=product, product_group=product_group, day= day)
                # sleep(200)
            elif day == "ThisWeek":
                import mysql.connector

                mydb = mysql.connector.connect(host='localhost',
                                               database='feedOPT',
                                               user='root',
                                               password='root')

                mycursor = mydb.cursor()

                mycursor.execute("SELECT * FROM This_week")
                product = mycursor.fetchall()

                # for s in product:
                #     print(s)

                mydb = mysql.connector.connect(host='localhost',
                                               database='feedOPT',
                                               user='root',
                                               password='root')

                mycursor = mydb.cursor()

                mycursor.execute("SELECT * FROM product_group")
                product_group = mycursor.fetchall()

                self.render("feedPage.html", product=product, product_group=product_group, day= day)
                # sleep(200)
            elif day == "Last7":
                import mysql.connector

                mydb = mysql.connector.connect(host='localhost',
                                               database='feedOPT',
                                               user='root',
                                               password='root')

                mycursor = mydb.cursor()

                mycursor.execute("SELECT * FROM Last7days")
                product = mycursor.fetchall()

                # for s in product:
                #     print(s)

                mydb = mysql.connector.connect(host='localhost',
                                               database='feedOPT',
                                               user='root',
                                               password='root')

                mycursor = mydb.cursor()

                mycursor.execute("SELECT * FROM product_group")
                product_group = mycursor.fetchall()

                self.render("feedPage.html", product=product, product_group=product_group, day= day)
                # sleep(200)
            elif day == "LastWeek":
                import mysql.connector

                mydb = mysql.connector.connect(host='localhost',
                                               database='feedOPT',
                                               user='root',
                                               password='root')

                mycursor = mydb.cursor()

                mycursor.execute("SELECT * FROM Lastweek_Sun_Sat")
                product = mycursor.fetchall()

                # for s in product:
                #     print(s)

                mydb = mysql.connector.connect(host='localhost',
                                               database='feedOPT',
                                               user='root',
                                               password='root')

                mycursor = mydb.cursor()

                mycursor.execute("SELECT * FROM product_group")
                product_group = mycursor.fetchall()

                self.render("feedPage.html", product=product, product_group=product_group, day= day)
                # sleep(200)
            elif day == "Last14":
                import mysql.connector

                mydb = mysql.connector.connect(host='localhost',
                                               database='feedOPT',
                                               user='root',
                                               password='root')

                mycursor = mydb.cursor()

                mycursor.execute("SELECT * FROM Last14days")
                product = mycursor.fetchall()

                # for s in product:
                #     print(s)

                mydb = mysql.connector.connect(host='localhost',
                                               database='feedOPT',
                                               user='root',
                                               password='root')

                mycursor = mydb.cursor()

                mycursor.execute("SELECT * FROM product_group")
                product_group = mycursor.fetchall()

                self.render("feedPage.html", product=product, product_group=product_group, day= day)
                # sleep(200)
            elif day == "ThisMonth":
                import mysql.connector

                mydb = mysql.connector.connect(host='localhost',
                                               database='feedOPT',
                                               user='root',
                                               password='root')

                mycursor = mydb.cursor()

                mycursor.execute("SELECT * FROM Thismonth")
                product = mycursor.fetchall()

                # for s in product:
                #     print(s)

                mydb = mysql.connector.connect(host='localhost',
                                               database='feedOPT',
                                               user='root',
                                               password='root')

                mycursor = mydb.cursor()

                mycursor.execute("SELECT * FROM product_group")
                product_group = mycursor.fetchall()

                self.render("feedPage.html", product=product, product_group=product_group, day= day)
                # sleep(200)
            elif day == "Last30":
                import mysql.connector

                mydb = mysql.connector.connect(host='localhost',
                                               database='feedOPT',
                                               user='root',
                                               password='root')

                mycursor = mydb.cursor()

                mycursor.execute("SELECT * FROM Last30days")
                product = mycursor.fetchall()

                # for s in product:
                #     print(s)

                mydb = mysql.connector.connect(host='localhost',
                                               database='feedOPT',
                                               user='root',
                                               password='root')

                mycursor = mydb.cursor()

                mycursor.execute("SELECT * FROM product_group")
                product_group = mycursor.fetchall()

                self.render("feedPage.html", product=product, product_group=product_group, day= day)
                # sleep(200)
            elif day == "LastMonth":
                import mysql.connector

                mydb = mysql.connector.connect(host='localhost',
                                               database='feedOPT',
                                               user='root',
                                               password='root')

                mycursor = mydb.cursor()

                mycursor.execute("SELECT * FROM Lastmonth")
                product = mycursor.fetchall()

                # for s in product:
                #     print(s)

                mydb = mysql.connector.connect(host='localhost',
                                               database='feedOPT',
                                               user='root',
                                               password='root')

                mycursor = mydb.cursor()

                mycursor.execute("SELECT * FROM product_group")
                product_group = mycursor.fetchall()

                self.render("feedPage.html", product=product, product_group=product_group, day= day)
                # sleep(200)
            elif day == "Alltime":
                import mysql.connector

                mydb = mysql.connector.connect(host='localhost',
                                               database='feedOPT',
                                               user='root',
                                               password='root')

                mycursor = mydb.cursor()

                mycursor.execute("SELECT * FROM Alltime")
                product = mycursor.fetchall()

                # for s in product:
                #     print(s)

                mydb = mysql.connector.connect(host='localhost',
                                               database='feedOPT',
                                               user='root',
                                               password='root')

                mycursor = mydb.cursor()

                mycursor.execute("SELECT * FROM product_group")
                product_group = mycursor.fetchall()

                self.render("feedPage.html", product=product, product_group=product_group, day= day)
                # sleep(200)

            # test = False
            # await mainWeb(test)

        except:
            print("no argument in post in days too")
            # await self.post()


class Dashboard(tornado.web.RequestHandler):
    def get(self):
        name = self.get_argument("name")
        print(name)

        self.render("dashboard.html")


class Table(tornado.web.RequestHandler):
    def get(self):
        try:
            n = self.get_argument("n")
            print(n)
        except:
            print("nothing to print")
        # self.render("tables_dynamic.html")


class EidtPage(tornado.web.RequestHandler):
    def post(self):
        try:
            id = self.get_argument("cpcc")
            print(id)


        except:
            print("nothing to print")
        # self.render("tables_dynamic.html")


if __name__ == "__main__":
    favicon_path = '/Users/farhanpirzada/PycharmProjects/Express-matting/google-feed-automation/'  # Actually the directory containing the favicon.ico file
    AsyncIOMainLoop().install()

    settings = dict(
        # template_path=os.path.join(os.path.dirname(__file__),"production"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        debug = True
    )

    app = tornado.web.Application([
        (r"/", basicRequestHandler),
        (r"/dashboard", Dashboard),
        (r"/AllProduct", AllProduct),
        (r"/EidtPage", EidtPage),


    ],**settings)

    # app.listen(8881)
    # tornado.ioloop.IOLoop.current().start()
    server = tornado.httpserver.HTTPServer(app)
    server.bind(8881, '127.0.0.1')
    server.start()
    print("I'm listening on port 8881")
    asyncio.get_event_loop().run_forever().start()
