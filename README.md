# Web Sraper
An application to scrape data from https://coinmarketcap.com/all/views/all/, stored in the database and exposed via RESTful API. 

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [API Documentation](#api-documentation)



## General info
An application for keeping track of tourist and their site payments


## Technologies
* Python 3.9.6
* Django 3.2
* Django Rest Framework 3.14.0
* Beatiful Soup
* Selenium


## Installation on Windows
* [Follow the guide here](https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/) on how to install web driver for Selenium
### Setup

```
git clone https://github.com/Festus-Kwafo/Crypto_web_scraper.git
```
  
```
python3 -m venv venv

source venv/scripts/activate

pip install -r requirements.txt
py manage.py makemigrations
py manage.py migrate
```
  
## Running

Run this command to spin up the django development server.

```
py manage.py runserver
```

## Background Task

Run this command to run tasks that have been scheduled 
```
python manage.py process_tasks
```
## Generate Excel File
Run this command to generate Excel file
````
py manage.py run_scraper
````

## API Documentation
```
http://127.0.0.1:8000/api/v1/docs
```

