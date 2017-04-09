# -*- coding: utf-8 -*-

' test '

__author__='yang'

import functools

f= functools.partial(int,base=2)
def printdebug(func):
    def __decorator():
        print('enter the login')
        func()
        print('exit the login')

    return __decorator


@printdebug  # combine the printdebug and login
def login():
    print('in login')


if __name__ == '__main__':
    login()

