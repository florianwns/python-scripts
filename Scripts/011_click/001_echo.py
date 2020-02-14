#!/usr/bin/env python3
"""
Display text

Source : https://pypi.org/project/click/

Info : please install `pip install colorama`
"""
import click

# Hello world
click.echo('Hello World!')

# Unicode
click.echo(b'\xe2\x98\x83')

# With colors and styles
click.secho('Some more text', bg='blue', fg='yellow', underline=True, bold=True)
