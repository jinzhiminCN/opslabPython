
# coding=UTF-8
# version=3.x

import sys
import optparse

parser = optparse.OptionParser()
parser.add_option('-f', '--file', dest="filename", help="handler file", metavar="FILE")
parser.add_option('-q', '--quiet', action="store_false", dest="verbose", default=True,
                  help="don't print status messages to stdout")

(options, args) = parser.parse_args()

print(options.filename, options.verbose)
