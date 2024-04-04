#!/usr/bin/python3
"""
Deletes out-of-date archives
fab -f 100-clean_web_static.py do_clean:number=2
    -i ssh-key -u ubuntu > /dev/null 2>&1
"""

import os
from fabric.api import *

env.hosts = ['52.87.155.66', '54.89.109.87']


def do_clean(number=0):
    """Delete out-of-date archives.
    Args:
        number (int): The number of archives to keep.
    If number is 0 or 1, keeps only the most recent archive. If
    number is 2, keeps the most and second-most recent archives,
    etc.
    """
    number = 1 if int(number) == 0 else int(number)

    # Clean local archives
    local_archives = sorted(os.listdir("versions"))
    for archive in local_archives[:-number]:
        local("rm versions/{}".format(archive))

    # Clean remote archives
    with cd("/data/web_static/releases"):
        run_archives = run("ls -tr").split()
        run_archives = [a for a in run_archives if "web_static_" in a]
        for archive in run_archives[:-number]:
            run("rm -rf {}".format(archive))
