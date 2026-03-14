import os
import shutil

def list_dir(from_path):
    ls_dir_from_path = os.listdir(from_path)

    ls_dir_from_path_list = []
    for item in ls_dir_from_path:
        abs_item_path = os.path.join(from_path, item)
        if os.path.isdir(abs_item_path):
            ls_dir_from_path_list.append((item, 'dir', abs_item_path))
            
            # get files within this directory
            ls_dir_from_path_list += list_dir(abs_item_path)  
        else:
            ls_dir_from_path_list.append((item, 'file', abs_item_path))
    
    return ls_dir_from_path_list

def copy_files_recursive(working_directory, from_path, to_path):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        abs_from_path = os.path.normpath(os.path.join(abs_working_dir, from_path))
        abs_to_path = os.path.normpath(os.path.join(abs_working_dir, to_path))
        if not os.path.exists(abs_from_path):
            raise Exception(f'Error: Cannot copy as either "{from_path}" or "{to_path}" does not exist')


        ls_dir_from_path_list = list_dir(abs_from_path)
        
        # create to_path
        os.mkdir(abs_to_path)
        
        # recursively copy all files to from_path
        for item in ls_dir_from_path_list:
            item_name = item[0]
            item_type = item[1]
            item_path = item[2]
            
            if item_type == 'dir':
                os.mkdir(os.path.join(abs_to_path, item_name))
            
            if item_type == 'file':
                file_from = item_path
                # find the common path between the two before adding item_name
                file_to = item_path.replace(f"/{from_path}/", f"/{to_path}/")
                print(f"Copying from {file_from} to {file_to}...")
                shutil.copy(file_from, file_to)

    except Exception as e:
        return f"Error in executing copy: {e}"