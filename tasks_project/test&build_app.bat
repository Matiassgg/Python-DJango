@echo off
python -Wa manage.py test
echo ----------------------------------------------------------------------
docker build . -t tasks-app
exit
