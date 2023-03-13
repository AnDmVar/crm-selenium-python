@echo off
call python setup_db.py
call pytest -s -v --browser edge --headless no --environment local
python teardown_db.py