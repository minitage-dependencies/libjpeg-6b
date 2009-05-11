import os
import shutil
from minitage.core.common import which

def pre_make(options, buildout):
    """Custom pre-make hook for building libjpeg."""
    # The installation procedure is arrogant enough to expect all the
    # directories to exist and fails otherwise.
    for dir in ('bin', 'man/man1', 'include', 'lib'):
        os.makedirs(
            os.path.join(options['location'], dir)
        )
def libtoolize(options, buildout):
    cwd = os.getcwd()
    os.chdir(options['compile-directory'])
    l = None
    try:
        l = which('libtoolize')
    except Exception, e:
        pass
    if l:
        os.remove('libtool-wrap')
        shutil.copy('libtool', 'libtool-wrap')
        os.system(l)
    os.chdir(cwd)



