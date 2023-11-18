#  Project 3 - Web Applications

# Chapter 18: Getting started with Django, p.379


# Setting up a project, p.380
Writing a spec, p.380
Creating a virtual environment, p.380
Activating the virtual environment, p.381
Installing Django, p.381

    Note: Windows activate command: ll_env\scripts\activate

Creating a project in Django, p.382
Creating the database, p.382
Viewing the project, p.383


# Try it yourself, p.384

## 18-1. New Projects
To get a better idea of what Django does, build a couple of empty projects and look at what Django creates. Make a new folder with a simple name, like snap_gram or insta_chat (outside of your learning_log directory), navigate to that folder in a terminal, and create a virtual environment. Install Django and run the command django-admin.py startproject snap_gram . (make sure you include the dot at the end of the command). Look at the files and folders this command creates, and compare them to Learning Log. Do this a few times until you’re familiar with what Django creates when starting a new project. Then delete the project directories if you wish.


# Starting an app, p.384
Defining models, p.385
    models.py
Activating models, p.386
    settings.py
The django admin site, p.387
    Setting up a superuser
    Registering a model with the admin site
        admin.py
    Adding topics
Defining the entry model, p.390
    models.py
Migrating the entry model, p.391
Registering Entry with the admin site, p.391
    admin.py
The Django shell, p.392


# Try it yourself, p.394

## 18-2. Short Entries: 
The __str__() method in the Entry model currently appends an ellipsis to every instance of Entry when Django shows it in the admin site or the shell. Add an if statement to the __str__() method that adds an ellipsis only if the entry is longer than 50 characters. Use the admin site to add an entry that’s fewer than 50 characters in length, and check that it doesn’t have an ellipsis when viewed.
    models.py

## 18-3. The Django API: 
When you write code to access the data in your project, you’re writing a query. Skim through the documentation for querying your data at 
https://docs.djangoproject.com/en/4.2/topics/db/queries/ 
Much of what you see will look new to you, but it will be very useful as you start to work on your own projects.

## 18-4. Pizzeria: 
Start a new project called pizzeria with an app called pizzas. Define a model Pizza with a field called name, which will hold name values, such as Hawaiian and Meat Lovers. Define a model called Topping with fields called pizza and name. The pizza field should be a foreign key to Pizza, and name should be able to hold values such as pineapple, Canadian bacon, and sausage. Register both models with the admin site, and use the site to enter some pizza names and toppings. Use the shell to explore the data you entered.
    pizadmin:ww


# Making pages: the learning log home page, p.394
Mapping an url, p.395
    learning_log/learning_log/urls.py
    learning_logs.urls.py
Writing a view, p.396
    views.py
Writing a template, p.397
    index.html


# Try it yourself, p.398

## 18-5. Meal Planner: 
Consider an app that helps people plan their meals throughout the week. Make a new folder called meal_planner, and start a new Django project inside this folder. Then make a new app called meal_plans. Make a simple home page for this project.

## 18-6. Pizzeria Home Page: 
Add a home page to the Pizzeria project you started in Exercise 18-4 (page 394).


# Building additional pages, p.398
Template inheritance, p.398
    base.html
The child template, p.399
    index.html
The topics page, p.400
    The topics URL pattern, urls.py
    The topics view, views.py
    The topics template, topics.html
Individual topics pages, p.403
    The topic url pattern, urls.py
    The topic view, views.py
    The topic template, topic.html


# Try it yourself, p.406

## 18-7. Template Documentation: 
Skim the Django template documentation at
https://docs.djangoproject.com/en/4.2/topics/templates/
You can refer back to it when you’re working on your own projects.

## 18-8. Pizzeria Pages:
Add a page to the Pizzeria project from Exercise 18-6 (page 398) that shows the names of available pizzas. Then link each pizza name to a page displaying the pizza’s toppings. Make sure you use template inheritance to build your pages efficiently.


# Chapter 19: User accounts, p.409

# Allowing users to enter data, p.410
Adding new topics, p.410
    The topic ModelForm
        forms.py, p.411
    The new topic URL
        urls.py
    The new topic() view function
        views.py
    GET and POST requests
    The new_topic template
        new_topic.html
    Linking to the new topic page
        topics.html
Adding new entries, p.414
    The entry ModelForm
    The new entry url
    The new_entry view function
    The new entry template
    Linking to the new entry page
Editing entries, p.418
    The edit_entry url
    The edit_entry() view function
    The edit_entry template
    Linking to the edit_entry page


# Try it yourself, p.421

## 19-1. Blog: 
    web_apps/blog

Start a new Django project called Blog. 
Create an app called blogs in the project 
and a model called BlogPost. 
The model should have fields like title, text, and date_added. 

Create a superuser for the project, and use the admin site to make a couple of short posts. 
    Note: superuser: blog_admin

Make a home page that shows all posts in chronological order. 

Create a form for making new posts 
and another for editing existing posts. p.418 
Fill in your forms to make sure they work.


# Setting up user accounts, p.421
The users app
    Adding users to settings.py
        learning_log/learning_log/settings.py
    Inclusing the urls from users
        learning_log/urls.py
The login page
        learning_logs/urls.py
    The login template
        # ToDo: login.html
    
