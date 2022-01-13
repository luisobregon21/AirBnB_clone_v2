#!/usr/bin/python3
'''
script generates a .tgz archive from the contents
of the web_static folder of your AirBnB Clone repo,
using the function do_pack
'''

from datetime import datetime
# corre el comando dado, donde estes parado
from fabric.api import local
# verifies if it's a directory
from os.path import isdir


def do_pack():
    """ generates a tgz archive from the contents of web_static """
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        # verify if versions directory exists
        if isdir("versions") is False:
            local("mkdir versions")
        name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(name))
        return name
    except:
        return None
