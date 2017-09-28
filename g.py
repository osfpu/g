#!/usr/bin/python
# -*- coding: utf-8 -*-
import getopt, sys
import os
import json

home = os.environ['HOME'] + "/.g"
path_record_file_path = home + "/path_record_file.json"
if not os.path.exists(home):
    os.mkdir(home)
if not os.path.exists(path_record_file_path):
    path_record_file = open(path_record_file_path,'w')
    empty_records = {}
    path_record_file.write(json.dumps(empty_records))
    path_record_file.close()

def warning():
    print("Use \"goto --help\" to learn usage information")

def usage():
    print('''
    g [option] [value]
        -h or --help
        -l or --list        List all records.
        -r or --remove      Remove a record by key.
        -a or --add         Add a record to your current path. For example, use
                            `g -a 1` record the current path and you can use
                            `g 1` go back the path next time.
        --clear             Remove all records.
    ''')

def read():
    path_record_file = open(path_record_file_path, 'r')
    records = json.loads(path_record_file.read())
    path_record_file.close()
    return records

def write(records):
    path_record_file = open(path_record_file_path, 'w')
    path_record_file.write(json.dumps(records));
    path_record_file.close()

def show_list():
    records = read()
    print("\033[1;32;40m")
    for key in records:
        print(key + "       -------->      " + records[key])
    print("\033[0m")

def remove(target):
    records = read()
    if records.has_key(target):
        del records[target]
    write(records)

def add(target):
    records = read()
    records[target] = os.getcwd()
    write(records)

def goto(target):
    records = read()
    if records.has_key(target):
        print(records[target])

def clear():
    os.remove(path_record_file_path)

def main(argv):
    if (len(argv) <= 1):
        print(os.getcwd())
        exit()
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hlr:a:", ["help", "list", "remove=", "add=", "clear"])
    except getopt.GetoptError as err:
        print(str(err))
        warning()
        exit()

    for opt, val in opts:
        if opt in ( "-h", "--help" ):
            usage()
            exit()
        if opt in ( "-l", "--list" ):
            show_list()
            exit()
        if opt in ( "-r", "--remove" ):
            remove(val)
            exit()
        if opt in ( "-a", "--add" ):
            add(val)
            exit()
        if opt in ( "--clear" ):
            clear()
            exit()

    goto(args[0])

if __name__ == "__main__":
    main(sys.argv)
