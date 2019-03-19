import os
import tornado.web

from python3.properties.url import url

settings = dict(
    cookie_secret="61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
    template_path = os.path.join(os.path.dirname(__file__), "../../resource/webpage/templates"),
    static_path = os.path.join(os.path.dirname(__file__), "../../resource/webpage"),
    data_path=os.path.join(os.path.dirname(__file__), "../../resource/uploadfile")
)

application=tornado.web.Application(
    handlers =url,
    **settings
)