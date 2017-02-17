from setuptools import setup

setup(
    name='gamedb',
    packages=['gamedb'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask_sqlalchemy',
        'psycopg2',
    ],
)
