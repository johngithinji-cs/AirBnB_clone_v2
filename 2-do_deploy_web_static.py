#!/usr/bin/python3
"""Fab script"""
import os
from datetime import datetime
from fabric.api import *

env.hosts = ["3.236.245.170", " 34.226.233.255"]
env.user = "ubuntu"

def do_pack():
    """Packs web_static into tgz"""
    current_time = datetime.now().strftime("%Y%m%d%H%M%S")
    file_path = "versions/web_static_" + current_time + ".tgz"
    local("mkdir -p versions")
    local("tar -cvzf " + file_path + " web_static")
    if os.path.exists(file_path):
        return file_path
    else:
        return None


def do_deploy(archive_path):
    """Deploys archive to web servers"""
    if not os.path.exists(archive_path) and not os.path.isfile(archive_path):
        return False

    temp = archive_path.split('/')
    temp0 = temp[1].split(".")
    f = temp0[0]

    try:
        put(archive_path, "/{}.tgz".format(f))
        run("mkdir -p /data/web_static/releases/{}/".format(f))
        run("tar -xzf /tmp/{}.tgz" -C /data/web_static/releases/{}/".format(f,f))
        run("rm /tmp/{}.tgz".format(f))
        run("mv /data/web_static/releases/{}"
            "/web_static/* /data/web_static/releases/{}".format(f,f))
        run("rm -rf /data/web_static/releases/{}//web_static".format(f))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}//data/web_static/current".format(f))
        print("New version deployed!")
        return True
    except:
        return False

    return True
