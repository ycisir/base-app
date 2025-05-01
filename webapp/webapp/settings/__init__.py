from decouple import config

if config('ENVIRONMENT') == "DEVELOPMENT":
	from .development import *
else:
	from .production import *