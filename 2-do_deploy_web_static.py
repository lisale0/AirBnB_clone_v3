#!/usr/bin/python3
"""
deploy
"""
import os
import time
from fabric.api import local, run, hosts, env, put

env.hosts = ['144.217.245.116', '54.91.123.178']


def do_deploy(archive_path):
    """
    deploy
    """
    if not archive_path:
        return False

    if not os.path.exists(archive_path):
        return False

    filename = archive_path.split("/")[-1]
    """upload the archive to the /tmp/ directory of the web server"""
    put(archive_path, "/tmp/{}".format(filename))

    """ make directory to uncompress files"""
    run("sudo mkdir -p /data/web_static/releases/{}".format(filename))

    """uncompress the archive to the folder"""
    run("sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}"
        .format(filename, filename))

    """ remove tgz file"""
    run("sudo rm /tmp/{}".format(filename))

    """ move all the files"""
    run("sudo mv /data/web_static/releases/{}/web_static/*"
        " /data/web_static/releases/{}"
        .format(filename, filename))

    """remove"""
    run("sudo rm -rf /data/web_static/releases/{}/web_static"
        .format(filename))

    run("sudo rm -rf /data/web_static/current")
    run("sudo ln -s /data/web_static/releases/{}/ /data/web_static/current"
        .format(filename))
    print("New version deployed!")
