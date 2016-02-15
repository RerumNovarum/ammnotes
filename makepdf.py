#!/usr/bin/python3

"""
Produces PDF from directories consisting of markdown or html pages using pandoc.
Relative links in files are fixed with pandocfilters
"""

import os
import sys
import shutil
import argparse
import itertools
import subprocess
from collections import deque

latex_engine='xelatex'
mainfont=os.environ.get('mainfont') or 'CMU Serif'
mathfont=os.environ.get('mathfont') or 'Asana Math'
margin=2.5
outfile=os.environ.get('outfile') or 'out.pdf' # ./out/out.pdf

fixpaths_script=os.environ.get('fixpaths') or os.path.join(os.path.split(os.path.realpath(__file__))[0], 'fixpaths.py')

filters = [fixpaths_script,]

CWD = os.getcwd()

pandoc_args = [ 'pandoc',
                '--latex-engine=xelatex',
                '-V', 'mainfont=%s' % mainfont,
                '-V', 'mathfont=%s' % mathfont,
                '-V', 'geometry:margin=%.1fcm' % margin,
                '-S'
                ]
pandoc_pre_args = list(itertools.chain(pandoc_args, *[ ('--filter', f) for f in filters ]))

prepr = dict()

def exec(args):
    print(args)
    subprocess.call(args)

def exec_pandoc(args):
    exec(pandoc_args + args)

def exec_pandoc_pre(args):
    exec(pandoc_pre_args + args)

def pandoc(infile, virtdir, outdir):
    """
    converting file to tex using `pandoc`
    """
    name = os.path.split(infile)[1]
    outfile = os.path.join(outdir, name + '.tex')
    exec_pandoc_pre([infile, '-o', outfile])
    return os.path.join(virtdir, name + '.tex')
for f in ['.tex', '.htm', '.html', '.md', '.markdown', '.odt', '.docx', '.epub']: prepr[f] = pandoc

def nbconvert(infile, virtdir, outdir):
    """
    executing Jupyter notebook and processing tex using `jupyter nbconvert`
    """
    olddir = os.getcwd()
    name = os.path.split(infile)[1]
    outfile = os.path.join(outdir, name + '.tex')
    outcopy = os.path.join(outdir, name + '.ipynb')
    shutil.copy(infile, outcopy)
    os.chdir(outdir)
    args = ['jupyter', 'nbconvert', '-y', '--to', 'markdown', name]
    exec(args)
    os.chdir(olddir)
    outmd = os.path.join(outdir, name + '.md')
    pandoc(outmd, outfile)
    return os.path.join(virtdir, name + '.tex')
prepr['.ipynb'] = nbconvert

def copy(infile, virtdir, outdir):
    """
    copying raw file
    """
    shutil.copy(infile, outdir) 
for f in ['', '.jpg', '.jpeg', '.jpe', '.png', '.tif', '.gif']: prepr[f] = copy

def ignore(infile, virtdir, outdir):
    """
    ignoring file
    """
    pass

def preprocess(infile, virtdir, outdir):
    os.environ['pandoc_file'] = infile
    os.environ['pandoc_virtdir'] = virtdir
    ext = os.path.splitext(infile)[1]
    p   = prepr.get(ext, ignore)
    if p: print(p.__doc__)
    else: print('Unknown filetype: %s'%ext)
    print(infile)
    r   = p(infile, virtdir, outdir)
    if r:
        global sources
        sources.append(r)
    return r

sources = []
if __name__ == '__main__': 
    parser = argparse.ArgumentParser(prog='makepdf', description=__doc__)
    parser.add_argument('-r', '--recursive', action='store_true', help='recursively source files from subdirectories')
    parser.add_argument('src', nargs='+', type=str, help='directories to process')
    args = parser.parse_args()
    
    if os.path.isdir('out'): 
        shutil.rmtree('out')
    os.mkdir('out')

    q = deque()
    for s in args.src:
        if os.path.isdir(s): q.append( (s, os.path.split(s.rstrip('/'))[1]) )
        else: q.append( (s, './') )

    while len(q):
        src, virtdir = q.popleft()
        outdir = os.path.join('out', virtdir)
        def handle_file(file, virtdir, name):
            print('----')
            virt = os.path.join(virtdir, name + '.tex')
            outfileabs = os.path.join(CWD, 'out', virt)
            preprocess(file, virtdir, outdir)
        if os.path.isfile(src):
            handle_file(src, '', os.path.split(src)[1])
        elif os.path.isdir(src):
            outdirabs = os.path.join('out', virtdir)
            if not os.path.isdir(outdirabs): os.mkdir(outdirabs)
            for name in os.listdir(src):
                if name[0] == '.' or name.startswith('__'): continue
                path = os.path.join(src, name)
                if os.path.isfile(path):
                    handle_file(path, virtdir, name)
                else: 
                    if os.path.islink(path): continue
                    q.append( (path, os.path.join(virtdir, name)) )
    os.chdir(os.path.join(CWD, 'out'))
    print("""
    producing pdf
    """)
    exec_pandoc(['-s', '-o', 'out.pdf'] + sources)
