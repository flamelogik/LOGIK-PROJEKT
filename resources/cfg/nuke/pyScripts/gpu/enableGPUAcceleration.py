import nuke

###Version 1.0.0

def enableGPUAcceleration():
    for i in nuke.allNodes():
        if i.knob('useGPUIfAvailable'):
            i.knob('useGPUIfAvailable').setValue(1)
        if i.knob('r3dUseCUDA'):
            i.knob('r3dUseCUDA').setValue(1)
        if i.knob('arriUseCUDA'):
            i.knob('r3dUseCUDA').setValue(1)
        ## apDespill:
        if i.knob('Use GPU if Available'):
            i.knob('Use GPU if Available').setValue(1)


def main():
    nuke.message('enabling GPU 123')
    enableGPUAcceleration()