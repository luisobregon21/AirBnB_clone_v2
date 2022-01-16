#!/usr/bin/python3
'''
creates and distributes an archive to your web servers,
using the function deploy
'''


from datetime import datetime
# corre el comando dado, donde estes parado
from fabric.api import local, run, put
# verifies if it's a directory
from os.path import isdir
# corre el comando dado, donde estes parado
from os import path
import os

os.environ.hosts = ["34.139.237.184", "3.80.64.94"]


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


def do_deploy(archive_path):
    """ deploys archive to web server"""

    if path.exists(archive_path):
        try:
            # uploads file to given directory
            put(archive_path, '/tmp/')
            ''' versions/web_static_2022113185539.tgz '''
            filename = archive_path[9:]
            no_tgz = filename[:-4]
            final_name = '/data/web_static/releases/' + no_tgz + '/'

            # creates a directory
            run('mkdir -p ' + final_name)

            # Uncompresses the archive
            run('tar -xzf /tmp/' + filename + ' -C ' + final_name)
            # Deletes archive
            run('rm -f /tmp/' + filename)
            # moves all uncompressed archive
            run('mv ' + final_name + '/web_static/* ' + final_name)
            # Deletes symbolic link
            run('rm -rf /data/web_static/current')
            # create a new symbolic link
            run('ln -s ' + final_name + ' /data/web_static/current')
            print('New version deployed!')
            return True
        except:
            return False
    else:
        return False


def deploy():
    ''' creates and distributes an archive to your web servers '''
    name = do_pack()

    if name is None:
        return False
    return do_deploy(name)
