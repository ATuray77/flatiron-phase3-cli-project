# Phase 3 CLI Project
## Project Repo: https://github.com/ATuray77/flatiron-phase3-cli-project/

# Installation
# Local download instructions
[1] click on the link then create a fork 
[2] Open your terminal then clone it locally then navigate to the folder
[3] Open the link a code editor of your choice.


# Program features
## cli.py
This files handles the functionality of the CLI portion of the code
[1] Important packages and files that aid in its functionality are imported and or defined here
    - simple_term_menu package handles the menu feature of the program
    - prettycli package handles coloring or higlighted display of imortant lines in the code
    - prompt_toolkit package handles prompting functionality of the cli
[2] The cars and owners table from the models folder are imported here to speed up the query process
    - The interaction between the database and the cli is enabled here. 
    - Querying the database, a key feature of the cli is made possible by this import.
[3] The 'get name' function is defined here. This handles the prompting to get user input of their name
## car.py
[1] Builds out the cars table
    - the __repr__ function defines the structure of the output display
[2] Imports important dependencies for the cars table
    - It imports sqlalchemy from which the foreign key and other table structures are included
    
## owner.py
[1] Builds out the owners table
    - the __repr__ function defines the structure of the output display
[2] Imports important dependencies for the owners table
    - It imports sqlalchemy, base and session packages to aid in the migration of data to the database
[3] This file further defines the one-to-many relationship between the owners table and the cars table
## seed.py
[1] This file contains data that populates the database
[2] This file also imports important packages to enable its functionality
[3] This file imports the sqlalchemy engine and session. The engine converts python language into sqlite vice versa. The session encapsulates the engine and makes communication with the subsequent database possible. 
[3] THis package further defines the one-to-many relationship between the tables
## session.py
It is here that the sqlalchemy engine and session packages are imported and defined for subsequent imports to other files that need them.The engine that converts the python OOP language into sqlite is defined and the session that promotes the communication with the database is also defined. 
## base.py
The declarative base is imported and defined here. This base is useful in the creation of objects/instances that are defined in the python class. This base is further imported by other files that need it. This helps to prevent duplication of code and the writing of clean code. 


### What Goes into a README?

This README should serve as a template for your own- go through the important
files in your project and describe what they do. Each file that you edit
(you can ignore your Alembic files) should get at least a paragraph. Each
function should get a small blurb.

You should descibe your actual CLI script first, and with a good level of
detail. The rest should be ordered by importance to the user. (Probably
functions next, then models.)

Screenshots and links to resources that you used throughout are also useful to
users and collaborators, but a little more syntactically complicated. Only add
these in if you're feeling comfortable with Markdown.

***

## Conclusion

A lot of work goes into a good CLI, but it all relies on concepts that you've
practiced quite a bit by now. Hopefully this template and guide will get you
off to a good start with your Phase 3 Project.

Happy coding!

***

## Resources

- [Setting up a respository - Atlassian](https://www.atlassian.com/git/tutorials/setting-up-a-repository)
- [Create a repo- GitHub Docs](https://docs.github.com/en/get-started/quickstart/create-a-repo)
- [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)
