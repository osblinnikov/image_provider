
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
    arg_list.append(('cppflag', '-std=c++11'))

    return prepare_env(args, arg_list)

def AddOpenCV(env):
    conf = Configure(env['prj_env'])
    env['prj_env'].ParseConfig('pkg-config --cflags --libs opencv4')
    env['prj_env'] = conf.Finish()

def add_dependencies(env):
    AddOpenCV(env)
    # AddDependency(env,'libcaf_core','github.com/actor-framework/libcaf_core')
    # AddPthreads(env)
    # AddNetwork(env)
    # AddOpenGL(env)
    return

nenv = with_gpp(env)

c = {}
c['PROG_NAME'] = 'image_provider'
c['libFiles'] = ['image_provider.c']
c['testFiles'] = ['tests.c']
c['runFiles'] = ['main.c']
c['defines'] = []
c['depsDynamic'] = add_dependencies
c['depsStatic'] = add_dependencies
c['runnableOnly'] = False

c['TOOLS'] = nenv['TOOLS']
c['CC'] = nenv['CC']
c['LINKFLAGS'] = nenv['LINKFLAGS']
c['CCFLAGS'] = nenv['CPPFLAGS']
c['CPPDEFINES'] = nenv['CPPDEFINES']
c['LINKFLAGS'] = nenv['LINKFLAGS']
c['LIBPATH'] = nenv['LIBPATH']

DefaultLibraryConfig(env,c)
