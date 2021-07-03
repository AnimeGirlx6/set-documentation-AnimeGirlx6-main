# Overview

In this assignment you will complete a very simple Python application and document it via Sphinx.  

This is an individual assignment.  Under no circumstance should you look at, share, or copy another student's code.  You may search the internet for help using Sphinx or consult with the practical exercises I did with you in class.  You should document any websites you use as described in the requirements below.

Read all of the requirements carefully.

# Requirements 

1. Complete the Calculator class by replacing `pass` with appropriate code to update the value and return the new value.
2. Test to make sure it works correctly. (It should print out 2 and -1 when you are finished)
3. Add docstrings to each function documenting what it does.
4. Create sphinx documentation in the docs folder.  
5. Create a file called about.rst.
    * Write some information about yourself in the about page.  
    * In your about page, make use of headers, bold, and italic text.
    * Add about.rst so it shows up in your Sphinx table of contents
6. Create another file called references.rst.
    * In references.rst, create a list of web sites that you use to help you complete this assignment.
    * Add references.rst so it shows up in your Sphinx table of contents
7. Install sphinx auto-api and configure `conf.py` to generate an API for app.py.  See tips below.
8. Generate the html documentation using Sphinx.  (Confirm that it generated properly and correct any mistakes.)
9. Add all the files you created to the git repository.  Commit them and push to the server.

# Tips

* To install sphinx, try `py -m pip install -U sphinx`
* To install sphinx-auto api, try `py -m pip install sphinx-autoapi`
* To configure sphinx-autoapi, add these lines to conf.py:

```
extensions.append('autoapi.extension')

autoapi_type = 'python'
autoapi_dirs = ['../src']
```