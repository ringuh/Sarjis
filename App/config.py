# -*- coding: utf-8 -*-
import os.path

class BaseConfig(object):
	DEBUG = True
	SECRET_KEY = "WQF2aEeyhJN5yQh"
	SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://admin:zergling@localhost/sarjisdb"
	SQLALCHEMY_POOL_SIZE = 15
	SQLALCHEMY_MAX_OVERFLOW = 100
	SQLALCHEMY_POOL_RECYCLE = 900
	WTF_CSRF_ENABLED = True
	APP_ROOT = os.path.dirname(os.path.abspath(__file__))
	SARJAKUVA_FOLDER = os.path.join( os.path.join( os.path.join(APP_ROOT, 'project'), 'static' ), 'sarjakuvat' )
	
	MAX_CONTENT_LENGTH = 2 * 1024 * 1024
	
	REQUEST_HEADER = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.124 Safari/537.36' }
	
	#ERRORS_LOG_PATH = os.path.join(UPLOAD_FOLDER, 'foo.log')

class DebugConfig(BaseConfig):
	DEBUG = True

