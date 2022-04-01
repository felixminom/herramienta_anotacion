import os
import sys
from dotenv import load_dotenv

load_dotenv()

try:
    db_conn = os.getenv('DB_CONN')
except KeyError:
    print('Env var for db connection is missing, check your config')
    sys.exit()

class Config:
    """Una llave aleatoria, en producción deberia cambiarse"""
    SECRET_KEY = os.getenv('SECRET_KEY', 'This_key_should_be_changed')
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = db_conn


class DevelopmentConfig(Config):
    """Configuracion para el ambiente local de desarrollo"""
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DockerConfig(Config):
    """Configuracion para el ambiente dockerizado"""
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

#Se podría incrementar un cuarto ambiente de pruebas en un futuro

class ProductionConfig(Config):
    """Configuracion para el ambiente de produccion"""
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True


config_by_name = dict(
    dev=DevelopmentConfig,
    prod=ProductionConfig,
    docker=DockerConfig
)

key = Config.SECRET_KEY
