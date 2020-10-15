#!/usr/bin/python3.8

from sys import argv
from os import mkdir, environ

def camelCaseUri(uri):
    return (uri.capitalize() + ".rs", uri + "Routes.rs")

def runCommand(args) -> None:
    if args[0] == "full":
        currentPath = environ["PWD"]
        mkdir(currentPath + "/models")
        mkdir(currentPath + "/routes")
        
        apiUri = input("\n Enter a name for the api URI you want to make\n-> ")
        modelName, routeName = camelCaseUri(apiUri)

        open(currentPath + "/models/" + modelName, "w+")
        open(currentPath + "/routes/" + routeName, "w+")
    
if __name__ == "__main__":
    try:
        runCommand(argv[1:])
    except IndexError:
        print("Fatal: script must contain atleast one argument.")
