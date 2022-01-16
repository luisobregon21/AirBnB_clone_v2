#!/usr/bin/python3
'''
distributes an archive to your web servers, using the function do_deploy
'''

# corre el comando dado, donde estes parado
from fabric.api import run, put
# verifies if it's a directory
from os import path
import os


def do_deploy(archive_path):
    """ deploys archive to web server"""

    os.environ.hosts = ["34.139.237.184", "3.80.64.94"]

    if path.exists(archive_path) is False:
        return False
    else:
        try:
            # uploads file to given directory
            put(archive_path, '/tmp/')
            ''' versions/web_static_2022113185539.tgz '''
            filename = archive_path[9:]
            no_tgz = filename[:-4]
            final_name = '/data/web_static/releases/' + no_tgz +'/'

            # creates a directory
            run('mkdir -p ' + final_name)

            # Uncompresses the archive
            run('tar -xzf /tmp/' + filename + ' -C ' + final_name)
            # Deletes archive
            run('rm -rf ' + '/tmp/*.tgz')
            # moves all uncompressed archive
            run('mv ' + final_name + '/web_static/*' + final_name)
            # Deletes symbolic link
            run('rm -rf ' + '/data/web_static/current')
            # create a new symbolic link
            run('ln -s ' + final_name + '/data/web_static/current')
            print('New version deployed!')
            return True
        except:
            return False
