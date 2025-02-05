def list_files(parent_directory, current_filepath=""):
    file_list = []
    for key in parent_directory:
        new_filepath = current_filepath + "/" + key
        val = parent_directory[key]
        if val is None:
            file_list.append(new_filepath)
        else:
            file_list.extend(list_files(val, new_filepath))
    return file_list
