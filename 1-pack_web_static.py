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
        date = datetime.now().strftime('%Y%m%d%H%M%S')
        if isdir('versions') is False:
            # create version folder
            local('mkdir versions')
        file_name = f"versions/web_static{date}.tgz"
        local(f'tar -cvzf {file_name} web_static')
        return file_name
    except:
        return None
