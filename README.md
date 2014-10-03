# Watchme

Python module that watches for changes to a source file and copies it each time.

## Why
We need to copy the HTML output file produced by our internet radio software onto our webserver.
The HTML output file contains song and artist data which we are required to show on our internet
radio site for compliance.

## Installation
```
$ git clone git@github.com:mscweb/watchme.git
$ cd watchme
$ virtualenv .
$ pip install requirements.txt -r
```

Create a ```config.json``` that specifies the source and destination file. See ```config.example.json```
for an example.

## Usage
```
$ python watchme.py
```

## Convert to Windows Executable
To build using py2exe, download the [binary installer](http://sourceforge.net/projects/py2exe/files/py2exe/0.6.9/).

From outside your virual environment run:
```
$ python setup.py py2exe
```
The build process has only been tested using the official 32-bit distribution of Python 2.7.

## Python 3
Not supported.

## Feeback
Questions, comments, and feedback are welcome at web@morrisville.edu

## Copyright
Copyright (c) 2014 Morrisville State College. See [LICENSE][] for details.

[license]: https://github.com/mscweb/watchme/blob/master/LICENSE
