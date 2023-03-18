# Create a Virtual Environment with Python

Creating a virtual environment is an essential step when developing **Projects**. It allows you to create an isolated environment where you can install specific versions of packages and dependencies without interfering with other Python projects on your system.

The present guide is a hybrid between a 'go-to' **cheat sheet** and a **tutorial** when starting a new **Project**.

Its purpose is to create a **virtual environment** with Python using the '**venv**' module.

---

Table of contents

- [Create a Virtual Environment with Python](#create-a-virtual-environment-with-python)
    - [Python](#python)
  - [Steps to creating a 'venv'](#steps-to-creating-a-venv)
    - [Create a folder for the project](#create-a-folder-for-the-project)
    - [Create a virtual environment for the project](#create-a-virtual-environment-for-the-project)
    - [Activate the new virtual environment ```venv```](#activate-the-new-virtual-environment-venv)
    - [Record the dependencies for the project](#record-the-dependencies-for-the-project)
    - [Install a Python Library](#install-a-python-library)
    - [Deactivate the virtual environment](#deactivate-the-virtual-environment)
   

---

### Python

    Version:  Python 3.11.1

---


## Steps to creating a 'venv'

### Create a folder for the project

There are 2 options:

1. Create a repository on [GitHub.com](https://github.com "GitHub.com") BEFORE creating the project folder on the local machine.

    Once the repository is created, clone it onto the local machine.

    OR

2. Create the project folder locally (see below gist)

   - First, open a **Terminal Prompt within VS Code**.

   - Then, go to the folder where the new project is to be created, *i.e.* go to the 'working folder'.

        For example, if the main folder is called ```python_projects```, go to

            C:\python_projects

        Hence, for the **relative path**, type:

            cd /python_projects

   - Create a folder for the project called ```project_name``` and check if it is present in the working folder

            mkdir project_name && dir

   - ```cd``` into this folder

            cd project_name

   - Open the project folder ```project_name``` from the menu in VS Code

---

### Create a virtual environment for the project

- Create a ```.py``` python file into ```project_name``` and ```cd``` into it

        echo >> python_script.py

    Alternatively, create the ```.py``` file from VS Code menu.

- Open ```python_script.py``` file

    **NOTE**: it is important to **create** AND **open** a ```.py``` file BEFORE creating and activating the venv, as it helps with its activation

- Create a virtual environment called ```venv_name```

    The command below will create a new folder called ```venv_name```

        python -m venv venv_name

    NOTE: the virtual environment name can be anything (like ```banana```).
    However, it is common practice to use just ```venv```. This is handy when copying/pasting code snippets.

    Hence, use the following command:

        python -m venv venv

    NOTE: a message will appear (bottom right) asking to use the new environment, click 'Yes'.

    Alternatively, choose from the list of environments (bottom left). The Python version should be listed with ```venv``` in parentheses, *e.g.*

        Python 3.10.1 64-bit ('venv')

        Python 3.9.1 64-bit ('venv')

        Python 3.9.2 64-bit ('venv')


---

### Activate the new virtual environment ```venv```

If using the default command prompt (```cmd```), type:

    .\venv\Scripts\activate

If using Windows PowerShell (```PS```), type:

    .\venv\Scripts\Activate.ps1

IMPORTANT: if no changes seem to occur, open a new terminal prompt to activate the environment.

The active path should now be preceded by ```(venv)``` or ```(banana)``` if a specific venv name was chosen.

---

### Record the dependencies for the project

- First, update the ```pip``` library

        python -m pip install --upgrade pip

- Then, create the dependencies file named ```requirements.txt```

        pip list > requirements.txt

---

### Install a Python Library

    pip install package_name

If installing more than one package, type:

    pip install package_name_1 package_name_2

If installing a specific version of a package, type:

    pip install package_name=1.6

---


### Deactivate the virtual environment

    deactivate

