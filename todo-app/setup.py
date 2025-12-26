from setuptools import setup, find_packages

setup(
    name="todo-console-app",
    version="1.0.0",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'todo-app=src.main:main',
        ],
    },
)