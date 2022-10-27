#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of
the web_static folder 
"""


from os import path
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    this function generates a .tgz archive from the contents of
    of the web_static folder of AirBnB clone
    """
    time = datetime.utcnow()
    file_name = "versions/web_static_{}{}{}{}{}{}.tgz".format(time.year,
                                                          time.month,
                                                          time.day,
                                                          time.hour,
                                                          time.minute,
                                                          time.second)

    if path.exists("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file_name)).failed is True:
        return None
    return file_name