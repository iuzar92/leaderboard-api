# **Highscore Challenge** #
_Author: Ibrahim Uzar_

Case Study for a REST API for accepting, processing, storing and returning information about user scores and rankings on a leaderboard.

>Please read each sub-section fully before running the relevant commands.

#### _Development Iteration: 1_
The project is currently under development. The full functionality of the API hasn't been integrated yet.

The next stages include:
- Create a Docker image
- Integrating a local, proxy and remote PostgreSQL database on Google Cloud
- Technical documentation !!

## **Installation** ##
Follow these steps to build and mount the app into a Docker container:

### 1. Python & Pip ###
>Python version 3.7.6 and Pip version 21.0.1

Click [here][Python] to install Python.

Click [here][Pip] for the get-pip.py file.

Paste the contents into a file named get-pip.py and run the following command to install pip:
```bash
python get-pip.py pip==21.0.1 wheel==0.36.0 setuptools==52.0.0
```
This will automatically install the suitable version of pip, wheel and setuptools.

Pip can also be installed through most package managers such as homebrew or apt-get.
>Example: \<brew install pip>

[Python]: https://www.python.org/downloads/release/python-376/
[Pip]: https://bootstrap.pypa.io/get-pip.py

### 2. Pipenv ###
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

## 3. Docker ##
Dockerfile inside the project folder contains instructions for setting up a Docker container on supported instances.

>The following code requires [Docker][Docker] to be installed locally

[Docker]: https://docs.docker.com/get-docker/

To build a Docker image from Dockerfile use:
+ Linux/Mac:
```bash
./scripts/uni/docker_build.sh
```
+ Windows:
```bash
./scripts/win/docker_build.ps1
```
<!--
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
-->
To start the container use:
+ Linux/Mac:
```bash
./scripts/uni/docker-run.sh
```
+ Windows:
```bash
./scripts/win/docker-run.ps1
```
This will start a Docker container on port 8888 using production settings.

> App entrypoint is '0.0.0.0:8888/leaderboard' on local installations

## **Usage** ##
To be updated !
