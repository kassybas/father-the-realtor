
setup-db::
	./manage.sh makemigrations
	./manage.sh migrate
	cp ../db.sqlite3 ./ || echo "Could not find ../db.sqlite3"

setup-su::
	./manage.sh createsuperuser

setup:: setup-db setup-su

run::
	./manage.sh runserver
