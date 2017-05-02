import os
from distutils.core import setup

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
    long_description = long_description.replace("\r","")
except:
    print('Long desc failure')
    long_description = open('README.md').read()

setup(
    name = 'link_preview', # name of package
    packages = ['link_preview'],
    version = '1.0',
    description = 'Python package to get elements that make link preview',
    long_description=long_description,
    license='MIT',
    author = 'Akash Ahmed',
    author_email = 'aksben65@gmail.com',
    url = 'https://github.com/aakash4525/py_link_preview', # url of git repo
    download_url = 'https://github.com/aakash4525/py_link_preview/archive/v1.0.tar.gz', # git tagged tar.gz
    keywords = ['preview', 'link'],
    platforms='all',
    classifiers = []
)