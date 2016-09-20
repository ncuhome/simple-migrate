from setuptools import setup
from os.path import join, dirname

with open(join(dirname(__file__), 'requires.txt'), 'r') as f:
    install_requires = f.read().split("\n")

setup(
    name="simple-migrate",
    version="0.0.1",
    description="A simple database migrate tool",
    author="ncuhome",
    url="https://github.com/ncuhome/simple-migrate",
    license="MIT",
    py_modules=['simple_migrate'],
    install_requires=install_requires,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
