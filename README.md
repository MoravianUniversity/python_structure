# python_structure
A repo that demonstrates preferred project structure in Python

## Developer Setup

1. Create a virtual environment

    `python3 -m venv .env`

2. Activate the virtual environment

    `source .env/bin/activate`
    
3. Install required libraries

    `pip install -r requirements.txt`
    
4. Install source as an editable package

    `pip install -e .`
    
## Files and Directories

* `requirements.txt` - The list of required libraries.  
* `setup.py` - The script the `pip` runs to install the package.  The current version is bare-bones.  Many
   other options should be set for a production system.
* `src/python_structure/__init__.py` - Establishes the `python_structure` directory as a package. This file is empty 
   by default.

 
 ## Background Reading
 
 * [An argument](https://hynek.me/articles/testing-packaging/) to use the `src` folder.  This article also
   talks about using `tox`, which is not used in this repo.
*  [In-depth discussion of packaging](https://blog.ionelmc.ro/2014/05/25/python-packaging/), also using a
   `src` directory.  Only the section, "The structure" is relevant to this repo.  The rest goes further into
   configuring testing and continuous integration via TravisCI.
