#!/usr/bin/python3
"""
This script deploys my static files to my servers using Fabric
"""


from fabric.api import env, run, put
from os import path


env.hosts = ["34.207.156.32", "52.91.133.128"]


def do_deploy(archive_path):
    """Distributes an archive to your web servers
    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """
    if path.exists(archive_path) is False:
        return False
    f = archive_path.split("/")[1]
    f_n = f.split(".")[0]
    dest_f = "/data/web_static/releases/"

    if put(archive_path, "/tmp/{}".format(f)).failed is True:
        return False
    if run("rm -rf {}{}/".format(dest_f, f_n)).failed is True:
        return False
    if run("mkdir -p {}{}".format(dest_f, f_n)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C {}{}".format(f, dest_f, f_n)).failed is True:
        return False
    if run("rm -rf /tmp/{}".format(f_n)).failed is True:
        return False
    if run("mv {}{}/web_static/* {}{}/".format(dest_f,
                                               f_n,
                                               dest_f,
                                               f_n)).failed is True:
        return False
    if run("rm -rf {}{}/web_static".format(dest_f, f_n)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s {}{} /data/web_static/current".format(dest_f,
                                                        f_n)).failed is True:
        return False
    return True
