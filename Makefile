
setup-db::
	./manage.sh makemigrations
	./manage.sh migrate

setup-su::
	./manage.sh createsuperuser

setup:: setup-db setup-su

run::
	./manage.sh runserver
