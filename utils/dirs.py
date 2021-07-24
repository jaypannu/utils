import os
import sys
import getpass

homedir = os.path.expanduser("~")
logdir = os.path.join(homedir, 'log')
datadir = os.path.join(homedir, 'data')
resdir = os.path.join(homedir, 'output')

def mkdir(path, *args, **kwargs):
    if not os.path.exists(path):
        os.mkdir(path, *args, **kwargs)


mkdir(logdir)
mkdir(datadir)
mkdir(resdir)