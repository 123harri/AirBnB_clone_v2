#!/usr/bin/python3
"""
Fabric script to create and distribute an archive to web servers
Usage: fab -f 3-deploy_web_static.py deploy
"""

from fabric.api import local, env, put, run
from os.path import exists
from datetime import datetime

env.hosts = ['100.25.188.51', '54.209.116.96']
env.user = 'ubuntu'

def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder
    Returns:
        str: Archive path if created successfully, None otherwise
    """
    try:
        # Create the versions folder if it doesn't exist
        local("mkdir -p versions")

        # Generate the timestamp for the archive name
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

        # Create the archive
        archive_name = "web_static_{}.tgz".format(timestamp)
        local("tar -cvzf versions/{} web_static".format(archive_name))

        # Return the archive path if created successfully
        return "versions/{}".format(archive_name)
    except Exception as e:
        print(e)
        return None


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


def deploy():
    """
    Creates and distributes an archive to web servers
    """
    # Call do_pack and store the path of the created archive
    archive_path = do_pack()
    if archive_path is None:
        return False

    # Call do_deploy using the new path of the new archive
    return do_deploy(archive_path)


if __name__ == "__main__":
    deploy()
