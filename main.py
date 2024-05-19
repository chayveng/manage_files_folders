import json

from utils.manage_files_folders import ManageFilesFolders

sort_file = "D:\WorkSpace\lab\move_file\structure\sort_file.json"

## Read sorf template
with open(sort_file, "r") as file:
    template = json.load(file)

for target in template:
    mange = ManageFilesFolders(src=target["src"], dst=target["dst"])
    ## Get filename and set template
    for type_file in target["target_type"]: 
        ## ".exe"
        type_name = ".{}".format(type_file) 
        target["files"] += mange.read_file_type(type_name)
    mange.loop_move_file(target["files"])

# json_data = json.dumps(template, indent=4)
# print(json_data)
