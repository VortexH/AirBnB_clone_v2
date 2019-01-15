#!/usr/bin/python3
""" Contains a fabric function to generate a .tgz archive """


from fabric.api import local
import datetime


def do_pack():
    """ Takes the contents of web_static and creates an archive
        of all the files, stores the archives in the versions folder
        located within the root of the application, and
        names the archive like "web_static<year><month><day><hour>
        <minute><second>.tgz
    """
    local('mkdir -p versions')
    time = datetime.datetime.now().strftime("%Y,%m,%d,%I,%M,%S").split(',')
    archive_name = "web_static_{}{}{}{}{}{}.tgz".format(
        time[0], time[1], time[2], time[3], time[4], time[5])
    result = local('tar cvzf versions/{} web_static'.format(archive_name),
                   capture=True)
    if result.failed:
        return None
    else:
        return local('readlink -f versions/archive_name')
