#### create django project using command 

```bash
django-admin startproject boltscourier
```

---

```bash
cd boltscourier
```

---

#### create app
create django app using command -> 

```bash
python manage.py startapp app
```

---

#### Registers app in boltscourier/settings.py
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app', # added this line
]
```

---

### edit file boltscourier/urls.py to add app urls in project(currently not defined)
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')), # in backtesting-django/backtesting-django/urls.py (the file in which project config is stored)
]
```

---

#### making url files to define urls or endpoints for app
-> make a file urls.py in folder app, and added the following code

```python
urlpatterns = [
    path('', landing_page, name='landing page'), # in app/urls.py # landing page here is function to display landing page which we will write later on.
    path('/contact-us/', contact_submit, name='Contact us page'),
]
```


#### Edit view.py adding function to get data for landing page

```python
def landing_page(request):
    return render(request, "landing/index.html") # this will show the template index.html at base url with no endpoints
```



#### added a new folder templates, and landing folder, and static/css/ folder in app/
then created files index.html, and contact_us.html with dummy code of frontend.





---

---



## Steps to follow for setting up
- boltscourier folder is given in zip file is our project in which manage.py exists.
- inner folder within the folder with same name 'boltscourier' is used for storing project level config files.
- app/ folder is storing app level config files, we are designing this as a single app for now.(we can also create multiple apps)

---

- open vscode in main boltscourier folder.
- go to terminal and run the following commands one by one.

```bash
python -m venv venv # create a virtual environment

# for activating virtual environment run
source ./venv/bin/activate # if running on bash, for cmd or powershell(on windows) it is a little bit different, use scripts instead of bin and so on.

# install neccessary dependencies by running
pip install -r requirements.txt

# run project by
python manage.py runserver
# make sure your terminal is open in main boltscourier folder in which manage.py file exist.

```


# How to Edit files frontend devs.
working folders for frontend developers are mainly templates/ and static/.

create a file for a seperate page in templates like index.html, contact_us.html, etc.

For now I have made two files index.html for landing page, and contact_us file, try to make changes in index.html file and run the project, you will see changes on main page.

Notice how files are connected differently from local html, css js projects, and **study about django template language (DTL)**

## optional tasks for now
create the file called .gitignore and add your virtual environment to avoid pushing it to github later.

# How to edit files for backend devs
...