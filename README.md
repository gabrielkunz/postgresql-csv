# PostgreSQL & CSV Conversion
 Script to export and import PostgreSQL tables into/from CSV files

## database.cfg file format:

Database password is request during script execution, there's no need to save it in the .cfg file. Place the file in the same directory where the main script is located.

>[postgresql]\
>database=yourDatabaseName\
>user=userName\
>password= \
>host=yourHostAddress\
>port=portNumber

## Setup

It is recommended to use the program in a virtual environment using th virtualenv package:

```console
foo@bar ~ % python3 -m pip install virtualenv
```

Create a new environment:

```console
foo@bar ~ % python3 -m venv env
```

Activate the environment:

```console
foo@bar ~ % source env/bin/activate
```

Install the required packages:

```console
foo@bar ~ % pip install -r requirements.txt
```

When you finish usin the script, leave the virtual environment:

```console
foo@bar ~ % deactivate
```
