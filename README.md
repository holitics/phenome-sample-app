# Phenome Sample App

The Sample App is based on the [Phenome AI](https://phenome.ai/) platform. It also depends on the [Phenome Extensions](https://github.com/holitics/phenome-extensions).

For documentation of the Phenome Platform and API, please see the [Phenome AI Online Doc](https://holitics.github.io/holitics_core_agent/html/) 

SampleApp is a **Flask Application**. It has a REST API and a simple embedded UI interface. If you are familiar with Python, Flask and JSON, it's fairly easy to create your own application.

## Getting Started

Please note, these instructions assume you have a minimum of [Python 3.6](https://www.python.org/downloads/) and [git](https://git-scm.com/downloads) installed. **Do not use Python 3.8+** as some of the dependencies like TensorFlow, Keras, SQLAlchemy may not work correctly due to deprecation (WIP).

First clone the source:
```
$ git clone https://github.com/holitics/phenome-sample-app
```

then change into the directory:

```
$ cd phenome-sample-app
```

create a base INI file:
```
$ cp sample_app/sample_app.ini.dist ./sample_app.ini.ini
```

If you would like, you should edit this file and put in your Mail Server information, etc. It is pretty self-explanatory. Detailed documentation on the INI file forthcoming.

## Install the dependencies

The Phenome core will be needed:
```
$ pip install phenome-core --extra-index-url https://api.packagr.app/AvVcpYfO2/
```
then clone the extensions directly into the source directory:
```
$ git clone https://github.com/holitics/phenome-extensions phenome
```

At this point the Sample App should be runnable. Let's try it out!

## Run the app locally

```
$ ./run.sh
```

If you haven't followed the previous instructions it will try to install the dependencies. Once it is ready and has started, you should see some information print to the screen:

```
Starting Sample App...
Opening Database, please wait ...
Loading Object Model, please wait ...
Object Model loaded in 4117ms
Using TensorFlow backend.
 * Serving Flask app "phenome" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
WARNING: Logging before flag parsing goes to stderr.

Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)

```

Everything else will probably go to the log. There should be a "/log" directory created automatically.

## Check the UI in browser
[App Local UI](http://localhost:8080/)

## Access the API
```
$ curl http://localhost:8080/api/v1/helloworld
```

## Development Environment

At this point you should be ready to start running / debugging the application in the IDE. If you have PyCharm, simply go to "File" -> "Open" and point to the **phenome-sample-app** folder (or whatever folder you cloned into). Once opened, create a Run/Debug configuration by going to "Run" -> "Edit Configurations".

![Debug Configuration For PyCharm](http://staging2.phenome.ai/wp-content/uploads/2019/11/PyCharm_DEBUG_Config_Sample_App.png)

Make sure to use **Python 3.6 or 3.7**. Also for a DEBUG configuration, make sure to add the parameters: **"--debug True"**
