#!/usr/bin/python3

# infezione
# Copyright (C) 2024 Salvo "LtWorf" Tomaselli
#
# infezione is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# author Salvo "LtWorf" Tomaselli <tiposchi@tiscali.it>

from sys import argv, exit

def load_version():
    with open('CHANGELOG.md', 'rt') as f:
        return f.readline().strip()

AUTHOR = 'Salvo \'LtWorf\' Tomaselli'
AUTHOR_EMAIL = 'tiposchi@tiscali.it'
URL = 'https://github.com/ltworf/infezione'
BUGTRACKER = 'https://github.com/ltworf/infezione/issues'
DESCRIPTION = 'This is malware. Do not install this.'
KEYWORDS='security malware scorecard'
CLASSIFIERS = [
    'Development Status :: 2 - Pre-Alpha',
    'License :: OSI Approved :: GNU Affero General Public License v3',
    'Programming Language :: Python :: 3.11',
]

if len(argv) != 2:
    exit('Wrong command line')

if argv[1] == '--setup.py':
    with open('setup.py', 'wt') as f:
        print(
f'''#!/usr/bin/python3
# This file is auto generated. Do not modify
from setuptools import setup
setup(
    name='infezione',
    version={load_version()!r},
    description='{DESCRIPTION}',
    readme='README.md',
    url='{URL}',
    author={AUTHOR!r},
    author_email='{AUTHOR_EMAIL}',
    license='AGPL3',
    classifiers={CLASSIFIERS!r},
    keywords='{KEYWORDS}',
    packages=['infezione'],
)''', file=f
    )

elif argv[1] == '--pyproject.toml':
    with open('pyproject.toml', 'wt') as f:
        print(
f'''[project]
name = "infezione"
version = "{load_version()}"
authors = [
  {{ name="{AUTHOR}", email="{AUTHOR_EMAIL}" }},
]
description = "{DESCRIPTION}"
readme = "README.md"
requires-python = ">=3.8"
classifiers = {CLASSIFIERS!r}
keywords = {KEYWORDS.split(' ')!r}
license = {{file = "LICENSE"}}

[project.urls]
"Homepage" = "{URL}"
"Bug Tracker" = "{BUGTRACKER}"

[build-system]
requires = ["setuptools", "wheel"]
''', file=f
        )
