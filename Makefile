PROJECT=test42cc
MANAGE=$(PROJECT)/manage.py

test:
	$(MANAGE) test
syncdb:
	$(MANAGE)  syncdb --noinput

devserver:
	$(MANAGE)  runserver
