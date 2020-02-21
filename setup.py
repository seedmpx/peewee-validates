from setuptools import setup
from codecs import open
from os import path

# from peewee_validates import __version__  # the build requires preinstalled peewee and datautils
__version__ = '1.0.8'

root_dir = path.abspath(path.dirname(__file__))

with open(path.join(root_dir, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(root_dir, 'requirements.txt'), encoding='utf-8') as f:
    install_requires = list(map(str.strip, f.readlines()))

setup(
    name='peewee-validates',
    version=__version__,

    description='Simple and flexible model validator for Peewee ORM.',
    long_description=long_description,

    url='https://github.com/timster/peewee-validates',

    author='Tim Shaffer',
    author_email='timshaffer@me.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Database :: Front-Ends',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='peewee orm database form validation development',

    py_modules=['peewee_validates'],

    install_requires=install_requires,
)
