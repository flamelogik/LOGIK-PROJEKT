import nuke

###Version 1.0.0

def disableGPUAcceleration():
    for i in nuke.allNodes():
        if i.knob('useGPUIfAvailable'):
            i.knob('useGPUIfAvailable').setValue(0)
        if i.knob('r3dUseCUDA'):
            i.knob('r3dUseCUDA').setValue(0)
        if i.knob('arriUseCUDA'):
            i.knob('r3dUseCUDA').setValue(0)
        ## apDespill:
        if i.knob('Use GPU if Available'):
            i.knob('Use GPU if Available').setValue(0)


def main():
    nuke.message('disabling GPU acceleration knobs...')
    disableGPUAcceleration()