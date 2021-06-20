
from snocs_helper import *
from builder import *
import copy
#           Environment
Import( 'env' )

def with_gpp(env):
    # Replace current compiler with g++
    args = copy.deepcopy(env['scons']['ARGUMENTS'])
    arg_list = copy.deepcopy(env['scons']['ARGLIST'])

    args['compiler'] = 'gpp'
    args['platform'] = 'x64'
    arg_list.append(('cppflag', '-std=c++11'))

    nenv = prepare_env(args, arg_list)
    
    env['scons']['TOOLS']=nenv['TOOLS']
    env['scons']['CC']=nenv['CC']
    env['scons']['CPPFLAGS'].clear()
    env['scons']['CPPFLAGS'].extend(nenv['CPPFLAGS'])
    env['scons']['CCFLAGS'].clear()
    env['scons']['CCFLAGS'].extend(nenv['CCFLAGS'])
    env['scons']['CPPDEFINES'].clear()
    env['scons']['CPPDEFINES'].extend(nenv['CPPDEFINES'])
    

def with_opencv(env):
    conf = Configure(env['scons'])
    env['scons'].ParseConfig('pkg-config --cflags --libs opencv4')
    env['scons'] = conf.Finish()

def add_dependencies(env):
    # AddDependency(env,'libcaf_core','github.com/actor-framework/libcaf_core')
    # AddPthreads(env)
    # AddNetwork(env)
    # AddOpenGL(env)
    return

with_gpp(env)
with_opencv(env)

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
