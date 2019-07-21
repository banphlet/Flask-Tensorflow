## Flask-React Tensorflow Project
This project illustrates using flask and react to start a machine learning Project based on Tensorflow. 

### Installation
Install flask https://flask.palletsprojects.com/en/1.1.x/installation/

Clone the repository
`git clone https://github.com/banphlet/Flask-Tensorflow`

Install virtual env 
```
python3 -m venv venv

```
Install dependencies
```
pip install -r requirements.txt

```

### Envs
```
FLASK_APP=./autoapp.py
DATABASE_URL=mongodb://localhost/flask

```


### Frontend
Ensure you have nodejs installed.

Install dependencies
`npm install`

Build production react build

`npm run build`



### Start application

`flask run`
