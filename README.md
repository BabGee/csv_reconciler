## Screenshots

![image](https://github.com/BabGee/csv_reconciler/assets/39271713/00307dbb-4390-43cf-bf6c-591aca2c73e9)

# csv_reconciler

**csv_reconciler** is tool that reads in two CSV files (termed "source" and
"target"), reconcile the records, and produce a report detailing the differences between the two.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 


### Prerequisites
You will find hereafter what I use to develop and to run the project
* Python 3
* Django 5.0.6
* Virtualenv installed (optional but recommended)


### Installation

Get a local copy of the project directory by cloning "csv_reconciler" from github.

```bash
git clone https://github.com/BabGee/csv_reconciler.git
```

cd into the folder

```bash
cd csv_reconciler
```

I use Virtualenv for developing this project so I recommend you to create a virtual environment and activate it.

```bash
python3 -m venv env
source env/bin/activate
```

Install the requirements

```bash
python3 -m pip install -r requirements.txt
```

Then follow these steps:

```bash
python manage.py migrate
```

run the django server

```bash
python manage.py runserver
```


5. Select your source and target CSV files for reconciliation; a CSV reconciliation_report will be downloaded on your local machine with report detailing the differences between the source and target CSV files.

## Built With

* [Python 3](https://www.python.org/downloads/) - Programming language
* [Django](https://www.djangoproject.com/) - Web framework 
