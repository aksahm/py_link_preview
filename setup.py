import os, markdown
from distutils.core import setup

long_description = markdown.html(os.path.join(os.path.abspath(__file__), 'README.md'))

setup(
    name = 'link_preview', # name of package
    packages = ['link_preview'],
    version = '0.7',
    description = 'Python package to get elements that make link preview',
    long_description=long_description,
    license='MIT',
    author = 'Akash Ahmed',
    author_email = 'aksben65@gmail.com',
    url = 'https://github.com/aakash4525/py_link_preview', # url of git repo
    download_url = 'https://github.com/aakash4525/py_link_preview/archive/v0.7.tar.gz', # git tagged tar.gz
    keywords = ['preview', 'link'],
    platforms='all',
    classifiers = []
)