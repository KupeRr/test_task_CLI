# test_task_CLI
It was necessary to make a simple service that interactively calls some subprogram. That is, a certain top-level menu, in which the user selects one of the available subprograms, and begins to work with it.  

Functional parts of the service:
- Calculator
- Git-client
- Interaction with external API / REST service

----

# Documentation
The main file to run the service is main.py. After starting it, you will be able to select the necessary module to work through the terminal.

Also, you can access a separate module through the terminal, for example: 
```
python calculator.py '(1+1)**(6/2)'
```
The first module is a calculator. It takes a string as an argument and calculates its result.


The second module is the Git client. Allows you to download the necessary project by link to the selected directory. It is possible to choose both a global path to the folder and a local one. If the project is already downloaded - the command git pull will be executed. Implemented the ability to switch between branches and select the name of the folder in which the project will be located. It takes a string as an argument for folder name.

Parameters:
- --path (-p)         - Path to the folder of the repository
- --local-path (-lp)  - Path to the repository folder from the current folder
- --git-link (-gl)    - HTTPS path to github repository
- --branch (-b)       - Necessary branch name of the repository

If you do not specify a link to GitHub, the default link to the example project will be used. The same will happen if you don't specify a branch, by default it will be main.
The third module is Pokémon. This module allows you to get information about any pokémon, as well as a brief description of all its abilities. Accordingly, the module takes the name of the pokémon as an argument.

Example:
```
python git_service.py folder -p C:\proj\test_repo -gl https://github.com/KupeRr/test.git   
```


The third module is Pokémon. This module allows you to get information about any pokémon, as well as a brief description of all its abilities. Accordingly, the module takes the name of the pokémon as an argument.

Example:
```
python pokemon.py pikachu 
```

All required libraries are in the requirements.txt file.
