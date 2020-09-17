# Django 3.1 project

This is a simple Django project with the implimentation of login-registration. Below are the features for the application.

## Features

1.  An Admin login page
2.  Validate ID and Password
3.  If Valid, redirect to the profile page.
4.  If Invalid, redirect to a Signup page.
5.  Post Login/Signup, display all existing User ID on profile page using a dropdown list.
6.  Delete button to delete the selected User ID from the database.
7.  Logout.

## How to install (this is valid for linux and mac)

1. Clone the project.
2. Create and activate virtualenv for the project. (if want)
```bash
$ virtualenv venv -p python3 
$ souce venv/bin/activate
$ pip install -r requirements.txt
```
3. Navigate to algoscale directory and run the application.
```bash
$ cd algoscale 
$ python manage.py runserver 
```
4. Now the application will be running on port 8000(default).
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)
 

