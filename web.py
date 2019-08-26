import tornado.web
import tornado.ioloop
import click
from time import sleep
# import playground
import os.path
import main
import playground
import urllib3
urllib3.disable_warnings()
import logging
logging.getLogger('requests.packages.urllib3.connectionpool').setLevel(logging.CRITICAL)

class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")
        self.callFunc()

    def callFunc(self):
        data = playground.main()
        print(data)
        print("in basicRequest")


class AllProduct(tornado.web.RequestHandler):
    def get(self):
        data = False
        product = main.mainWeb(data)
        self.render("feedPage.html",product=product)


class Dashboard(tornado.web.RequestHandler):
    def get(self):
        name = self.get_argument("name")
        print(name)

        self.render("dashboard.html")



if __name__ == "__main__":
    favicon_path = '/Users/farhanpirzada/PycharmProjects/Express-matting/google-feed-automation/'  # Actually the directory containing the favicon.ico file

    settings = dict(
        # template_path=os.path.join(os.path.dirname(__file__),"production"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        debug = True
    )

    app = tornado.web.Application([
        (r"/", basicRequestHandler),
        (r"/dashboard", Dashboard),
        (r"/AllProduct", AllProduct),
    ],**settings)

    app.listen(8881)
    print("I'm listening on port 8881")
    tornado.ioloop.IOLoop.current().start()