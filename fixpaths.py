#!/usr/bin/env python3

import os
import sys
from urllib.parse import urljoin
from  pandocfilters import toJSONFilter, Image, Link

constructors = {'Image': Image, 'Link': Link}

file = os.environ.get('pandoc_file')
base_dir = os.environ.get('pandoc_virtdir')
if base_dir == '': base_dir = './'
if not base_dir.endswith('/'): base_dir += '/' # that's for urllib

def fixpath(key, value, format, meta):
    if key in ['Link', 'Image']:
        oldpath = value[2][0]
        newpath = oldpath if oldpath.startswith('#') else urljoin(base_dir, oldpath)
        print('"%s" -> "%s"'%(oldpath, newpath), file=sys.stderr)
        value[2][0] = newpath
        return constructors[key](*value)
        

if __name__ == '__main__':
    toJSONFilter(fixpath)
