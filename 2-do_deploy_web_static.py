#!/usr/bin/python3
"""
Fabric script to distribute an archive to web servers.
"""
from fabric.api import *
import os

# Define the username and SSH key file
env.user = 'ubuntu'
env.key_filename = '/path/to/your/ssh/private/key'

# List of web server IP addresses
env.hosts = ['107.21.37.236', '54.89.179.235']

def do_deploy(archive_path):
    """
    Distribute an archive to web servers and deploy it.
    """
    if not os.path.exists(archive_path):
        return False

    # Extract the filename from the archive path
    archive_filename = os.path.basename(archive_path)
    archive_no_ext = os.path.splitext(archive_filename)[0]

    try:
        # Upload the archive to /tmp/ directory on the web server
        put(archive_path, '/tmp/')

        # Create the target directory for deployment
        run('mkdir -p /data/web_static/releases/{}'.format(archive_no_ext))

        # Extract the archive to the target directory
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}'.format(archive_filename, archive_no_ext))

        # Remove the uploaded archive
        run('rm /tmp/{}'.format(archive_filename))

        # Move the contents from the extracted folder to the target directory
        run('mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}'.format(archive_no_ext, archive_no_ext))

        # Remove the empty folder
        run('rm -rf /data/web_static/releases/{}/web_static'.format(archive_no_ext))

        # Remove the current symlink if it exists
        run('rm -rf /data/web_static/current')

        # Create a new symlink to the deployed version
        run('ln -s /data/web_static/releases/{} /data/web_static/current'.format(archive_no_ext))

        print("New version deployed!")
        return True

    except Exception as e:
        return False

