from setuptools import setup, find_packages

setup(
    name='ytdl',
    version='0.0.0',
    packages=find_packages(),
    install_requires=[
        'click',
    ],
    entry_points={
        'console_scripts': ['ytdl = main:main'],
    },
)
