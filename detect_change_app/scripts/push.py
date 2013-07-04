##############################################################################
## Intent: To be single point of contact for pushing the version to gae sever
## Date: 2013-06-29 Sat 11:08 AM
## Author: Ashish Anand
##############################################################################

import subprocess
import os
import argparse
from util_gae import FixSysPath, gae_sdk_path

WEBAPPDIR = os.path.normpath(os.path.join(os.environ["PHUNGSUKDIR"]))

def ParseArguments():
    p = argparse.ArgumentParser(description='Process some integers.')
    p.add_argument("-V", "--version", dest="version", required=True, help="version to update - dev/live")
    p.add_argument("--email", dest="email", required=True, help="email to use for upload")
    args = p.parse_args()


    return args

def main():
    args = ParseArguments()
    unitTestsPath = os.path.normpath(os.path.join(WEBAPPDIR, "scripts", "unittests.py"))
    subprocess.call("python {}".format(unitTestsPath))

    appcfgPath = os.path.normpath(os.path.join(gae_sdk_path, "appcfg.py"))
    updateCmd = "python \"{a}\" --version={v} --email={e} update {w}".format(a=appcfgPath, v=args.version,e=args.email, w=WEBAPPDIR)
    subprocess.call(updateCmd)
    return


if __name__ == '__main__':
    FixSysPath()
    main()
