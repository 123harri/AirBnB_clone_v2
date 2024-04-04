#!/usr/bin/python3
"""
Fabric script to distribute an archive to web servers
Usage: fab -f 2-do_deploy_web_static.py do_deploy:/path/to/archive.tgz
"""

from fabric.api import put, run, env
from os.path import exists

env.hosts = ['54.89.109.87', '100.25.190.21']


def do_deploy(archive_path):
    """
    Distributes an archive to the web servers
    Args:
        archive_path (str): Path to the archive file

    Returns:
        bool: True if successful, False otherwise
    """
    if not exists(archive_path):
        return False

    try:
        # Get filename and directory name
        filename = archive_path.split("/")[-1]
        dirname = filename.split(".")[0]

        # Upload archive to /tmp directory of web server
        put(archive_path, "/tmp")

        # Create directory for extraction
        run("mkdir -p /data/web_static/releases/{}".format(dirname))

        # Extract archive to /data/web_static/releases/<dirname>
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(filename, dirname))

        # Delete archive from web server
        run("rm /tmp/{}".format(filename))

        # Move contents to correct directory
        run("mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/"
            .format(dirname, dirname))

        # Delete old symbolic link
        run("rm -rf /data/web_static/current")

        # Create new symbolic link
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(dirname))

        print("New version deployed!")
        return True
    except Exception as e:
        print(e)
        return False
