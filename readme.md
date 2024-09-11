# Django

## Initialisation

Create virtual environment :  
`virtualenv -p python3 <name>`

Activate it :  
`source <name>/bin/activate`

Deactivate it :  
`deactivate`

## Installation

Install Django :  
`pip install django`

## Start

Start the development server :

```bash
cd GestionTaches
python3 manage.py runserver
```

## Migrations

## Migrate

Migrate the current models :

```bash
cd GestionTaches
python3 manage.py migrate
```

## Create migration

Make a new migration with the new model :

```bash
cd GestionTaches
python3 manage.py makemigration
```
