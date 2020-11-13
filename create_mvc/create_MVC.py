import os
from os import listdir
from os.path import isfile, join
import json
from jinja2 import Template

def my_create_all():
    migration_path = "./apiNodejs/app/migration"
    files = [f for f in listdir(migration_path) if isfile(join(migration_path, f))]
    files.remove("init-models.js")
    for f in files:
        my_object = create_object(migration_path + "/" + f)
        my_object.remove("id")
        create_route(my_object)
        create_controller(my_object)
        create_model(my_object)
        create_server()

def create_object(file):
    table_line = []
    table_line.append(file.split('/')[-1].split('.')[0])
    with open(file) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            if ": {" in line:
                table_line.append(line.split(':')[0].strip()) # take the name and remove the space
            line = fp.readline()
            cnt += 1
    return (table_line)

def checkFileExistance(filePath):
    try:
        with open(filePath, 'r') as f:
            return (True)
    except FileNotFoundError as e:
        return False
    except IOError as e:
        return (False)

def create_route(table_line):
    route_path = "./apiNodejs/app/routes/"
    template_path = "./create_mvc/templates/template.route.txt"
    my_file = open(template_path, 'r')
    template = Template(my_file.read())
    content = template.render(name=table_line[0],capiName=table_line[0].capitalize())
    my_file.close()
    if checkFileExistance(route_path + table_line[0] + ".route.js"):
        print("Error 1: Route [{}.js] is existing, maybe create a backup of this file and change is name".format(route_path + table_line[0] + ".route"))
        return (False)
    else:
        with open(route_path + table_line[0] + ".route.js", "w") as fp:
            fp.write(content)
    return (True)

def create_controller(table_line):
    route_path = "./apiNodejs/app/controllers/"
    template_path = "./create_mvc/templates/template.controller.txt"
    my_file = open(template_path)
    template = Template(my_file.read())
    content = template.render(name=table_line[0],capiName=table_line[0].capitalize(), content_table=table_line[1:])
    my_file.close()
    if checkFileExistance(route_path + table_line[0] + ".controller.js"):
        print("Error 2: Controller [{}.js] is existing, maybe create a backup of this file and change is name".format(route_path + table_line[0] + ".controller"))
        return (False)
    else:
        with open(route_path + table_line[0] + ".controller.js", "w") as fp:
            fp.write(content)
    return (True)

def create_model(table_line):
    route_path = "./apiNodejs/app/models/"
    template_path = "./create_mvc/templates/template.model.txt"
    my_file = open(template_path)
    template = Template(my_file.read())
    content = template.render(name=table_line[0],capiName=table_line[0].capitalize(), content_table=table_line[1:])
    my_file.close()
    if checkFileExistance(route_path + table_line[0] + ".model.js"):
        print("Error 3: Model [{}.js] is existing, maybe create a backup of this file and change is name".format(route_path + table_line[0] + ".model"))
        return (False)
    else:
        with open(route_path + table_line[0] + ".model.js", "w") as fp:
            fp.write(content)
    return (True)

def create_server():
    route_path = "./apiNodejs/app/routes/"
    template_path = "./create_mvc/templates/template.server.txt"
    files = [f for f in listdir(route_path) if isfile(join(route_path, f))]
    my_file = open(template_path)
    template = Template(my_file.read())
    content = template.render(route_list=files)
    with open('./apiNodejs/server.js', "w") as fp:
        fp.write(content)
    print("Your server is created and running on port 3000 check the localhost:3000 !")

# def create_myroad():
    

my_create_all()