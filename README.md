# Flask-API-Examples
This repository is an example of how to deploy a tensorflow model 
to a remote virtual server such that users can use it as an application.


## Technologies used
1. [Flask](http://flask.pocoo.org/) Micro-framework for serving the application itself.
2. [Gunicorn](http://gunicorn.org/) Standard WSGI-compatible web server.
3. [Tensorflow](https://www.tensorflow.org/) The famous deep learning framework.

## Instructions
1. Install Python 3 using [pyenv](https://github.com/pyenv/pyenv). You can make use of the [pyenv-installer](https://github.com/pyenv/pyenv-installer) to install **pyenv** effortlessly. **This application requires Python 3!**. It is assumed that every instructions are based on Python 3 instead of Python 2 without any mentioning.
2. Run the following command:

```
    pip install -r requirements.txt
```

3. For development mode, run `flask run`
4. For production usage, run `gunicorn --bind 0.0.0.0:8080 --daemon wsgi`