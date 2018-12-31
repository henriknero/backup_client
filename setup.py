#! /usr/bin/python3
from setuptools import setup

setup(
    name='backup_client',
    version='0.4',
    author='Henrik Nero',
    author_email='henriknero@gmail.com',
    packages=['backup_client','backup_client.filehandler', 'backup_client.network'],
    scripts=['gibc'],
    data_files=[('.', ['default.conf']),
                ('data', ['data/icon.png'])]
)
