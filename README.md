# Fright Night Film Finder

This is my fourth milestone project with Code Institute. It is a website for people who enjoy horror movies to seek a recommendation for a movie, comment on, like and/or review other peoples movie posts, or indeed post their own recommendations.

[Click here to go to my live project](https://fnff-app-762333af5e41.herokuapp.com/)

![image of mobile devices of varying sizes displaying the website at different points on the page](FNFF/assets/Responsive.jpg)


## Project Goal

The primary goal for this project is to create a horror movie website that enables full CRUD functionality to admin users so that they can Create, Read, Update, Delete, as well as like posts directly on the site, and for registered users the ability to Create comments, Read comments and posts and like posts if they wish. The admin user has full control over their posts and any changes made are reflected on the site.

## Approach

An Agile methodology was used to plan this project. This was implemented using a Kanban board in GitHub Project with linked Issues. To cover the goals of this project, a total of 10 User Stories where created. Labels where then used to prioritize the importance of each User Story.

The following labels were used in this project and the distribution of user stories by label are:

Must-Have: 6/10
Should-Have: 2/10
Could-Have: 2/10

For more info: [View Kanban Board here.](https://github.com/users/Ger-23/projects/7)

## Features


## Design


## Testing

### Browser Testing

I have tested that this application works using the following browsers:

  - Safari Version
  - Google Chrome
  - Microsoft Edge

I have tested this application works on the following devices:

  - Samsung S22
  - iPad 10

### Responsiveness

Chrome developer tool have been used to check the responsiveness.

I have tested that this application works on different screen sizes from small (260px wide) to standard screen size (1920px wide).


### Validator Testing

**W3C Markup Validator**

The W3C Markup Validator was used to validate the HTML on all pages of the project to ensure there were no errors. 
All passed without errors.

![image of W3C Markup Validator results](FNFF/assets/htmlvalidate.jpg)

**W3C CSS Validator**

The W3C CSS Validator was used to validate the CSS in the project to ensure there were no errors. 
All passed without errors.

![image of W3C CSS Validator results](FNFF/assets/cssvalidate.jpg)


**The CI Python Linter**

The Code Institute Python Linter was used to ensure there were no errors in the Python code. 
All passed without errors.

![image of CI Python Linter results](FNFF/assets/pythonformstest.jpg)


**Lighthouse Validation**

The Lighthouse Extension in Google Chrome was used to check performance, accessibility best practices 
and search engine optimisation. 

![image of Lighthouse Validation results](FNFF/assets/lighthousevalidate.jpg)


## Deployment

The application was deployed to Heroku. The steps to deploy are as follows:

  - Login to [Heroku](https://dashboard.heroku.com/apps) dashboard to get an overview of installed apps.
  - Click on New and Create new app.
  - Choose a name for your application (must be unique) and enter your location.
  - Click on Create app.
  - After creating your new application, navigate and click on the Resources tab.
  - In the Add-ons search bar enter Heroku Postgres and Select Heroku Postgres.
  - A pop-up window till appear, choose Plan name Hobby Dev - Free.
  - Click on Submit order form.
  - Navigate to the Settings tab and click on Reveal Config Vars.
  - Copy the DATABASE_URL url value to the clipboard.
  - In GitPod create a new env.py file on top level directory.
  - In Heroku navigate to the Settings tab and click on Reveal Config Vars.
  - Add SECRET_KEY to Config Vars with the randomSecretKey value previously chosen.
  - In the settings.py file remove the insecure secret key and replace it with: SECRET_KEY = os.environ.get(’SECRET_KEY')
  - Update to use the DATABASE_URL: dj_database_url.parse(os.environ.get(”DATABASE_URL"))
  - Save all files and Make Migrations: python3 manage.py migrate
  - Login to [Cloudinary](https://cloudinary.com/) and navigate to the Cloudinary Dashboard.
  - Copy your CLOUDINARY_URL API Environment Variable to the clipboard.
  - In the env.py file add Cloudinary URL
  - In Heroku navigate to the Settings tab and click on Reveal Config Vars.
  - Add ’CLOUDINARY_URL’ to Config Vars with the in API Environment Variable value.
  - Add ’DISABLE_COLLECTSTATIC’ 1 to Heroku Config Vars (temporary, must be removed before final deployment).
  - In the settings.py file:
    - Add Cloudinary Libraries to installed apps (note: order is important) ’cloudinary_storage',  ’django.contrib.staticfiles', ’cloudinary',
    - Add the following code below STATIC_URL = ’/static/' to use Cloudinary to store media and static files:
      - STATICFILES_STORAGE = ’cloudinary_storage.storage.StaticHashedCloudinaryStorage'
      - STATICFILES_DIRS = [os.path.join(BASE_DIR, ’static')]
      - STATIC_ROOT = os.path.join(BASE_DIR, ’staticfiles')
      - MEDIA_URL = '/media/'
      - DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
    - Link file to the templates directory in Heroku: TEMPLATES_DIR = os.path.join(BASE_DIR, ’templates')
    - Change the templates directory to: TEMPLATES_DIR: 'DIRS': [TEMPLATES_DIR],
    - Add Heroku Hostname to ALLOWED_HOSTS: ALLOWED_HOSTS = [”Your_Project_name.herokuapp.com”, ”localhost”]
  - Create 3 new folders on top level directory: media, static, templates
  - Create a Procfile on the top level directory
  - In the Procfile file:
    - Add the following code with your project name: web: gunicorn PROJ_NAME.wsgi
  - In the terminal: Add, Commit and Push.
  - In Heroku navigate to the Deploy tab and click on Deploy Branch.
  - When build process is finished click on Open App to visit the live site.


## Future Implementation

  - Complete Readme.
  - Create more tests on views, models and forms.
  - Improve lighthouse performance scores
  - Create images functionality for Team member profiles.
  - Give registered users edit functionality for comments.


## Bugs

- Issue loading images to assets folder from local. Having to delete cookies
and site data each time for any results but still not loading all images 
(eg. Python Linter images for views and models, testing on views, models and forms, etc.)

- Issue with database connection which presented when trying to run tests - this line 
of code was added in env.py - os.environ['DEV'] = "1" - which was hashed out when finished running tests, 
and this in settings - DEBUG = 'DEV' in os.environ .


## Credit

- I Think Therefore I Blog Walkthrough for code and structure
- Mentor & Code Institute Tutors for guidance and coding assistance.
- Fishtails project for Readme guidance
- Stack Overflow for code assistance.