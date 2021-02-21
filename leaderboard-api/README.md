# **Highscore Challenge**

##### _Author: Ibrahim Uzar_

<hr style="border-bottom: 1px solid #ffcc00;">
<br/>

### Objective

Case Study for a REST API for accepting, processing, storing and returning information about user scores and rankings on a leaderboard.

<br/>
<hr>

##### **dev-iter.1 notes**

> ##### !! The project is currently under development. The full functionality of the API has not been integrated yet.

> ##### Please read each sub-section carefully before running the relevant commands.

> ##### The application currently runs on a local virtual environment (pipenv) running Python 3 and a PostgreSQL database.

<hr>
<br/>

## **Installation**

<hr style="border-bottom: 1px solid rgb(255, 204, 0);">

### **1. Python & Pip**

<hr style="width: 15%;margin-left:0;border-bottom: 2px dashed rgba(255, 204, 0, 0.2);">
<br/>

> Python version 3.7.6 and Pip version 21.0.1
>
> Click [here][python] to install Python.
>
> Click [here][pip] for the get-pip.py file.

Paste the contents into a file named get-pip.py and run the following command to install pip:

```bash
python get-pip.py pip==21.0.1 wheel==0.36.0 setuptools==52.0.0
```

This will automatically install the suitable version of pip, wheel and setuptools.

Pip can also be installed through most package managers such as homebrew or apt-get.

> Example: brew install pip

[python]: https://www.python.org/downloads/release/python-376/
[pip]: https://bootstrap.pypa.io/get-pip.py

<br/>

### 2. Pipenv

<hr style="width: 15%;margin-left:0;border-bottom: 2px dashed rgba(255, 204, 0, 0.2);">
<br/>

> Pipenv version 2020.11.15.

Update Pip and install Pipenv for setting up a virtual environment for the app.

```bash
pip install --upgrade pip
pip install pipenv
```

The Pipfile inside the project folder contains a list of Pipenv dependencies. To install dependencies automatically, navigate into the project folder and run:

```bash
pipenv update
```

> Edit Pipfile to see list of packages and their exact versions.

<hr>
<br/>

## **Run App Locally**

<hr style="border-bottom: 1px solid rgb(255, 204, 0);">

Navigate into the project root directory '/leaderboard-api' run the following scripts to migrate and initialize the application:

- ##### Linux/Mac

```bash
./scripts/uni/django_migrate_dev.sh
```

- ##### Windows

```bash
./scripts/win/django_migrate_dev.ps1
```

<hr>
<br/>

#### Next stages include:

<hr style="width: 15%;margin-left:0;border-bottom: 2px dashed rgba(255, 204, 0, 0.2);">

- Integrating a local, proxy and remote postgresql database on Google Cloud

- Implementing Django models (database, tables, test data)

- Documentation

<!--

## 3. Docker

Dockerfile inside the project folder contains instructions for setting up a Docker container on supported instances.

> ##### The following code requires [Docker][docker] to be installed locally

[docker]: https://docs.docker.com/get-docker/

To build a Docker image from Dockerfile use:

- ##### Linux/Mac:

```bash
./scripts/uni/docker_build.sh
```

- Windows:

```bash
./scripts/win/docker_build.ps1
```

To build and push a Docker image to remote container use:
>Edit script to add remote host address first
+ Linux/Mac:
```bash
./scripts/uni/docker_build_push.sh
```
+ Windows:
```bash
./scripts/win/docker_build_push.ps1
```

To start the container use:

- Linux/Mac:

```bash
./scripts/uni/docker-run.sh
```

- Windows:

```bash
./scripts/win/docker-run.ps1
```

This will start a Docker container on port 8888 using production settings.

> App entrypoint is '0.0.0.0:8888/leaderboard' on local installations

## **Usage**

To be updated !
-->
