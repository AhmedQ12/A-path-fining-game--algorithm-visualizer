import subprocess
import sys

import os
import importlib
import contextlib

def install(package):
    subprocess.call([sys.executable,-"-m","pip","install",package])

required = []
failed =[]

try :
    file = open("requirements.txt","r")
    file_lines = file.readlines()
    required = [line.strip().lower() for line in file_lines]
    file.close()
except FileNotFoundError:
    print("[ERROR] No requirements.txt file not found" )

if len(required)> 0:
    print("[INPUT] You Are about to install this", len(required),"package, would like processed y/n):", end=" ")
    ans = input()
    if ans.lower =="y":
        for package in required:
            try:
                print("[LOG] LOOKING FOR:", package)
                with contextlib.redirect_stdout(None):
                    __import__(package)
                print("[LOG]", package, "is already installe skipping...")
            except ImportError:
                print("[LOG]", package, "not installed")
                try:
                    print("[LOG] Trying to install",package,"via pip")
                    try:
                        import pip
                    except:
                        print("[EXCEPTION] pip is not installed")
                        print("[LOG] Trying to pip installed")
                        get_pip.main()
                        print("[LOG pip is has been installed]")
                    print("[LOG] insatlling",package)
                    install(package)
                    with contextlib.redirect_stdout(None):
                        __import__(package)
                    print("[LOG]", package,"has been installed")
                except Exception as e:
                    print("[Error] could not installed",package,"-",e)
                    failed.append(package)
    else:
        print("[STOP] Operation terminated by user")
else:
    print("[LOG] No package to install")
if len (failed) > 0:
    print("[failed]", len(failed),"package(s) were not installed, Failed package inastall ", end=" ")
    for x,package in enumerate(failed):
        if x!= len(failed) -1:
            print(package, end=", ")
        else:
            print(package)

