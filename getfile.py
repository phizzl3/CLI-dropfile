from pathlib import Path


def get_file_path():
    """
    Gets file/directory via drag and drop and return a Path object.

    Asks for file or directory via drag and drop, strips unneeded characters,
    and uses pathlib.Path to return a Path object.

    Returns:
    - (pathlib.PosixPath object): A pathlib.PosixPath object that can be 
    used to get file path, filname, extension, etc. 

    Sample Usage:
    - p = get_file_path()
        - p = full path
        - p.parent = parent folder
        - p.stem = filename excluding extension
        - p.suffix = file extension
    """
    
    # get input file and strip characters
    f = input('\n Drop File: ')
    f = f.strip(" &'\"")
    f = f.replace("\ ", " ")
    # set Path object and return
    p = Path(f)
    return p
    