#!/usr/bin/python3
""" Contains a fabric function to generate a .tgz archive """


from fabric.api import local, env, put, run
import datetime
from os.path import isfile, splitext

env.hosts = ['35.243.137.120', '35.227.93.69']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


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
    local('tar cvzf versions/{} web_static'.format(archive_name))
    return local('readlink -f versions/archive_name')


def do_deploy(archive_path):
    """
        Args: archive_path: the path to the archive created in do_pack


        Returns: False, if the file at the path archive_path doesn't exist


    """

    if isfile(archive_path) is False:
        return False
    no_extension = splitext(archive_path)[0]
    version_name = no_extension.split('/')[1]
    try:
        dir_str = "/data/web_static/releases"
        put(archive_path, "/tmp/")
        run("mkdir -p {0}/{1}".format(dir_str, version_name))
        run("tar -xzf /tmp/{0}.tgz -C {1}/{0}/".format(
            version_name, dir_str))
        run("rm /tmp/{}.tgz".format(version_name))
        run("mv {0}/{1}/web_static/* {0}/{1}".format(
            dir_str, version_name))
        run("rm -rf {0}/{1}/web_static".format(dir_str, version_name))
        run("rm -rf /data/web_static/current")
        run("ln -s {0}/{1} /data/web_static/current".format(
            dir_str, version_name))
        return True

    except:
        return False
