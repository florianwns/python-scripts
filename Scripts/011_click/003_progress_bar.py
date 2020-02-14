#!/usr/bin/env python3
"""
A progress bar
"""
import click
import time

arr = range(10)
with click.progressbar(arr, label="Sleep") as bar:
    for item in bar:
        time.sleep(.2)


# external iterator
with click.progressbar(length=len(arr), label="Sleep") as bar:
    for item in arr:
        bar.update(1)
        time.sleep(.2)

# custom bar
bar_template = ''.join([
    click.style('%(label)s', fg='green'),
    click.style('  [', fg='red'),
    click.style('%(bar)s', fg='yellow'),
    click.style(']  ', fg='red'),
    click.style('%(info)s', fg='green'),
])
with click.progressbar(arr, label="Sleep", bar_template=bar_template, fill_char='*') as bar:
    for item in bar:
        time.sleep(.2)
