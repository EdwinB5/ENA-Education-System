from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

MYSQL = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME' : 'ENA.system',
        'USER' : 'root',
        'PASSWORD' : '',
        'PORT' : 3306,
        'HOST' : '127.0.0.1',
   }
}

POSTGRESQL = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ENA.system',
        'USER':'postgres',
        'PASSWORD':'1234',
        'HOST':'127.0.0.1',
        'DATABASE_PORT':'5432',
    }
}