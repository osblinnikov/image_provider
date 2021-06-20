
from snocs_helper import *
#           Environment
Import( 'env' )

def add_dependencies(env):
    # AddDependency(env,'libcaf_core','github.com/actor-framework/libcaf_core')
    # AddPthreads(env)
    # AddNetwork(env)
    # AddOpenGL(env)
    return

c = {}
c['PROG_NAME'] = 'image_provider'
c['libFiles'] = ['image_provider.c']
c['testFiles'] = ['tests.c']
c['runFiles'] = ['main.c']
c['defines'] = []
c['depsDynamic'] = add_dependencies
c['depsStatic'] = add_dependencies
c['runnableOnly'] = False
DefaultLibraryConfig(env,c)
