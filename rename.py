'''
  When starting a new project, you will likely want to change the name
  of your Remote Script from "RemoteScriptStarter" - however this requires
  you to change the name in several places and to make a mistake may cause
  the script to not work.

  This script takes one optional argument, the name of what you want your
  project to be and changes all occurrences or "RemoteScriptStarter" to the
  new name. If no name is supplied then this script will take the name of
  the root directory. Use the `--name` flag to specify this name.

  If you would like to rename your project again, after the initial rename
  from "RemoteScriptStarter", use the `--old` flag
'''

import os
import argparse

currentDir = os.getcwd()
srcDir = os.path.join(currentDir, 'src')

parser = argparse.ArgumentParser()
parser.add_argument('--name', required=False)
parser.add_argument('--old', required=False)

oldName = parser.parse_args().old or "RemoteScriptStarter"
newName = parser.parse_args().name or os.path.basename(currentDir)

for fileName in os.listdir(srcDir):
    with open(os.path.join(srcDir, fileName), 'r') as file:
        filedata = file.read()

    filedata = filedata.replace(
        oldName,
        newName
    )

    with open(os.path.join(srcDir, fileName), 'w') as file:
        file.write(filedata)

    if (fileName == oldName + ".py"):
        os.rename(
            os.path.join("src", oldName + ".py"),
            os.path.join("src", newName + ".py")
        )

print("""
    Your remote script was successfully renamed from {oldName} to {newName}
""".format(oldName=oldName, newName=newName))
