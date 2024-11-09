# this returns something different in the interactive session vs script...


'''
in interactive mode, show nuke and modules imported in the menu/init files...


for variable_name, variable_value in globals().items():
    if isinstance(variable_value, types.ModuleType):
        print(f"{variable_name}: {variable_value}")


        


'''


import sys
import types
def print_global_namespace():
    for variable_name, variable_value in globals().items():
    #for variable_name, variable_value in sys.modules.items():
        if isinstance(variable_value, types.ModuleType):
            print(f"{variable_name}: {variable_value}")


def main():
    #print_global_namespace()
    for variable_name, variable_value in globals().items():
    #for variable_name, variable_value in sys.modules.items():
        if isinstance(variable_value, types.ModuleType):
            print(f"{variable_name}: {variable_value}")


def __main__():
    main()