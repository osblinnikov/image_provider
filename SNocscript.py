
from snocs_helper import *
from builder import *
import copy
#           Environment
Import( 'env' )

def with_gpp(env):
    # Replace current compiler with g++
    args = copy.deepcopy(env['prj_env']['ARGUMENTS'])
    arg_list = copy.deepcopy(env['prj_env']['ARGLIST'])

    args['compiler'] = 'gpp'
    args['platform'] = 'x64'

    nenv = prepare_env(args, arg_list)

    env['prj_env']['TOOLS'] = nenv['TOOLS']
    env['prj_env']['CC'] = nenv['CC']
    env['prj_env']['LINKFLAGS'] = nenv['LINKFLAGS'] + ['-std=c++11']
    env['prj_env']['CPPFLAGS'] = nenv['CPPFLAGS'] + ['-std=c++11']
    env['prj_env']['CCFLAGS'] = []
    env['prj_env']['CPPDEFINES'] = nenv['CPPDEFINES']
    env['prj_env']['LIBPATH'] = nenv['LIBPATH']

def AddOpenCV(env):
    env['prj_env'].ParseConfig('pkg-config --cflags --libs opencv4')

def add_dependencies(env, run):
    with_gpp(env)
    AddOpenCV(env)
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
