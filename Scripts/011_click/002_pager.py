#!/usr/bin/env python3
"""
Simple pager

Each line have a different color
"""
import click


def generator():
    c = ['green', 'yellow', 'red']
    for idx in range(100):
        yield click.style('Line %d \n' % idx, fg=c[idx % len(c)])


click.echo_via_pager(generator())
