"""This tool allows to generate all the lecture resources (mostly plots)
automatically. It also allows to clean the outputs.
See the README.md for usage.
"""

from __future__ import print_function
import argparse
from contextlib import contextmanager
import glob
import os
from subprocess import call


@contextmanager
def cd(dir):
    'executes a statement in given directory, then returns to the previous one'
    cwd = os.getcwd()
    os.chdir(dir)
    yield
    os.chdir(cwd)


def make_plots():
    lectures = [file for file in glob.glob('*/plots-code') if os.path.isdir(file)]

    for lecture in lectures:
        print('lecture:', lecture)
        with cd(lecture):
            for script in glob.glob('*.py'):
                print('%s/%s' % (lecture, script))
                call(['python', script])


def clean(verbose=False):
    exts_to_delete = ['png', 'wav', 'mp3', 'json']
    files = [file for ext in exts_to_delete for file in glob.glob('*/*/*.%s' % ext)]
    for file in file:
        if verbose:
            print(file)
        os.remove(file)


def parse_args():
    parser = argparse.ArgumentParser(description='Generate plots and other resources for lectures')
    parser.add_argument('action', default='plots',
                        choices={'plots', 'clean'}, nargs='?')

    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_args()
    if args.action == 'plots':
        make_plots()
    elif args.action == 'clean':
        clean(verbose=True)
