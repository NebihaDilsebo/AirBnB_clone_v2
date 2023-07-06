from fabric.api import local
from datetime import datetime


def do_pack():
    """Create a .tgz archive from the contents of web_static folder."""
    # Create the versions folder if it doesn't exist
    local("mkdir -p versions")

    # Generate the name of the archive
    now = datetime.now()
    archive_name = "web_static_{}.tgz".format(
        now.strftime("%Y%m%d%H%M%S")
    )
    
    # Compress the web_static folder into the archive
    result = local("tar -czvf versions/{} web_static".format(archive_name))

    if result.failed:
        return None

    return "versions/{}".format(archive_name)

