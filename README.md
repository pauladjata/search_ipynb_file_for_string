# search_ipynb_file_for_string
Searches directory for Jupyter Notebook files for particular string


purpose: to search a directory for any Jupyter Notebook files ('.ipynb')
If a Jupyter Notebook file is found:
1. it is converted to a text file and then;
2. searched for a string the user enters
returns a list of filepaths to the .ipynb file containing the search term

To use:

a. cd into directory which you would like to search
b. in command line: [ python search_notebook.py "string to search" ]
c. the search string must be surrounded by double quotes

