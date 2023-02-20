# Library Django Project Installation Guide

This guide provides step-by-step instructions for installing and running this Library-Django-project that uses a phpMyAdmin database.

## Requirements

- Python
- Virtual environment (optional)

## Steps

1. Install Python
    - Make sure that Python is installed on your machine by running the following command in your terminal or command prompt: `python --version`.
    - If you do not have Python installed, you can download it from the official Python website.

2. Create a virtual environment (optional)
    - It is recommended to create a virtual environment for your Django project to isolate the dependencies and packages used by the project from other projects on your machine.
    - To create a virtual environment, run the following command in your terminal or command prompt: `python -m venv myenv`. Replace `myenv` with the name you want to give to your virtual environment.

3. Activate the virtual environment (if created)
    - Once the virtual environment has been created, activate it by running the following command in your terminal or command prompt:
      - For Unix-based systems: `source myenv/bin/activate`
      - For Windows: `myenv\Scripts\activate`

4. Install the required packages
    - The required packages for the project are listed in the `requirements.txt` file.
    - To install them, run the following command in your terminal or command prompt: `pip install -r requirements.txt`.

5. Create a database in phpMyAdmin
    - Log in to phpMyAdmin and create a new database for the Django project.

6. Configure the database settings
    - In the Django project, open the `settings.py` file and add the following code to configure the database:

                            DATABASES = {
                                'default': {
                                    'ENGINE': 'django.db.backends.mysql',
                                    'NAME': '<your_database_name>',
                                    'USER': 'root',
                                    'PASSWORD': '',
                                    'HOST': 'localhost',
                                    'PORT': '3306',
                                }
                            }



7. Run migrations
    - In the terminal or command prompt, run the following command to apply the database migrations to the newly created database: `python manage.py migrate`.

8. Run the server
    - To start the Django development server, run the following command in your terminal or command prompt: `python manage.py runserver`.

9. Access the project
    - You can access the Django project in your web browser by navigating to `http://localhost:8000/`.

## Conclusion

That's it! You should now be able to run the Library-project with a phpMyAdmin database.








Endpoint                 | Description                                  | Method(s) Supported
------------------------ | -------------------------------------------- | ------------
/login/                  | Login to the API                             | POST
/library-members/        | Create a new library member                  | POST
/library-staff-members/  | Create a new library staff member            | POST
/user_list/              | List all users                               | GET
/user/{id}/              | Retrieve or delete a specific user           | GET, DELETE
/books/                  | List all books                               | GET
/books/add/              | Create a new book                            | POST
/books/{id}/             | Retrieve or delete a specific book           | GET, DELETE
/issues/                 | List or create a new issue                   | GET, POST
/returns/                | List or create a new return                  | GET, POST
/renewals/               | List or create a new renewal                 | GET, POST
/issues/{id}/            | Retrieve or delete a specific issue          | GET, DELETE
/returns/{id}/           | Retrieve or delete a specific return         | GET, DELETE
/renewals/{id}/          | Retrieve or delete a specific renewal        | GET, DELETE

/books/search/?search=<any-related-value>  | Search for books based on related value |GET






=========================================================================================


                                _________________

                                HOSTED ON HEROKU
                                _________________

                    http://library-project-api.herokuapp.com

                                /login/                
                                /library-members/      
                                /library-staff-members/
                                /user_list/            
                                /user/{id}/            
                                /books/                
                                /books/add/            
                                /books/{id}/           
                                /issues/               
                                /returns/              
                                /renewals/             
                                /issues/{id}/          
                                /returns/{id}/         
                                /renewals/{id}/        
                                
=========================================================================================
