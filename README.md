# Cybersecurity Based Knowledge Management System

## About / Synopsis

C-KMS aims to store and retrieve corporate information security knowledge, improve collaboration, locate knowledge sources, mine repositories for hidden knowledge, capture and use knowledge in the workplace. 

The target users of C-KMS would be company employees who use information systems in their day-to-day work. Two fundamental technologies will significantly contribute to the development, implementation, and maintenance of C-KMS: portals and databases. To that end, general users (company employees) should be comfortable to obtain security-relevant knowledge they need at work (i.e., ease of use and usability of C-KMS), while they can engage in the knowledge-creating process via the portal, posting questions, insights, and even solutions related to corporate information security."

Our team will deploy a solution using web technologies in order to be accessible from any device. Our team will strive to develop a system with ease of use along with the necessary structure required to stored data that can answer questions user provide the system along with the ability for data expand ability through content uploaded by users and curated by approved users in the community.

* Columbus State University
* Senior Capstone 
* Project status: prototype

## Table of contents

> * [Title / Repository Name](#Cybersecurity-Based-Knowledge-Management-System)
>   * [About / Synopsis](#about--synopsis)
>   * [Table of contents](#table-of-contents)
>   * [Required Knowledge](#required-knowledge)
>   * [Installation](#installation)
>       * [Recommendations](#Recommendations)
>       * [Python](#Python)
>           * [Install with zip](#Install-with-zip)
>           * [Install command line](#Install-command-line)
>       * [Django](#Django)
>           * [pip install (optional)](#pip-install-(optional))
>           * [Django install command line](#Django-install-command-line)
>       * [Pycurl](#Install-Pycurl-library)
>       * [PostgreSQL](#PostgreSQL)
>           * [Install](#Install)
>           * [Create local database](#Create-local-database)
>           * [Load local database](#Load-local-database)
>   * [Code](#code)
>     * [Build](#build)
>         * [Start the postgres server](#Start-the-postgres-server)
>         * [Update database (optional)](#Update-database-(optional))
>         * [Start the web application](#Start-the-web-application)
>         * [Application running](#Now-the-application-is-running)   
>   * [Usage](#usage)
>     * [Features](#features)
>   * [Resources (Documentation and other links)](#resources-documentation-and-other-links)
>   * [Contributing / Reporting issues](#contributing--reporting-issues)
>   * [License](#license)
>   * [Development Team](#Development-Team)
>   * [Acknowledgements](#Acknowledgements)

## Required Knowledge
- Familiarity with chosen operating system and its command line interface. Preferably a unix based environment such as macOS or linux.
- Experience with Python.
- Familiarity with HTML, CSS and JavaScript.
- Experience with web development.
- Prior experience with Django is preferable.

## Installation

### Recommendations
We suggest using a UNIX based environment to run/build the application. This would include macOS, linux, and WSL.

**Note:** 
A windows based system is possible, but extra packages/library's might be needed and we do not guarantee its validity. 

### Python
The [python](https://www.python.org/) programming languages is needed because the app is built with the django library that uses python. Install version 3.6 of python. We recommend against the use of v2 because of its connectivity with the Django library. You can install it though the zip installer or though the command line. 

#### Install with zip:
[python v3](https://www.python.org/downloads/)

#### Install command line:
```bash
$ sudo apt-get update
$ sudo apt-get install python3.6
```
verify the install
```bash
$ python3 --version
```

### Django
Is the library that builds our application. [Django](https://docs.djangoproject.com/en/3.0/topics/install/) recommends that you use `pip` to install the django library. If your system does not have pip installed, you will need to do so. 

#### pip install (optional):
```bash
$ sudo apt-get update
$ sudo apt install python3-pip
```

verify the install
```bash
$ pip3 --version
```

#### Django install command line:
```bash
$ python3 -m pip3 install Django
```

verify the install by opening the python shell
```bash
$ python3
```

within the python shell
```python
import django
django.get_version()
quit()
```

### Install Pycurl library:
We use the [Pycurl library](https://pypi.org/project/pycurl/) to handle some URL requests, so this will need to be installed as well.

First, we need to make sure some dependceies of pycurl are installed
```bash
$ sudo apt install libcurl4-openssl-dev libssl-dev
```

Now we can install pycurl
```bash
$ pip3 install pycurl
``` 

### PostgreSQL
Django by default uses the [SQLite](https://www.sqlite.org/index.html) DBMS, but we decide to swap over to the [PostgreSQL](https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04) DBMS. Because PostgreSQL needs sever to host its data on, we need to create and run this server locally.

#### Install:
```bash
$ sudo apt-get install python3-dev libpq-dev postgresql postgresql-contrib
```

#### Create local database:
```bash
$ sudo su - postgres
$ psql

CREATE DATABASE postgres;
CREATE USER runner WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE postgres TO runner;
\q
```

#### Load local database:
```bash
$ python3 manage.py shell
```
```python
from django.contrib.contenttypes.models import ContentType
ContentType.objects.all().delete()
quit()
```
```bash
$ python3 manage.py loaddata datadump.json
```

## Code

### Build
In order to build and run the application, a few steps need to happen. first, the Postgres server needs to start, then update any data in the database if needed, finally start the server.

#### Start the postgres server:
```bash
$ sudo service postgresql start
```

#### Update database (optional):
```bash
$ python3 manage.py makemigrations
$ python3 manage.py migrate
$ python3 manage.py loaddata datadump.json
```

#### Start the web application:
```bash
$ python3 manage.py runserver
```

#### Now the application is running!!!
To view the main portal, to your [local host(8000)](http://127.0.0.1:8000)<br>
To view the admin portal for database purposes, go to [/admin](http://127.0.0.1:8000/admin/)<br>
To stop the server from running, hit `CTRL C` at the terminal. 

## Usage

### Features

| # | Feature | Details | Status |
|---|---------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------:|:------:|
| 1 | Login portal | The system is protected via a login portal | :heavy_check_mark: |
| 2 | Question query | enter my questions regarding Cyber Security topics on threats, assets, and advice on what to do | :heavy_check_mark: |
| 3 | Submit new questions | If a question returns no answer, user should be able to submit a new question | :heavy_check_mark: |
| 4 | Experts and colleagues can answer questions | The knowledge base should be provided by experts and questions should be answered by colleagues. | :heavy_check_mark: |
| 5 | List of relevant threats to the asset | Quickly select an asset from a dropdown list and see a list of relevant threats to that asset. Also have the ability to add a new threat | :heavy_check_mark: |
| 6 | Up-vote down-vote system | Answers should be voted on by users | :heavy_check_mark: |
| 7 | Admins approve additions | Only admin users should be able to approve new security related answers | :x: |

## Resources (Documentation and other links)
A collection of visual aids and research papers the team used to better abstract the development this system. The research papers was provided by the clients, while the diagrams where created by the development team to help abstract some of the areas of application. 

##### Research papers:

* [Ontology Security Management](resources/Tsuoumas_&_Gritzalis_2006.pdf)
* [Ontology Information Security](resources/Ontology_Paper_2007.pdf)

##### Diagrams
* [Wire-Frame](resources/site_map.pdf)
* [Technology Stack](resources/techonolgy_stack.pdf)
* [DataBase Design](resources/Database.pdf)

##### Installation Guides
- [Django](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django)
- [PostgreSQL](https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04)

## Contributing / Reporting issues
For [Contributing](https://github.com/JamesEllerbee/Cybersecurity-based-Knowledge-Management-System/pulls), please create a pull request with the title ether being **'New Feature'** or the title that was used when reporting the issue. The pull request should be with a testing branch and not with **'main'**. Any pull request that merges with main will odds are be denied.

For [reporting issues](https://github.com/JamesEllerbee/Cybersecurity-based-Knowledge-Management-System/issues), we are using the built in reporting system that github provides. Any bugs or suggestions to the application should be placed there.

## License

* [Python 3](https://docs.python.org/3/license.html)<br>
* [Django](https://www.djangoproject.com/trademarks/)<br>
* [PostgreSQL](https://www.postgresql.org/about/licence/)<br>

## Development Team

#### Peter Keres
* [GitHub Account](https://github.com/peterkeres)
* <keres_peter@columbusstate.edu>

#### James Ellerbee
* [GitHub Account](https://github.com/JamesEllerbee)
* <ellerbee_james1@columbusstate.edu>

#### Taylor Woods
* [GitHub Account](https://github.com/Woods-Taylor)
* <woods_taylor@columbusstate.edu>

#### Jeffery Hardin
* [GitHub Account](https://github.com/HardinScott)
* <hardin_jeffrey1@columbusstate.edu>

#### Alexander Hewit
* [GitHub Account](https://github.com/Toxic5863)
* <hewitt_alexander@columbusstate.edu>

## Acknowledgements
We would like to thank both of our sponsors Yaojie Li, Yoon Lee, and Yi Zhou. For their guidance and wisdom during the development of this application.
