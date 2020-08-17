#!/usr/bin/python3
"""  Fabric script that generates a .tgz archive from the contents
     of the web_static folder of your AirBnB Clone repo """
from fabric.api import *
from os import path
from datetime import datetime


def do_pack():
    """ function """
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    local("mkdir versions")
    f = "versions/web_static_{}.tgz".format(time)
    local("tar czvf {} web_static".format(f))
    if path.exists(f):
        return f
    else:
        return None
