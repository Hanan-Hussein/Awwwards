#  Awwwards
### By Hanan Hussein
### [Live Site](https://awardsmarble.herokuapp.com) 

<img width="1440" alt="Screenshot 2022-06-15 at 23 01 08" src="https://user-images.githubusercontent.com/36597096/173929039-ea8dfe47-5f6b-482c-bf75-a31749457e12.png">




## Description 
This is a site where users can submit their projects, rate projects by usability,content and design, view and edit their profiles.
The site also provides api to view all projects and the users in the system
## Behavioural Driven Development
1. A user can sign up
2. A user can login
3. A user can post their projects for rating
4. A user can rate projects
5. A user can view projects
6. A user can view voters and their rates
7. An api to fetch all users in the system
8. A user can view and edit profile
9. An api to view all projects in the site

## Installation

    # clone the repository
    $ git clone https://github.com/Hanan-Hussein/Awwwards
    $ cd Awwwards
    # Open with your favourite code editor
    $ for vscode 
    $ code .
    
    
### Create a virtualenv and activate it

    $ python3 -m venv env
    $ . env/bin/activate

### Or on Windows cmd

    $ py -3 -m venv env
    $ env\Scripts\activate.bat

### Install dependancies in the app

    $ python3 -m install -r requirements.txt 
    
 ### Run 
 
     $ python3 manage.py runserver
     
 ### Built With
* Python 3.10.4
* Django
* psql
* JS

## License
Copyright (c) 2022 Hanan-Hussein
[MIT LICENSE](https://github.com/Hanan-Hussein/Awwwards/blob/master/LICENSE)
