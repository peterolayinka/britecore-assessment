# Project Title

This an insurance solution (BriteCore Engineering Application) that allows insurers to define their own custom data model for their risks. This solution aids insurers to create their own risk types and attach as many different fields as they would like.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
Django==2.1.3
django-extensions==2.1.3
djangorestframework==3.9.0
Markdown==3.0.1
```

`pip install requirements/base.txt`

### Installing

A step by step series of examples that tell you how to get a development env running


```
Set Up a Virtual Environment
```

```
install requirements
```

```
makemigrations and migrate the changes to your database
```

```
creat a superuser
```

```
makemigrations and migrate the changes to your database
```

```
creat a superuser
```

```
create as much risk types as you want
```

```
create as much risk field types as you want also
```

```
then input risk and risk fields from the main interface <http://localhost:8000> as a normal user
```

```
hmmm! are you expecting something more? Sorry! that is all.
```

```
#wink ;)
```

## Running the tests

run tests by using the command 

`python manage.py test management.tests.test_views`

`python manage.py test management.tests.test_views`


### Enpoints
1. <http:/localhost:8000/api/risk/type> [`GET`, `POST`]
2. <http:/localhost:8000/api/risks/> [`GET`]
3. <http:/localhost:8000/risks/<pk>/> [`GET`]


## Deployment

include all neccessary credentials like (database, hosting of static files *optional, etc)

`pip install zappa`

`zappa init`

`zappa deploy dev`

## Demo
<https://w9ajph1iqe.execute-api.us-west-2.amazonaws.com/dev/>

## Built With

* [Django](https://docs.djangoproject.com/) - The web framework used
* [AWS (S3, RDS, Lambda)](https://s3.console.aws.amazon.com/) - Hosting Platform
* [Zappa](https://github.com/Miserlou/Zappa/) - Deploy server-less, event-driven Python applications
* [Django Rest Framework](https://www.django-rest-framework.org/) - Web API Framework
* [Vue.js](https://vuejs.org/) - Javascript framework

