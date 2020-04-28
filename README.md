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
>   * [Installation](#installation)
>       * [Recommendations](#Recommendations)
>       * [Python](#Python)
>           * [Python install with zip](#Python-install-with-zip)
>           * [Python install command line](#Python-install-command-line)
>       * [Django](#Django)
>           * [pip install (optional)](#pip-install-(optional))
>           * [Django install command line](#Django-install-command-line)
>   * [Usage](#usage)
>     * [Screenshots](#screenshots)
>     * [Features](#features)
>   * [Code](#code)
>     * [Content](#content)
>     * [Requirements](#requirements)
>     * [Limitations](#limitations)
>     * [Build](#build)
>     * [Deploy (how to install build product)](#deploy-how-to-install-build-product)
>   * [Resources (Documentation and other links)](#resources-documentation-and-other-links)
>   * [Contributing / Reporting issues](#contributing--reporting-issues)
>   * [License](#license)
>   * [Development Team](#Development-Team)
>   * [Acknowledgements](#Acknowledgements)

## Installation

### Recommendations
we suggest using a UNIX based environment to run/build the application. This would include macOS, linux, and WSL.

**Note:** 
A windows based system is possible, but extra packages/library's might be needed and we do not guarantee its validity. 

### Python
The python programming languages is needed because the app is built with the django library that uses python. Install version 3.6 of python. We recommend against the use of v2 because of its connectivity with the Django library. You can install it though the zip installer or though the command line. 

#### Python install with zip:
[python v3](https://www.python.org/downloads/)

#### Python install command line:
>
> `sudo apt-get update`
>
> `sudo apt-get install python3.6`

verify the install
> `python3 --version`

### Django
Is the library that builds our application. [Django](https://docs.djangoproject.com/en/3.0/topics/install/) recommends that you use `pip` to install the django library. If your system does not have pip installed, you will need to do so. 

#### pip install (optional):
> `sudo apt-get update`
>
> `sudo apt install python3-pip`

verify the install
> `pip3 --version`

#### Django install command line:
> `python3 -m pip3 install Django`

verify the install
> `python3`
>
> `import django`
>
> `django.get_version()`
>
> `quit()`

### PostgreSQL
Django by default uses the [SQLite](https://www.sqlite.org/index.html) DBMS, but we decide to swap over to the PostgreSQL DBMS. Because PostgreSQL needs sever to host its data on, we need to create and run this server locally.

#### PostgreSQL install:
> `sudo apt-get install python3-dev libpq-dev postgresql postgresql-contrib`

#### PostgresSQL local database:
> `sudo su -postgres`
>
> `psql`
>
> `CREATE DATABASE postgres;`
>
> `CREATE USER runner WITH PASSWORD 'password';`
>
> `GRANT ALL PRIVILEGES ON DATABASE postgres TO runner;`
>
> `\q`

#### PostgresSQL 



* From the Nuxeo Marketplace: install [the Sample Nuxeo Package](https://connect.nuxeo.com/nuxeo/site/marketplace/package/nuxeo-sample).
##### From the command line 
>`nuxeoctl mp-install nuxeo-sample`

## Usage

### Screenshots

### Features

## Code

[![Build Status](https://qa.nuxeo.org/jenkins/buildStatus/icon?job=/nuxeo/addons_nuxeo-sample-project-master)](https://qa.nuxeo.org/jenkins/job/nuxeo/job/addons_nuxeo-sample-project-master/)

### Content

Description, sub-modules organization...

### Requirements

See [CORG/Compiling Nuxeo from sources](http://doc.nuxeo.com/x/xION)

Sample: <https://github.com/nuxeo/nuxeo/blob/master/nuxeo-distribution/README.md>

### Limitations

Sample: <https://github.com/nuxeo-archives/nuxeo-features/tree/master/nuxeo-elasticsearch>

### Build

    mvn clean install

Build options:

* ...

### Deploy (how to install build product)

Direct to MP package if any. Otherwise provide steps to deploy on Nuxeo Platform:

 > Copy the built artifacts into `$NUXEO_HOME/templates/custom/bundles/` and activate the `custom` template.

## Resources (Documentation and other links)

## Contributing / Reporting issues

Link to JIRA component (or project if there is no component for that project). Samples:

* [Link to component](https://jira.nuxeo.com/issues/?jql=project%20%3D%20NXP%20AND%20component%20%3D%20Elasticsearch%20AND%20Status%20!%3D%20%22Resolved%22%20ORDER%20BY%20updated%20DESC%2C%20priority%20DESC%2C%20created%20ASC)
* [Link to project](https://jira.nuxeo.com/secure/CreateIssue!default.jspa?project=NXP)

## License

[Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0.html)

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