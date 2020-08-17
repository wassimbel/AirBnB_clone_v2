#!/usr/bin/python3
""" Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to web servers """
from fabric.api import *
from os import path
from datetime import datetime


env.hosts = ['34.229.124.30', '34.73.6.154']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """ function to deploy """
    if not path.exists(archive_path):
        return False
    put("archive_path", "/tmp/")
    fp = archive_path.split('/')[-1].split('.')[0]
    run("mkdir -p /data/web_static/releases/fp")
    run("tar xzf /tmp/{}.tgz -C /data/web_static/releases/{}".format(fp, fp))
    run("rm -rf /tmp/{}".tgz.format(fp))
    run("mv /data/web/static/releases/{}/web_static/*\
        /data/web_static/releases/{}".format(fp, fp))
    run("rm -rf /data/web_static/current")
    run("run: rm -rf /data/web_static/releases/{}/web_static".format(fp))
    run("ln -sf /data/web_static/releases/{}\
         /data/web_static/current".format(fp))
    return True
