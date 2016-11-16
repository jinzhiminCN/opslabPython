#!/usr/bin/python
# coding:utf-8
import cmd


class Menu(cmd.Cmd):
    def __init__(self, cookie):
        cmd.Cmd.__init__(self)
        self.prompt = " >>> "
        self.cookie = cookie

    def do_help(self, arg):
        print 'Sheet helps'
        print '\tAccept callinno -> accept a sheet'
        print '\tHelp -> print command help'

    def do_exit(self):
        return True

    def do_run(self, args):
        '''[*] run'''
        print "it's running"

    def do_accept(self, args):
        '''[*] accept sheet'''
        print "sending data"


