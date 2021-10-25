import config.version
from config import *
import os, sys


def cmd_version():
    print("the version of cmd is: "+ config.version.version)

def cmd_no_shutdown():
    os.system("shutdown /a")
