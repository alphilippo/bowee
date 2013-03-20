Title: Bowee
Date: 2012-11-15
Author: Josue Kouka
Summary: Little cool tool

##What's __BoWee__

***BoWee*** is little python tool which helps people creating an architecture for **bottle** project.

It tries to use the [MVC](http://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller) architecture, actually is more ***Model View Template*** like in [Django Framework](http://en.wikipedia.org/wiki/Django_(web_framework)).
***BoWee*** uses **peewee** as ORM. 

##Requirements
To be able to use ***BoWee***, it's required to have at least installed:

* Peewee 

* SQLite  


##Installation

	:::console

	yosuke@loking:~$sudo pip install bowee

##Turorial

	:::console

	yosuke@loking:~$bowee_admin project test
	yosuke@loking:~$tree test
	test/
	├── __init__.py
	├── models.py
	├── static_files
	├── templates
	└── views.py

	2 directories, 3 files




