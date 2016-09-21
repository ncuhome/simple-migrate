from setuptools import setup
from os.path import join, dirname

with open(join(dirname(__file__), 'requires.txt'), 'r') as f:
    install_requires = f.read().split("\n")

setup(
    name="simple-migrate",
    version="0.0.3",
    description="A simple database migrate tool for flask",
    author="ncuhome",
    author_email="dev@ncuhome.cn",
    url="https://github.com/ncuhome/simple-migrate",
    license="MIT",
    py_modules=['simple_migrate'],
    install_requires=install_requires,
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
