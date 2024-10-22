## Getting Started
Follow the steps below to clone the repository and set up the project locally.

1. Clone the repository to your local file: git clone https://github.com/darya17b/CptS322GradeTracker.git
2. cd CptS322GradeTracker
3. Check out the branch: git checkout feature/login_DB
4. Pull all the files: git pull origin feature/login_DB

## On VSCode Set Up a Virtual Environment
1. open the file on the vs code
2.  <img width="879" alt="Screenshot 2024-10-21 at 5 24 44 PM" src="https://github.com/user-attachments/assets/d77c1cd6-5f71-4766-8ed9-e9e4d533f34a">
3. in the terminal: pip install virtualenv
4. virtualenv env\
5. Activiate on Windows: env\Scripts\activate
6. Activate on Mac: source env/bin/activate

## Install Django
run: pip install django

if you get permission error: run with sudo pip install django

## Apply Migrations(setup the database)
1. cd gradetracker
2. run: python3 manage.py makemigrations gradetracker
2. run: python3 manage.py migrate in the terminal
3. <img width="859" alt="Screenshot 2024-10-21 at 4 20 25 PM" src="https://github.com/user-attachments/assets/c0de14fc-1f89-4d19-af1a-c0237c6928a5">
4. If the migration runs successfully, you should see an output similar to this in your terminal:
5. <img width="877" alt="Screenshot 2024-10-21 at 5 32 21 PM" src="https://github.com/user-attachments/assets/9a603f04-b233-4a47-bbfe-3aa88b0866ce">
6. Note : if python3 is not installed on your computer, use: python manage.py migrate instead!
7. run: python3 manage.py createsuperuser and Enter your username, email, and password
8. <img width="859" alt="Screenshot 2024-10-21 at 4 23 31 PM" src="https://github.com/user-attachments/assets/df2e386d-5943-4f48-8dfb-3a127badf5cf">.
9. Now run python3 manage.py runserver
10. If you implemented successfully, you should see the following in the terminal:
11. <img width="859" alt="Screenshot 2024-10-21 at 4 25 34 PM" src="https://github.com/user-attachments/assets/2829c561-cb25-4d33-89cd-f741aaf960e7">
12.  After successfully applying that, you now have admin privileges to add, change, and assign grades to students
13.  go to http://127.0.0.1:8000/admin/
14.  Enter the username and password that you created when you ran the createsuperuser command.
15.  now you can add,change, and assign grades
16.  <img width="1014" alt="Screenshot 2024-10-21 at 4 29 20 PM" src="https://github.com/user-attachments/assets/3c542fe9-1842-471a-b69d-bafb3e058933">
17. Then you can test it by login as a student with http://127.0.0.1:8000/accounts/login/ 
<img width="1014" alt="Screenshot 2024-10-21 at 4 31 28 PM" src="https://github.com/user-attachments/assets/e827662b-9e47-49a9-ade4-ad614b0c3444">
18. After login you should see a page
<img width="1014" alt="Screenshot 2024-10-21 at 4 31 59 PM" src="https://github.com/user-attachments/assets/efafbd5a-6ee5-4690-904a-25f2936fee44">

## Notes
If you change the application name in Django, you'll also need to update the INSTALLED_APPS section in the settings.py otherwise it will fail!

<img width="614" alt="Screenshot 2024-10-21 at 4 42 46 PM" src="https://github.com/user-attachments/assets/066d26d3-490a-4508-aff1-00af7f6db28a">

The HTML files are under /templates/gradetracker/, and urls.py routes to the views that render them. Right now, the logout function isn’t working, so that needs to be fixed.
models.py defines the structure of the database, so spend some time getting familiar with how the data is modeled there. 
In admin.py, the models are registered so we can manage the database through the Django admin interface.

