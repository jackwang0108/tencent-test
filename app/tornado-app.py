import tornado.ioloop
import tornado.web


class TestHandler(tornado.web.RequestHandler):
    def get(self):
        a = self.get_argument("a", default=None)
        b = self.get_argument("b", default=None)

        if b is None:
            self.write(
                {
                    "error_code": "1",
                    "error_message": "Parameter 'b' is required",
                    "reference": None,
                }
            )
        else:
            self.write(
                {"error_code": "0", "error_message": "success", "reference": "111"}
            )


def make_app():
    return tornado.web.Application(
        [
            (r"/test", TestHandler),
        ]
    )


if __name__ == "__main__":
    app = make_app()
    app.listen(5000, "127.0.0.1")
    tornado.ioloop.IOLoop.current().start()
