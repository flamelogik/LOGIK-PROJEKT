


import os
import platform
import string
import json
import shutil
import subprocess
import sys
import traceback
import flame

#####
synflame_config_filename = "/Users/tradecraft_vfx/Library/Application Support/SynthEyes/flame_config.json"
SYFLAME_VERSION = 1.05
# Leave the PREVIOUS two lines alone! (except to change the version#)
#####
syndebug = 0
synNoteTag='SYFLAME='

# SynthEyes Data Importer --- to be installed and run in Flame's python. 
#     It reads .syflame files produced by the "File/Export/Flame 2025+" 
#     exporter.
# NOT a python script for SynthEyes! Don't tag it for SynthEyes's script-finder.
# syntax check:  python3 -c "import ast; ast.parse(open('synflame.py').read())"
# Note: use flame.messages.show_in_dialog(...) as needed

allowed_functions = [
"syGotoBatch", "syGetMediaNode", "syGetActionNode", "syCreateLDNode",
"syCreateComp", "syConnectNodes", "sySetNodePos", "sySetOffsetPos",
"syWrap", "syImportClip", "syAddMedia", "syConnectClip", "syDeleteNode",
"syApplyTexToMap", "sySaveState", "syRestoreState", "syNodeByName",
"sySetFrame", "syLoadLDNode", "syUpdExtra", "syUpTkS", "syUpTkMS",
"syUpTkMF", "syUpMshS", "syUpCamInfo", "syUpCamSA", "syUpCamSI",
"syUpCamSR", "syUpCamFP", "syUpCamFPA", "syUpCamFPI", "syUpCamFPR",
"syUpCamFPF", "syUpCamFPAF", "syUpCamFPIF", "syUpCamFPRF", "syUpCamFA",
"syUpCamFI", "syUpCamFR", "syUpCamFF", "syUpCamFAF", "syUpCamFIF",
"syUpCamFRF", "syRemapFile", "syUpLiteS", "sySetLiteC", "syUpLiteF",
"syUpMobS", "syUpMobF", "syCheckNew", "syCheckUpdate", "syUpMshABC",
"syUpMshFBX", "syUpMshSP", "syUpTkSP", "sySetRenderable", "sySyFlameVersion",
"syIfBatchNodeMissing", "syIfBatchNodeExists", "syDeleteBatchNode",
"syManifestDestiny", "syReadManifest", "syAbort", "syUpDefCamInfo",
"syWriteManifest", "sySetOverscan", "syCheckOverscan", "syCamTrackersNode", 
"sySetParent", "sySaveWorld", "syRestoreWorld", "sySetAutoKey",
"syWrapUpdate", "syConnectRender", "syAddSurface",
        ]

synfile_fromlist = []
synfile_tolist = []
synlinecnt = 0


def MyDecode(hex_string):
    i = 0
    n = len(hex_string)
    rv = ""
    while i < n:
        ch = hex_string[i]
        i += 1
        if ch == "%":
            rv += "%c" % int(hex_string[i:i+2],16)
            i += 2
        elif ch == "+":
            rv += " "
        else:
            rv += ch
    return rv

def InitFileAdjust(prjdir):
    global synfile_fromlist, synfile_tolist

    synfile_fromlist = []
    synfile_tolist = []
    synfile_fromlist.append('SYN_PROJECT')
    synfile_tolist.append(prjdir)

def AdjustFileName(fnm, ctx):
    global synfile_fromlist, synfile_tolist

    for i in range(0, len(synfile_fromlist)):
        tag = synfile_fromlist[i]
        if tag != 'SYN_PROJECT':            # get environment variable
            val = os.getenv(tag, synfile_tolist[i]) # tolist is the default
        else:
            val = synfile_tolist[i]         # don't even look for project
        fnm = AdjustFileImp(fnm, "<[" + tag + "]>", val)
    return fnm

def AdjustFileImp(fnm, from_prefix, to_prefix):
    if from_prefix == None:
        return fnm
    if to_prefix == None:
        to_prefix = ""
    prefl = len(from_prefix)
    if prefl > 0 and fnm[0:prefl] == from_prefix:
        fnm = to_prefix + fnm[prefl:]
    return fnm

def ReplaceFileNames(txt, ctx):
    global synfile_fromlist, synfile_tolist

    for i in range(0, len(synfile_fromlist)):
        tag = synfile_fromlist[i]
        if tag != 'SYN_PROJECT':            # get environment variable
            val = os.getenv(tag, synfile_tolist[i]) # tolist is the default
        else:
            val = synfile_tolist[i]         # don't even look for project
        txt = txt.replace("<[" + tag + "]>", val)
    return txt

def read_syntheyes_export(filename):
    global allowed_functions, synlinecnt
    ctx = {}
#    ctx["fbias"] = 0    # not currently supported
    ctx["ok"] = 1
    ctx['blocked'] = 0
    ctx['batch'] = flame.batch
    ctx['mediahub'] = flame.mediahub
    ctx['messages'] = flame.messages
    ctx['timeline'] = flame.timeline
    ctx['renderable'] = ''
    ctx['tplunk_dx'] = 100
    ctx['tplunk_dy'] = 100
    ctx['tplunk_x0'] = 100       # avoid Default Camera
    ctx['tplunk_x'] = ctx['tplunk_x0']
    ctx['tplunk_y'] = 100
    ctx['tplunk_width'] = ctx['tplunk_x0'] + 10*ctx['tplunk_dx']
    ctx['mplunk_dx'] = 100
    ctx['mplunk_dy'] = 100
    ctx['mplunk_x0'] = 100 + 14*ctx['mplunk_dx']       # avoid Default Camera
    ctx['mplunk_x'] = ctx['mplunk_x0']
    ctx['mplunk_y'] = 100
    ctx['mplunk_width'] = ctx['mplunk_x0'] + 10*ctx['mplunk_dx']
    if syndebug > 0:
        fout = open(os.getenv('HOME') + "/pylog.txt", "w")
        fout.write("Opening filename " + filename + "\n")
        fout.flush()
        flame.messages.show_in_console("read_syntheyes_export "+filename, duration=3)
    if not os.path.isfile(filename):
        ctx["ok"] = 0
        flame.messages.show_in_console("File not found: " + filename, duration=15)
        return ctx
    InitFileAdjust(os.path.dirname(filename))
    funcs = {}      # for quicker function lookup
    for func_name in allowed_functions:
        funcs[func_name] = globals()[func_name]
    f = open(filename, "r")
    if syndebug > 0:
        fout.write("Opened filename " + filename + "\n")
        fout.flush()
        flame.messages.show_in_console("opened "+filename, duration=3)
    synlinecnt = 0
    for line in f:
        if syndebug > 0:
            fout.write("Line: " + line + "\n")
        synlinecnt += 1
        if "#" in line:
            idx = line.find("#")
            line = line[:idx]
        tokens = line.split()
        if len(tokens) > 0:
            func_name = "sy" + tokens[0]
            args = tokens[1:]
            if func_name == 'syEndCond':
                ctx['blocked'] = 0
            elif ctx['blocked'] > 0:
                pass
            elif func_name in allowed_functions:
                funcs[func_name](args, ctx)    # pass ctx by reference
            else:
                if syndebug > 0:
                    fout.write(SyLine() + "Unrecognized command function " + func_name + "\n")
                flame.messages.show_in_dialog("Error!", 
                    (SyLine() + "Unrecognized command function "+func_name+". "
                        + "Run SynthEye's 'Integrate with Flame' "
                        + "and Flame's 'Rescan python hooks' "
                        + "and check for other version mismatches. "),
                    'error', ['Cancel'], '')
                break
        if ctx["ok"] != 1:        
            break
    f.close()
    if syndebug > 0:
        fout.close()
    if ctx['ok'] == 1:
        flame.messages.show_in_console("Finished reading "+filename, duration=10)
    else:
        flame.messages.show_in_console("ABORTED reading "+filename, duration=10)
    return ctx

def SyLine():
    global synlinecnt
    return "Input line " + str(synlinecnt) + ": "


def FindBatchNone(nm, ctx):
    try:
        return flame.batch.get_node(nm)
    except:
        return None

def FindBatchErr(nm, ctx):
    try:
        return flame.batch.get_node(nm)
    except:
        flame.messages.show_in_dialog("Error!", 
                (SyLine() + "Couldn't find the batch node named "+nm+
                        ", please change it back.\nAborting!"),
                'error', ['Cancel'], '')
        ctx['ok'] = 0


def ExistsInAction(nm, ctx):
    try:
        action = ctx['action']
        if action.get_node(nm) is not None:
            return True
    except:
        pass
    return False

def FindActionNone(nm, ctx):
    try:
        action = ctx['action']
        return action.get_node(nm)
    except:
        return None

def FindActionErr(nm, ctx):
    try:
        action = ctx['action']
        return action.get_node(nm)
    except:
        flame.messages.show_in_dialog("Error!", 
                (SyLine() + "Couldn't find the action node named "+nm+
                        ", please change it back.\nAborting!"),
                'error', ['Cancel'], '')
        ctx['ok'] = 0
        return None

def FindBatchByType(ty):
    cnt = 0
    fnd = None
    for nd in flame.batch.nodes:
        if nd.type == ty:
            fnd = nd
            cnt += 1
    if cnt > 1:
        fnd = None
    return fnd

# These are used to place unexpectedly new nodes.

def PlunkNewTNode(nd, ctx):
    nd.pos_x = ctx['tplunk_x']
    nd.pos_y = ctx['tplunk_y']
    ctx['tplunk_x'] += ctx['tplunk_dx']
    if ctx['tplunk_x'] >= ctx['tplunk_width']:
        PlunkNewTRow(ctx)

def PlunkNewTRow(ctx):
    ctx['tplunk_x'] = ctx['tplunk_x0']
    ctx['tplunk_y'] += ctx['tplunk_dy']

def PlunkNewMNode(nd, ctx):
    nd.pos_x = ctx['mplunk_x']
    nd.pos_y = ctx['mplunk_y']
    ctx['mplunk_x'] += ctx['mplunk_dx']
    if ctx['mplunk_x'] >= ctx['mplunk_width']:
        PlunkNewMRow(ctx)

def PlunkNewMRow(ctx):
    ctx['mplunk_x'] = ctx['mplunk_x0']
    ctx['mplunk_y'] += ctx['mplunk_dy']

#
########################################################################
# Stub routines to execute the commands
########################################################################
#
def syAbort(args, ctx):
    flame.messages.show_in_dialog("Abort, abort!", 
            "SynthEyes detected an error and aborted while exporting. "
            + "There is no useful information in this file. ",
            'error', ['Cancel'], '')
    ctx['ok'] = 0

def sySyFlameVersion(args, ctx):
    file_version = float(args[0])
    if round(1000*file_version) > round(1000*SYFLAME_VERSION):
        flame.messages.show_in_dialog("Uh Oh, Too New!", 
            ("The syflame file being imported is for version " 
            + str(file_version)
            + " but this python code is version " + str(SYFLAME_VERSION)
            + ". You should manually load this file using its .py file, "
            + "via the python console. "),
            'warning', ['Cancel'], '')
        ctx['ok'] = 0
    if round(1000*file_version) < round(1000*SYFLAME_VERSION):
        flame.messages.show_in_dialog("Uh Oh, Too Old!", 
            ("The syflame file being imported is for version " 
            + str(file_version)
            + " but this python code is version " + str(SYFLAME_VERSION)
            + ". You should manually load this file using its .py file, "
            + "via the python console. "),
            'warning', ['Cancel'], '')
        ctx['ok'] = 0

# See if the action node exists, if so, the scene has already been imported
#   and we may need to blow it away

def syCheckNew(args, ctx):
    actnm = MyDecode(args[0])
    actnod = FindBatchNone(actnm, ctx)  # look for Cam#Action in Batch
    if actnod is not None:
        rv = flame.messages.show_in_dialog("Starting Over?", 
                ("It looks like the SynthEyes track was previously imported "
                + "into the project. Delete all nodes except the clip, "
                + "to remove that prior track and earlier work, "
                + "so that the 'Receive' can be performed???\n\n"
                + "Or, you may need to run an 'Update' "
                + "export in SynthEyes (which would have happened "
                + "automatically in 'Auto' mode). Cancel for now.\n\n"
                + "If neither option sounds right,  "
                + "you can Cancel and then rename '" + actnm + "' "
                + "and any other SynthEyes-generated nodes before "
                + "re-running this 'Receive' operation.\n\n"),
            'question', ['Yes'], 'Cancel')
        if rv == 'Yes':
            zap = []
            for nd in flame.batch.nodes:
                if isinstance(nd, flame.PyClipNode):
                    conn = nd.sockets['output']     # check if a Media input
                    toMedia = 0
                    if len(conn) > 1:
                        key0 = next(iter(conn))
                        conns = conn[key0]  # names of nodes output is conn to
                        for trg in conns:
                            if flame.batch.get_node(trg).type == 'Action Media':
                                toMedia = 1
                    if toMedia > 0:         # only delete if conn to media inp.
                        zap.append(nd)
                else:
                    zap.append(nd)
            for nd in zap:
                flame.PyNode.delete(nd)
            # Now good to proceed with the import
        else:
            ctx['ok'] = 0       # import will terminate

def syCheckUpdate(args, ctx):
    actnm = MyDecode(args[0])
    actnod = FindBatchNone(actnm, ctx)  # look for Cam#Action in Batch
    if actnod is None:
        actcnt = 0
        fnd = None
        for nd in flame.batch.nodes:
            if nd.type == 'Action':
                fnd = nd
                actcnt += 1
        if actcnt == 0:
            flame.messages.show_in_dialog("Hmmmm?", 
                ("This 'Update' cannot be processed because there is "
                    + "no Action node (eg '" + actnm + "')\n\n. "
                    + "You must redo the export from SynthEyes "
                    + "with \"Force 'New' exports\" checked. "
                    + "After loading it into Flame, "
                    + "export again with \"Force 'New' exports\" "
                    + "turned off."),
                'error', ['Ok'], '')
            ctx['ok'] = 0       # import will terminate
        elif actcnt == 1:
            rv = flame.messages.show_in_dialog("Hmmmm?", 
                ("It looks like you have renamed the Action node to "
                    + "'" + fnd.name + "'. "
                    + "Can we change the Action node back to the "
                    + "expected name, '" + actnm + "' and proceed?\n\n"
                    + "Otherwise, you should cancel and redo the export "
                    + "from SynthEyes with \"Force 'New' exports\" checked."),
                'question', ['Yes'], 'Cancel')
            if rv == 'Yes':
                fnd.name = actnm
            else:
                ctx['ok'] = 0       # import will terminate
        else:
            flame.messages.show_in_dialog("Hmmmm?", 
                ("This 'Update' cannot be processed because there is "
                    + "no Action node named '" + actnm + "'. "
                    + "You should change the correct Action node "
                    + "back to that name. "),
                'error', ['Ok'], '')
            ctx['ok'] = 0       # import will terminate

def syRemapFile(args, ctx):
    global synfile_fromlist, synfile_tolist
    synfile_fromlist.append(MyDecode(args[0]))
    synfile_tolist.append(MyDecode(args[1]))

def syGotoBatch(args, ctx):
    flame.batch.go_to()

def syGetMediaNode(args, ctx):
    mediaName = MyDecode(args[0])
    medianode = FindBatchNone(mediaName, ctx)
    medianode = None
    cnt = 0
    for nd in flame.batch.nodes:
        if nd.name == mediaName and FindUnderlying(nd) is not None:
            medianode = nd
            cnt += 1
    if medianode is None or cnt > 1:
        medianode = FindClip([])
        if medianode is None or medianode.name != mediaName:
            flame.messages.show_in_dialog("Error!", 
                (SyLine() + "Couldn't find the clip node named "+mediaName+
                        ", please change it back.\nAborting!"),
                'error', ['Cancel'], '')
            ctx['ok'] = 0
            return
    ctx['medianode'] = medianode
    clp = FindUnderlying(medianode)      # the PyClip with useful info!
    ctx['pyclip'] = clp      # the PyClip with useful info!
    ctx['clip_frame_rate'] = clp.frame_rate   # incls DF/NDF state!
    
def syGetActionNode(args, ctx):
    actnm = MyDecode(args[0])
    actfile = AdjustFileName(MyDecode(args[1]), ctx)
    action = flame.batch.create_node('Action')
    eff_actfile = os.path.dirname(actfile) +"/eff_"+ os.path.basename(actfile)
    try:
        with open(actfile, 'r') as file:    # replace tag with project start
            actdata = file.read()
    except:
        flame.messages.show_in_dialog("Where'd it go?", 
            (SyLine() + "The action file " + actfile + " doesn't exist. "
                    + "Did your export from SynthEyes abort? "
                    + "We're aborting now!"),
            'error', ['Cancel'], '')
        ctx['ok'] = 0
        return
    actdata = ReplaceFileNames(actdata, ctx)
    with open(eff_actfile, 'w') as file:    # replace tag with project start
        file.write(actdata)
    action.load_node_setup(eff_actfile)
    try:
        action.name = actnm
    except:
        flame.messages.show_in_dialog("Error!", 
            (SyLine() + "An Action node with this name (" + actnm
                    + ") already exists "
                    + "from a previous run. You're loading a 'New' scene "
                    + "into an already set up Batch group. "
                    + "Please delete any existing SynthEyes-created "
                    + "batch nodes, then try again.\nAborting!"),
            'error', ['Cancel'], '')
        ctx['ok'] = 0
        return
    ctx['action'] = action

def syCreateLDNode(args, ctx):
    ldnm = MyDecode(args[0])
    ldfile = AdjustFileName(MyDecode(args[1]), ctx)
    which = int(args[2])
    nd = FindBatchNone(ldnm, ctx)
    if nd is not None:
        flame.PyNode.delete(nd)
    ldnode = flame.batch.create_node("Lens Distortion")
    ldnode.name = ldnm
    ldnode.load_node_setup(ldfile)
    ctx['redistort' if which > 0 else 'undistort'] = ldnode

def syCreateComp(args, ctx):
    ndnm = MyDecode(args[0])
    nd = FindBatchNone(ndnm, ctx)
    if nd is not None:
        flame.PyNode.delete(nd)
    compnode = flame.batch.create_node("Comp")
    compnode.name = ndnm
    ctx['compnode'] = compnode

def syConnectNodes(args, ctx):
    nd1 = MyDecode(args[0])     # the name in the context
    sk1 = MyDecode(args[1])
    nd2 = MyDecode(args[2])     # the name in the context
    sk2 = MyDecode(args[3])
    flame.batch.connect_nodes(ctx[nd1], sk1, ctx[nd2], sk2)

# See if we're in a timeline BFX group and there's a render node that
#   needs to be connected up. It will initially be connected to the clip
# Connects to Front and Matte on Render

def syConnectRender(args, ctx):
    srcnm = MyDecode(args[0])
    imgsock = MyDecode(args[1])
    matsock = MyDecode(args[2])
    src = FindBatchErr(srcnm, ctx)
    rend = None
    cnt = 0
    for nd in flame.batch.nodes:
        if nd.type == 'Render':
            rend = nd
            cnt += 1
    if cnt != 1:
        return          # don't do anything
    inps = rend.sockets['input']['Front']
    if len(inps) > 1:
        return
    if len(inps) == 1:
        ck = FindBatchErr(inps[0], ctx)     # node render.Front is connected to
        if not (ck.type == 'Action' 
                or ck.name.get_value() == ctx['medianode'].name.get_value()):
            return
    if imgsock in src.output_sockets:       # make sure it has it, esp Action
        flame.batch.connect_nodes(src, imgsock, rend, 'Front')
    if matsock in src.output_sockets:       # make sure it has it, esp Action
        flame.batch.connect_nodes(src, matsock, rend, 'Matte')


def sySetNodePos(args, ctx):
    nd = MyDecode(args[0])
    ctx[nd].pos_x = ctx['medianode'].pos_x + int(args[1])
    ctx[nd].pos_y = ctx['medianode'].pos_y + int(args[2])

def sySetOffsetPos(args, ctx):
    nd = MyDecode(args[0])
    setnd = ctx[MyDecode(args[0])]
    fromnd = ctx[MyDecode(args[1])]
    setnd.pos_x = fromnd.pos_x + int(args[2])
    setnd.pos_y = fromnd.pos_y + int(args[3])

def syWrap(args, ctx):
    flame.batch.frame_all()
    flame.batch.select_nodes([ctx['action']])


#
# Code for flameMesh's ApplyTexture:
#

def syImportClip(args, ctx):
    clipvar = MyDecode(args[0])
    txfile = AdjustFileName(MyDecode(args[1]), ctx)
    txreel = MyDecode(args[2])
    clipnm = MyDecode(args[3])
    clip = flame.batch.import_clip(txfile, txreel)
    clip.name = clipnm
    ctx[clipvar] = clip

# AddMedia is a bit tricky, needs to record the index of the created media,
#   and save the last two nodes so we can delete them later!

def syAddMedia(args, ctx):       # important: records index!
    action = ctx['action']
    inpvar = MyDecode(args[0])
    ctx[inpvar + "_idx"] = len(action.media_layers)
    ctx[inpvar] = action.add_media()
    nolis = action.nodes
    noliscnt = len(nolis)
    ctx['axistarget'] = nolis[noliscnt-2]
    ctx['surftarget'] = nolis[noliscnt-1]

def syConnectClip(args, ctx):
    clipvar = MyDecode(args[0])
    clipnd = ctx[clipvar]
    inpvar = MyDecode(args[1])
    inpnd = ctx[inpvar]
    onames = clipnd.output_sockets
    flame.batch.connect_nodes(clipnd, onames[0], inpnd, 'Front')
    if len(onames) >= 2:
        flame.batch.connect_nodes(clipnd, onames[1], inpnd, 'Matte')

def syDeleteNode(args, ctx):
    ndnm = MyDecode(args[0])        # Note: name of variable containing node
    nd = ctx[ndnm]                  # not the name of the node itself
    flame.PyNode.delete(nd)

def syDeleteBatchNode(args, ctx):
    ndnm = MyDecode(args[0])        # Note: name of node
    nd = FindBatchNone(ndnm, ctx)
    if nd is not None:
        flame.PyNode.delete(nd)

def syApplyTexToMap(args, ctx):
    action = ctx['action']
    mapnm = MyDecode(args[0])
    inpvar = MyDecode(args[1])
    nd = action.get_node(mapnm)
    nd.assign_media(ctx[inpvar + "_idx"])   # retrieve its index

def sySaveState(args, ctx):
    frm = int(args[0])
    ctx['prior_autokey'] = flame.batch.auto_key
    ctx['prior_frame'] = flame.batch.current_frame
    flame.batch.current_frame = frm
    flame.batch.auto_key = False

def syRestoreState(args, ctx):
    flame.batch.auto_key = ctx['prior_autokey']
    #flame.batch.current_frame = ctx['prior_frame']

# AddSurface surfacenm parentnm
# This adds the actual surface, *not the axis node controlling it*
#   Then it connects it to the actual axis node
#   Repositions it to the right of the axis node
#   Renames the batch node after the surface name
#   For update purposes, can be re-run; does nothing if the node exists.

def syAddSurface(args, ctx):       # important: records index!
    action = ctx['action']
    surfnm = MyDecode(args[0])
    axisnm = MyDecode(args[1])
    inpnm = MyDecode(args[2])
    axisnd = FindActionErr(axisnm, ctx)
    if axisnd is None:
        return
    surfnd = FindActionNone(surfnm, ctx)
    if surfnd is not None:          # if already exists, do nothing.
        action.connect_nodes(axisnd, surfnd)
        return
    idx = len(action.media_layers)      # in case we need it...
    inpnode = action.add_media()
    nolis = action.nodes
    noliscnt = len(nolis)
    extraxis = nolis[noliscnt-2]          # the new ones are the last two
    surfnd = nolis[noliscnt-1]   # in the list.
    surfnd.name = surfnm
    flame.PyNode.delete(extraxis)         # don't need this one
    action.connect_nodes(axisnd, surfnd)
    surfnd.pos_x = axisnd.pos_x
    surfnd.pos_y = axisnd.pos_y + 60
    inpnode.name = inpnm

#
# Code for UPDATES
#

def syWrapUpdate(args, ctx):
    DeleteNodesAndWriteManifest(ctx)

def sySetAutoKey(args, ctx):
    flame.batch.auto_key = (True if int(args[0]) > 0 else False)

def syNodeByName(args, ctx):
    varnm = MyDecode(args[0])
    ndnm = MyDecode(args[1])
    ctx[varnm] = FindBatchErr(ndnm, ctx)

def sySetFrame(args, ctx):
    flame.batch.current_frame = int(args[0])

def syLoadLDNode(args, ctx):
    ldnm = MyDecode(args[0])
    ldfile = AdjustFileName(MyDecode(args[1]), ctx)
    ldnode = FindBatchErr(ldnm, ctx)
    if ldnode is None:
        return
    ldnode.load_node_setup(ldfile)

def syUpdExtra(args, ctx):
    action = ctx['action']
    xtnm = MyDecode(args[0])
    hlp = FindActionNone(xtnm, ctx)
    if hlp is None:
        hlp = action.create_node('Axis')
        hlp.name = xtnm
        PlunkNewTNode(hlp, ctx)
    hlp.position = (float(args[1]), float(args[2]), float(args[3]))

# Cam1Trackers/DefaultTrackers must be present for enclosed trackers/meshes

def syCamTrackersNode(args, ctx):
    action = ctx['action']
    camnm = MyDecode(args[0])
    wldnm = MyDecode(args[1])
    wld = FindActionNone(wldnm, ctx)
    if wld is None:
        cam = FindActionErr(camnm, ctx)     # this is NOT the parent!
        wld = action.create_node('Axis')
        wld.name = wldnm
        wld.pos_x = cam.pos_x + 40
        wld.pos_y = cam.pos_y
    wld.position = (0.0, 0.0, 0.0)

#------ Trackers --------

def sySetRenderable(args, ctx):
    ctx['renderable'] = AdjustFileName(MyDecode(args[0]), ctx)
    ctx['renderableRate'] = args[1]         # keep as string
    ctx['renderableScale'] = args[2]         # keep as string

def ForceSetName(nd, nm, ctx):
    try:
        nd.name = nm
    except:
        pass
    else:
        return
    cnt = 1
    done = False
    ond = FindActionNone(nm, ctx)
    if ond is None:     # couldn't set it, but not present
        flame.messages.show_in_dialog("Uh oh!", 
                (SyLine() + "This name is unusable: " + nm),
                'error', ['Ok'], '')
        ctx["ok"] = 0
        return
    while not done and cnt < 10:
        try:
            ond.name = nm + str(cnt)
        except:
            pass
        else:
            done = True
        cnt += 1
    try:
        nd.name = nm
    except:
        flame.messages.show_in_dialog("Uh oh!", 
                (SyLine() + "This name is unusable: " + nm),
                'error', ['Ok'], '')
        ctx["ok"] = 0
        return
    flame.messages.show_in_dialog("Check this out!", 
        (SyLine() + "There was an existing node " + nm + "; "
                + "it has been renamed " + ond.name + ". "
                + "You should look at it and maybe delete or reuse it."),
                'warning', ['Ok'], '')

def UpdTrackerSetup(action, tknm, args, cr, ctx):
    tknd = FindActionNone(tknm, ctx)
    if tknd is None:
        tknd = action.create_node('Axis')
        tknd.name = tknm
        PlunkNewTNode(tknd, ctx)
    rfile = ctx['renderable']
    if rfile != '':     # if renderable but doesn't exist, create 
        mshnd = FindActionNone(tknm + "Chisel", ctx)
        if mshnd is None:
            mshnd = action.read_abc(rfile, lights=False, cameras=False, 
                    models=True, normals=True, mesh_animations=False, 
                    frame_rate='24 fps', # must match the CHISEL file's frate!
                    auto_fit=False, 
                    unit_to_pixels=float(ctx['renderableScale']), 
                    consolidate_geometry=True,
                    create_object_group=False)
            if mshnd is None:
                flame.messages.show_in_dialog("Uh oh!", 
                    (SyLine() + "The ABC file for chisels was not found; "
                    + "you'll need to copy in this file manually. "
                    + "The axis node has been configured to position it.\n\n"
                    + mshfile),
                    'error', ['Ok'], '')
            else:       # new renderable node with chisel and material
                mshnd.name = tknm + "Chisel"    # override flame default!
                mshnd.pos_x = tknd.pos_x + 20
                mshnd.pos_y = tknd.pos_y
                action.connect_nodes(tknd, mshnd)
                mtlnd = action.create_node('Material')
                ForceSetName(mtlnd, tknm + 'Mtl', ctx)
                mtlnd.pos_x = tknd.pos_x + 40
                mtlnd.pos_y = tknd.pos_y
                action.connect_nodes(mshnd, mtlnd)
                # TODO: when Flame python permits, set mtl color!
                r = float(args[cr])
                g = float(args[cr+1])
                b = float(args[cr+2])
    return tknd

# must enforce LACK of parentage regardless of whether node is new, may change!

def syUpTkS(args, ctx):
    action = ctx['action']
    tknm = MyDecode(args[0])
    tknd = UpdTrackerSetup(action, tknm, args, 4, ctx)     # 4=red's arg#
    while len(tknd.parents()) > 0:
        action.disconnect_nodes(tknd.parents()[0], tknd)
    tknd.position = (float(args[1]), float(args[2]), float(args[3]))

# must enforce parentage regardless of whether node is new, may change!

def syUpTkSP(args, ctx):
    action = ctx['action']
    tknm = MyDecode(args[0])
    parnm = MyDecode(args[1])       # ie Camera01Far or Object02
    tknd = UpdTrackerSetup(action, tknm, args, 5, ctx)     # 5=red's arg#
    parnd = FindActionNone(parnm, ctx)
    if parnd is None:
        flame.messages.show_in_dialog("Uh oh!", 
            (SyLine() + "The parent node " +parnm+ " of " +tknm 
                + " was not found. Notify support."),
            'error', ['Ok'], '')
    elif tknd not in parnd.children():
        action.connect_nodes(parnd, tknd)
    tknd.position = (float(args[2]), float(args[3]), float(args[4]))

def syUpTkMS(args, ctx):       # static, for moving trackers, no posn here
    action = ctx['action']
    tknm = MyDecode(args[0])
    tknd = UpdTrackerSetup(action, tknm, args, 1, ctx)     # 1=red's arg#
    while len(tknd.parents()) > 0:
        action.disconnect_nodes(tknd.parents()[0], tknd)

def syUpTkMF(args, ctx):
    action = ctx['action']
    tknm = MyDecode(args[0])
    tknd = FindActionErr(tknm, ctx)
    tknd.position = (float(args[1]), float(args[2]), float(args[3]))

#------------------------- Master World node support

def sySaveWorld(args, ctx):         # BEFORE updating poses and parenting
    action = ctx['action']
    wldnm = MyDecode(args[0])
    wldnd = FindActionNone(wldnm, ctx)
    if wldnd is not None:
        ctx['world_pos'] = wldnd.position.get_value()
        ctx['world_rot'] = wldnd.rotation.get_value()
        ctx['world_scl'] = wldnd.scale.get_value()
        wldnd.position.set_value((0., 0., 0.))
        wldnd.rotation.set_value((0., 0., 0.))
        wldnd.scale.set_value((100.0, 100.0, 100.0))
    else:
        wldnd = action.create_node('Axis')
        wldnd.name = wldnm
        PlunkNewTNode(wldnd, ctx)
        ctx['world_pos'] = (0., 0., 0.)
        ctx['world_rot'] = (0., 0., 0.)
        ctx['world_scl'] = (100.0, 100.0, 100.0)

def syRestoreWorld(args, ctx):      # After updating poses and parenting
    action = ctx['action']
    wldnm = MyDecode(args[0])
    wldnd = FindActionErr(wldnm, ctx)
    if wldnd is not None:
        wldnd.position.set_value(ctx['world_pos'])
        wldnd.rotation.set_value(ctx['world_rot'])
        wldnd.scale.set_value(ctx['world_scl'])

def sySetParent(args, ctx):         # Before restoring the world
    action = ctx['action']
    kidnm = MyDecode(args[0])
    kidnd = FindActionNone(kidnm, ctx)
    parnm = MyDecode(args[1])       # ie Camera01Far or Object02
    if parnm != '-':
        parnd = FindActionNone(parnm, ctx)
        if parnd is None:
            flame.messages.show_in_dialog("Uh oh!", 
                (SyLine() + "The parent node " +parnm+ " of " + kidnm 
                    + " was not found. Notify support."),
                'error', ['Ok'], '')
        elif kidnd not in parnd.children():
            action.connect_nodes(parnd, kidnd)
    else:       # no parents
        while len(kidnd.parents()) > 0:
            action.disconnect_nodes(kidnd.parents()[0], kidnd)

#---------- Meshes -----------


# must enforce LACK of parentage regardless of whether node is new, may change!

def syUpMshS(args, ctx):
    action = ctx['action']
    mshnm = MyDecode(args[0])       # ie axisCylinder02
    mshnd = FindActionNone(mshnm, ctx)
    if mshnd is None:
        mshnd = action.create_node('Axis')
        mshnd.name = mshnm
        PlunkNewMNode(mshnd, ctx)
    while len(mshnd.parents()) > 0:
        action.disconnect_nodes(mshnd.parents()[0], mshnd)
    mshnd.position = (float(args[1]), float(args[2]), float(args[3]))
    mshnd.rotation = (float(args[4]), float(args[5]), float(args[6]))
    mshnd.scale = (float(args[7]), float(args[8]), float(args[9]))

# must enforce parentage regardless of whether node is new, may change!

def syUpMshSP(args, ctx):           # with parent
    action = ctx['action']
    mshnm = MyDecode(args[0])       # ie axisCylinder02
    parnm = MyDecode(args[1])       # ie axisCylinder02
    mshnd = FindActionNone(mshnm, ctx)
    if mshnd is None:
        mshnd = action.create_node('Axis')
        mshnd.name = mshnm
        PlunkNewMNode(mshnd, ctx)
    parnd = FindActionNone(parnm, ctx)
    if parnd is None:
        flame.messages.show_in_dialog("Uh oh!", 
            (SyLine() + "The parent node " +parnm+ " of " +mshnm 
                + " was not found. Notify support."),
            'error', ['Ok'], '')
    elif mshnd not in parnd.children():
        action.connect_nodes(parnd, mshnd)
    mshnd.position = (float(args[2]), float(args[3]), float(args[4]))
    mshnd.rotation = (float(args[5]), float(args[6]), float(args[7]))
    mshnd.scale = (float(args[8]), float(args[9]), float(args[10]))

# The ABC file for it, if it is missing!
# Does nothing if it is present

def syUpMshABC(args, ctx):
    action = ctx['action']
    mshnm = MyDecode(args[0])       # just Cylinder02 
    mshfile = AdjustFileName(MyDecode(args[1]),ctx)       # full filename
    frate = MyDecode(args[2])           # leave in int format. UNUSED!
    scale = float(MyDecode(args[3]))
    mshnd = FindActionNone(mshnm, ctx)
    if mshnd is not None:
        return
    frate = ctx['clip_frame_rate']   # incls DF/NDF state! very touchy!
    if not os.path.isfile(mshfile):
        flame.messages.show_in_dialog("Uh oh!", 
            (SyLine() + "The ABC file for '" + mshnm + "' was not found; "
            + "you'll need set up this mesh's ReadFile manually. "
            + "The axis node has been configured to position it.\n\n"
            + mshfile),
            'error', ['Ok'], '')
        return
    try:
        mshnd = action.read_abc(mshfile, lights=False, cameras=False, 
                models=True, normals=True, mesh_animations=True, 
                frame_rate=frate, auto_fit=False,
                unit_to_pixels=scale, consolidate_geometry=True,
                create_object_group=False)
    except:
        flame.messages.show_in_dialog("Uh oh!", 
            (SyLine() + "The ABC file for '" + mshnm + "' apparently "
            + "has a different frame rate than this project. "
            + "They must match, so "
            + "you'll need set up this mesh's ReadFile manually. "
            + "The axis node has been configured to position it.\n\n"
            + mshfile),
            'error', ['Ok'], '')
        return
    PlunkNewMNode(mshnd, ctx)
    mshnd.name = mshnm              # override flame default!
    axnm = 'axis' + mshnm           # find the axis node
    axnd = action.get_node(axnm)
    if axnd is None:
        flame.messages.show_in_dialog("Uh oh!", 
            (SyLine() + "Couldn't find an expected axis node " + axnm),
            'error', ['Ok'], '')
        return
    action.connect_nodes(axnd, mshnd)     # wire them together
    # separate operation to create any material or texture maps
    AddMeshMtl(action, mshnd, mshnm, args, 4, ctx)

# The FBX file for it, if it is missing!
# Does nothing if it is present

def syUpMshFBX(args, ctx):
    action = ctx['action']
    mshnm = MyDecode(args[0])       # just Cylinder02 
    mshfile = AdjustFileName(MyDecode(args[1]),ctx)       # full filename
    frate = MyDecode(args[2])           # leave in int format. UNUSED!
    scale = float(MyDecode(args[3]))
    mshnd = FindActionNone(mshnm, ctx)
    if mshnd is not None:
        return
    mshnd = action.read_fbx(mshfile, lights=False, cameras=False, 
            models=True, normals=True, mesh_animations=True, 
            keep_frame_rate=False, bake_animation=True,  
            object_properties=True, auto_fit=False,
            unit_to_pixels=scale, is_udim=False, relink_material=True)
    if mshnd is None:
        flame.messages.show_in_dialog("Uh oh!", 
            (SyLine() + "The FBX file for '" + mshnm + "' was not found; "
            + "you'll need to this file manually. "
            + "The axis node has been configured to position it.\n\n"
            + mshfile),
            'error', ['Ok'], '')
        return
    PlunkNewMNode(mshnd, ctx)
    mshnd.name = mshnm              # override flame default!
    axnm = 'axis' + mshnm           # find the axis node
    axnd = action.get_node(axnm)
    if axnd is None:
        flame.messages.show_in_dialog("Uh oh!", 
            (SyLine() + "Couldn't find an expected axis node " + axnm),
            'error', ['Ok'], '')
        return
    action.connect_nodes(axnd, mshnd)     # wire them together
    # separate operation to create any material or texture maps
    AddMeshMtl(action, mshnd, mshnm, args, 4, ctx)

def AddMeshMtl(action, mshnd, mshnm, args, cr, ctx):
    if len(args) < cr+3:
        return
    mtlnd = action.create_node('Material')
    mtlnd.name = mshnm + 'Mtl'
    PlunkNewMNode(mtlnd, ctx)
    action.connect_nodes(mshnd, mtlnd)
    # TODO: when Flame python permits, set color!
    r = float(args[cr])
    g = float(args[cr+1])
    b = float(args[cr+2])

#-------------------------------------------------------------------------
# Camera static setups

def syUpCamInfo(args, ctx):         # for 3D cameras
    action = ctx['action']
    camnm = MyDecode(args[0])
    camnd = FindActionErr(camnm, ctx)
    if camnd is None:
        return          # TODO - do something better here!
    camnd.near = float(args[1])
    camnd.far = float(args[2])
    camnd.film_aspect = float(args[3])
    camnd.aperture_x = float(args[4])
    camnd.aperture_y = float(args[5])
    camnd.film_offset_x = float(args[6])
    camnd.film_offset_y = float(args[7])
    # TODO: something like camnd.aim_mode = ('free' if int(args[8]) else 'aim')

def syUpDefCamInfo(args, ctx):      # for Default camera
    action = ctx['action']
    camnm = MyDecode(args[0])
    camnd = FindActionErr(camnm, ctx)
    if camnd is None:
        return          # TODO - do something better here!
    camnd.near = float(args[1])
    camnd.far = float(args[2])
    #camnd.film_aspect = float(args[3])
    #camnd.aperture_x = float(args[4])
    #camnd.aperture_y = float(args[5])
    #camnd.film_offset_x = float(args[6])
    #camnd.film_offset_y = float(args[7])
    camnd.target_mode = (True if int(args[8])>0 else False)


def syUpCamSA(args, ctx):
    action = ctx['action']
    camnm = MyDecode(args[0])
    camnd = FindActionErr(camnm, ctx)
    if camnd is None:
        return
    camnd.position = (float(args[1]), float(args[2]), float(args[3]))
    camnd.aim = (float(args[4]), float(args[5]), float(args[6]))
    camnd.roll = float(args[7])
    camnd.fov = float(args[8])

def syUpCamSI(args, ctx):
    action = ctx['action']
    camnm = MyDecode(args[0])
    camnd = FindActionErr(camnm, ctx)
    if camnd is None:
        return
    camnd.position = (float(args[1]), float(args[2]), float(args[3]))
    camnd.interest = (float(args[4]), float(args[5]), float(args[6]))
    camnd.roll = float(args[7])
    camnd.fov = float(args[8])

def syUpCamSR(args, ctx):
    action = ctx['action']
    camnm = MyDecode(args[0])
    camnd = FindActionErr(camnm, ctx)
    if camnd is None:
        return
    camnd.position = (float(args[1]), float(args[2]), float(args[3]))
    camnd.rotation = (float(args[4]), float(args[5]), float(args[6]))
    camnd.fov = float(args[7])

# Many variants on camera updates.
# UpCamF[P][A|I|R][F]: P, PA, PI, PR, PF, PAF, PIF, PRF, A, I, R, F, AF, IF, RF

def syUpCamFP(args, ctx):
    action = ctx['action']
    camnm = MyDecode(args[0])
    camnd = FindActionErr(camnm, ctx)
    if camnd is None:
        return
    camnd.position = (float(args[1]), float(args[2]), float(args[3]))

def syUpCamFPA(args, ctx):
    action = ctx['action']
    camnm = MyDecode(args[0])
    camnd = FindActionErr(camnm, ctx)
    if camnd is None:
        return
    camnd.position = (float(args[1]), float(args[2]), float(args[3]))
    camnd.aim = (float(args[4]), float(args[5]), float(args[6]))
    camnd.roll = float(args[7])

def syUpCamFPI(args, ctx):
    action = ctx['action']
    camnm = MyDecode(args[0])
    camnd = FindActionErr(camnm, ctx)
    if camnd is None:
        return
    camnd.position = (float(args[1]), float(args[2]), float(args[3]))
    camnd.interest = (float(args[4]), float(args[5]), float(args[6]))
    camnd.roll = float(args[7])

def syUpCamFPR(args, ctx):
    action = ctx['action']
    camnm = MyDecode(args[0])
    camnd = FindActionErr(camnm, ctx)
    if camnd is None:
        return
    camnd.position = (float(args[1]), float(args[2]), float(args[3]))
    camnd.rotation = (float(args[4]), float(args[5]), float(args[6]))

def syUpCamFPF(args, ctx):
    action = ctx['action']
    camnm = MyDecode(args[0])
    camnd = FindActionErr(camnm, ctx)
    if camnd is None:
        return
    camnd.position = (float(args[1]), float(args[2]), float(args[3]))
    camnd.fov = float(args[4])

def syUpCamFPAF(args, ctx):
    action = ctx['action']
    camnm = MyDecode(args[0])
    camnd = FindActionErr(camnm, ctx)
    if camnd is None:
        return
    camnd.position = (float(args[1]), float(args[2]), float(args[3]))
    camnd.aim = (float(args[4]), float(args[5]), float(args[6]))
    camnd.roll = float(args[7])
    camnd.fov = float(args[8])

def syUpCamFPIF(args, ctx):
    action = ctx['action']
    camnm = MyDecode(args[0])
    camnd = FindActionErr(camnm, ctx)
    if camnd is None:
        return
    camnd.position = (float(args[1]), float(args[2]), float(args[3]))
    camnd.interest = (float(args[4]), float(args[5]), float(args[6]))
    camnd.roll = float(args[7])
    camnd.fov = float(args[8])

def syUpCamFPRF(args, ctx):
    action = ctx['action']
    camnm = MyDecode(args[0])
    camnd = FindActionErr(camnm, ctx)
    if camnd is None:
        return
    camnd.position = (float(args[1]), float(args[2]), float(args[3]))
    camnd.rotation = (float(args[4]), float(args[5]), float(args[6]))
    camnd.fov = float(args[7])

def syUpCamFA(args, ctx):
    action = ctx['action']
    camnm = MyDecode(args[0])
    camnd = FindActionErr(camnm, ctx)
    if camnd is None:
        return
    camnd.aim = (float(args[1]), float(args[2]), float(args[3]))
    camnd.roll = float(args[4])

def syUpCamFI(args, ctx):
    action = ctx['action']
    camnm = MyDecode(args[0])
    camnd = FindActionErr(camnm, ctx)
    if camnd is None:
        return
    camnd.interest = (float(args[1]), float(args[2]), float(args[3]))
    camnd.roll = float(args[4])

def syUpCamFR(args, ctx):
    action = ctx['action']
    camnm = MyDecode(args[0])
    camnd = FindActionErr(camnm, ctx)
    if camnd is None:
        return
    camnd.rotation = (float(args[1]), float(args[2]), float(args[3]))

def syUpCamFF(args, ctx):
    action = ctx['action']
    camnm = MyDecode(args[0])
    camnd = FindActionErr(camnm, ctx)
    if camnd is None:
        return
    camnd.fov = float(args[1])

def syUpCamFAF(args, ctx):
    action = ctx['action']
    camnm = MyDecode(args[0])
    camnd = FindActionErr(camnm, ctx)
    if camnd is None:
        return
    camnd.aim = (float(args[1]), float(args[2]), float(args[3]))
    camnd.roll = float(args[4])
    camnd.fov = float(args[5])

def syUpCamFIF(args, ctx):
    action = ctx['action']
    camnm = MyDecode(args[0])
    camnd = FindActionErr(camnm, ctx)
    if camnd is None:
        return
    camnd.interest = (float(args[1]), float(args[2]), float(args[3]))
    camnd.roll = float(args[4])
    camnd.fov = float(args[5])

def syUpCamFRF(args, ctx):
    action = ctx['action']
    camnm = MyDecode(args[0])
    camnd = FindActionErr(camnm, ctx)
    if camnd is None:
        return
    camnd.rotation = (float(args[1]), float(args[2]), float(args[3]))
    camnd.fov = float(args[4])

# Moving objects

def syUpMobS(args, ctx):
    action = ctx['action']
    mobnm = MyDecode(args[0])
    mobnd = FindActionNone(mobnm, ctx)
    if mobnd is None:
        mobnd = action.create_node('Axis')
        mobnd.name = mobnm
        PlunkNewTNode(mobnd, ctx)
    mobnd.position = (float(args[1]), float(args[2]), float(args[3]))
    mobnd.rotation = (float(args[4]), float(args[5]), float(args[6]))

def syUpMobF(args, ctx):
    action = ctx['action']
    mobnm = MyDecode(args[0])
    mobnd = FindActionErr(mobnm, ctx)
    if mobnd is None:
        return
    mobnd.position = (float(args[1]), float(args[2]), float(args[3]))
    mobnd.rotation = (float(args[4]), float(args[5]), float(args[6]))

# Lights! Maintain position, type, color. Rotation doesn't need to be set,
#   they are either point sources or directional aimed at the origin.

def syUpLiteS(args, ctx):
    action = ctx['action']
    ltnm = MyDecode(args[0])
    ltnd = FindActionNone(ltnm, ctx)
    if ltnd is None:
        ltnd = action.create_node('Light')
        ltnd.name = ltnm
        PlunkNewTNode(ltnd, ctx)
    if int(args[1]) == 1:
        ltnd.light_type = 'Directional'
    else:
        ltnd.light_type = 'Point / Spot'
    ltnd.position = (float(args[2]), float(args[3]), float(args[4]))

def syUpLiteF(args, ctx):
    action = ctx['action']
    ltnm = MyDecode(args[0])
    ltnd = FindActionErr(ltnm, ctx)
    ltnd.position = (float(args[1]), float(args[2]), float(args[3]))


def sySetLiteC(args, ctx):
    action = ctx['action']
    ltnm = MyDecode(args[0])
    ltnd = FindActionErr(ltnm, ctx)
    ltnd.colour = (float(args[1]), float(args[2]), float(args[3]))

#------ Conditionals for lens distortion handling ------
# See if the lens distortion node exists, if so, set blocked.
# Else, it will continue

def syIfBatchNodeMissing(args, ctx):
    ldnm = MyDecode(args[0])
    ldnode = FindBatchNone(ldnm, ctx)
    if ldnode is not None:
        ctx['blocked'] = 1

def syIfBatchNodeExists(args, ctx):
    ldnm = MyDecode(args[0])
    ldnode = FindBatchNone(ldnm, ctx)
    if ldnode is None:
        ctx['blocked'] = 1

# The old values are in ctx['old_sticky'], the new values (to be output
#   and saved) are in ctx['new_sticky']

def sySetOverscan(args, ctx):
    reqd_overscan = float(args[0])
    sugg_overscan = float(args[1])
    if 'new_sticky' not in ctx:
        ctx['new_sticky'] = {}
    ctx['new_sticky']['reqd_overscan'] = reqd_overscan
    ctx['new_sticky']['sugg_overscan'] = sugg_overscan

def syCheckOverscan(args, ctx):
    reqd_overscan = float(args[0])
    sugg_overscan = float(args[1])
    if 'old_sticky' in ctx:
        old_overscan = ctx['old_sticky']['sugg_overscan']
    else:
        old_overscan = 0.0
    if reqd_overscan > old_overscan:
        rv = flame.messages.show_in_dialog("You MUST do this!", 
            ("To prevent your renders from being clipped, "
            + "you MUST increase the overscan setting. "
            + "With the Action node selected, click Node Prefs, "
            + "then in the Rendering section, change 'Over Scan' to "
            + "'Scale " + ('{:d}'.format(int(sugg_overscan))) + "%'. "
            + "Until Flame's Python is enhanced, we can't do this "
            + "for you, sadly."),
            'info', ['Ok'], 'Cancel')
        if rv != 'Ok':
            ctx['ok'] = 0
            return
    if 'new_sticky' not in ctx:
        ctx['new_sticky'] = {}
    ctx['new_sticky']['reqd_overscan'] = reqd_overscan
    ctx['new_sticky']['sugg_overscan'] = sugg_overscan

############### Changing camera type functions ##################
# TODO? have code move any child nodes of the old camera to the new cam?

def ChangeCamTo3D(newnm, ctx):
    rv = flame.messages.show_in_dialog("Oh, this could get messy!", 
            ("The file being imported is calling for a 3D camera, "
                + "but the scene currently uses the default camera. "
                + "We can create the 3D camera, but python limitations "
                + "prevent us from fully configuring it. "
                + "For example, you'll need to manually adjust the "
                + "position expression on '" + newnm + "Far', "
                + "and its Free/Aim-Target status. "
                + "(The Default camera will be left unchanged, "
                + "don't let it cause confusion.) "
                + "Should we proceed?"),
            'warning', ['Yes'], 'Cancel')
    if rv != 'Yes':
        ctx['ok'] = 0
        return
    ChangeParents("Default", newnm, ctx)
    action = ctx['action']
    cam = action.create_node('Camera 3D')
    cam.name = newnm
    PlunkNewTNode(cam, ctx)

def ChangeCamToDefault(oldnm, ctx):
    rv = flame.messages.show_in_dialog("Oh, this is awkward!", 
            ("The file being imported is asking to use the Default camera, "
                + "but the scene currently uses a physical 3D camera node. "
                + "We can delete the 3D camera and start working on the "
                + "Default camera, but python limitations "
                + "prevent us from fully configuring it. "
                + "For example, you'll need to manually adjust the "
                + "position expression on 'DefaultFar'. "
                + "Should we proceed?"),
            'warning', ['Yes'], 'Cancel')
    if rv != 'Yes':
        ctx['ok'] = 0
        return
    ChangeParents(oldnm, "Default", ctx)
    action = ctx['action']
    nd = FindActionNone(oldnm, ctx) # no error, likely deleted earlier
    if nd is not None:
        flame.PyNode.delete(nd)

# This isn't necessary if the update fully reparents every node each update

def ChangeParents(oldnm, newnm, ctx):
    action = ctx['action']
    oldnd = FindActionNone(oldnm, ctx) # no error, likely deleted earlier
    if oldnd is None:
        return          # error?
    newnd = FindActionNone(newnm, ctx) # no error, likely deleted earlier
    if newnd is None:
        return          # error?
    kids = oldnd.children() 
    for nd in kids:
        action.disconnect_nodes(oldnd, nd)
        action.connect_nodes(newnd, nd)

############### Manifest-related functions ##################
# ManifestDestiny updates the Flame scene to match the expectations of the
#   incoming SynthEyes scene data. This happens before anything else.
# Takes place in two stages to avoid issues with swapping names etc.

def syManifestDestiny(args, ctx):
    oldfil = AdjustFileName(MyDecode(args[0]), ctx)
    newfil = AdjustFileName(MyDecode(args[1]), ctx)
    ctx['old_manifest'] = oldfil        # save names for Wrap
    ctx['new_manifest'] = newfil
    read_manifest(oldfil, 'uid2old', 'old_sticky', ctx)
    read_manifest(newfil, 'uid2new', 'new_sticky', ctx)
    uid2old = ctx['uid2old']
    uid2new = ctx['uid2new']
    # These only have entries where needed:
    pass1 = {}       # old name to temporary uid-nodename
    pass2 = {}       # new name to temporary uid-nodename
    deletelist = {}
    # Find the total set of uid nodes under discussion
    # Note that the uids include the pattern also! ..._axis~ for example.
    uids = []
    for k,v in uid2old.items():
        if k not in uids:
            uids.append(k)
    for k,v in uid2new.items():
        if k not in uids:
            uids.append(k)
    # now examine those uids to determine their fate
    for uid in uids:
        newnm = uid2new.get(uid, None)
        oldnm = uid2old.get(uid, None)
        if newnm is None and oldnm is None:
            pass        # "I know nothing!" -- do nothing
        elif oldnm is None:        # It is a new node
            pass                   # No action is required
        elif newnm is None:        # oldnm is being deleted
            nd = FindInEither(oldnm, uid, ctx)     # no error if not found
            if nd is not None:                  # likely deleted earlier
                flame.PyNode.delete(nd)         # that's ok
        elif FindInEither(oldnm, uid, ctx) is None:
            # The UID exists in both new and old, but the actual node has
            # been deleted in Flame. It will be re-created, but we'll
            # tag it for deletion at the end.
            # TODO future: provide handling throughout to avoid re-creation?
            deletelist[uid] = newnm       # delete it; this happens at the end
        elif newnm != oldnm:        # rename in process
            if oldnm == 'Default' and newnm != 'Default':
                ChangeCamTo3D(newnm, ctx)        # don't rename!
            elif newnm == 'Default' and oldnm != 'Default':
                ChangeCamToDefault(oldnm, ctx)   # don't rename!
            else:
                pass1[uid] = oldnm      # never index on a name!
                pass2[uid] = newnm 
        else:
            pass        # the uid is being mapped to itself, no special action
    for uid,nm in pass1.items():                # change to old names to UIDs
        if uid[0] == 'B':                       # batch node uids start w/'B'
            nd = FindBatchErr(nm, ctx)
        else:
            nd = FindActionErr(nm, ctx)
        nd.name = uid
    for uid,nm in pass2.items():                # change to UIDs to new names
        if uid[0] == 'B':
            nd = FindBatchErr(uid, ctx)
        else:
            nd = FindActionErr(uid, ctx)
        nd.name = nm
    ctx['deletelist'] = deletelist         # uid-tmp-nodename to final name



def FindInEither(nm, uid, ctx):
    try:
        if uid[0] == "B":
            rv = flame.batch.get_node(nm)
        else:
            action = ctx['action']
            rv = action.get_node(nm)
    except:
        rv = None
    return rv

# Wrap-up processing --- apply the final name changes, and write the
#   new manifest back out ***as the OLD manifest***

def DeleteNodesAndWriteManifest(ctx):
    deletelist = ctx.get('deletelist', {})
    for uid,nm in deletelist.items():
        if uid[0] == 'B':
            nd = FindBatchNone(nm, ctx)
        else:
            nd = FindActionNone(nm, ctx) # no error, likely deleted earlier
        if nd is not None:
            flame.PyNode.delete(nd)         # that's ok
    write_manifest(ctx)

# For 'New' exports, there is no manifest processing, but if we've succeeded,
#   then at the end should copy the manifest file over from NEW to OLD.
    
def syReadManifest(args, ctx):
    newfil = AdjustFileName(MyDecode(args[0]), ctx)
    ctx["new_manifest"] = newfil
    read_manifest(newfil, 'uid2new', 'new_sticky', ctx)

def syWriteManifest(args, ctx):
    ctx["old_manifest"] = AdjustFileName(MyDecode(args[0]), ctx)
    write_manifest(ctx)

# Read the JSON and build up bidirectional mapping dictionaries

def read_manifest(fnm, uid2whatnm, stickynm, ctx):
    with open(fnm) as fp:
        mani = json.load(fp)
    if mani is None or 'exported' not in mani:
        ctx[uid2whatnm] = {}
        ctx[stickynm] = {}
        return
    uid2what = mani['exported']
    ctx[uid2whatnm] = uid2what
    ctx[stickynm] = (mani['sticky'] if 'sticky' in mani else {})

def write_manifest(ctx):
    mani = {}
    mani['exported'] = ctx.get('uid2new', {})
    mani['sticky'] = ctx.get('new_sticky', {})
    outfile = ctx.get('old_manifest', '')
    if outfile != '':
        with open(outfile, "w") as fp:
            json.dump(mani, fp, indent=4)       # new data... to old location!

############### Hook-related functions ##################

# An incoming PyClipNode's clip attribute can either be a 
#   PyClip or a PySequence (which is derived from PyClip)
# This is just a handy way to get to the PyClip/PySequence

def FindUnderlying(clp):
    if isinstance(clp, flame.PyClipNode):
        return clp.clip         # May be PyClip or its derived PySequence
    return None

# Find the clip in the media panels and generate a description of where it is
# https://help.autodesk.com/view/FLAME/2024/ENU/?guid=Flame_API_Python_API_Flame_Module_Attributes_and_Defines_html
# Only look in Batch groups (ie ~Comp), assuming it has been dragged into the 
# project already.  Can then be done found by name.
# No need to look at shelf_reels -- as soon as dragged into project, shifts to 
#   a schematic reel.
# No need to look in desktop.reel_groups or project.current_workspace.libraries

# Here are some problems---- 
#   We're doing this based on the clip name, which is NOT UNIQUE
#   A Clip in a BFX node can simultaneously be open in a Batch Group,
#       resulting in a misattribution.
#   The "uids" don't help much, since the same clip uid shows up in multiple
#       batch groups.
#   It doesn't help disambiguate batch groups vs timeline BFXs
#   Multiple timeline BFXs on different parts of the same clip likely
#       still show up with the same clip uid.
#   At the end of the day, it's really the batch groups that need to have
#       their shots kept separate.
#   There's no batch.name that's visible AT ALL -- it's always 'Batch';
#       the name you see in the media panel appears to be from the database.
#   You can't access ANY other batch's aside from the active one,
#       even any that are in the library.
#   From this, some unique-ifying is required for sure!

def DescribeClip(clpnode):      # PyClipNode
    clp = FindUnderlying(clpnode)
    batch = flame.batch
    desktop = batch.parent
    project = flame.project.current_project
    wspace = project.current_workspace
    libs = wspace.libraries
    vals = {}
    vals['<PROJ>'] = project.name
    nick = project.nickname
    vals['<PROJNICK>'] = (nick if nick != '' else project.name)
    vals['<WORKSPACE>'] = wspace.name.get_value()
    vals['<BATGRP>'] = batch.name.get_value()
    vals['<BATID>'] = uid_condense(batch.uid.get_value())
    vals['<BATSML>'] = uid_mini(batch.uid.get_value())
    for rl in batch.reels:      # look only in current bg, not desktop.batch_groups
        vals['<REEL>'] = rl.name.get_value()
        if rl.clips is not None:
            for cl in rl.clips:
                vals['<CLIP>'] = cl.name.get_value()
                if (cl.name.get_value() == clp.name.get_value() 
                        and cl.uid.get_value() == clp.uid.get_value()):
                    return vals     # found it, success
        if rl.sequences is not None:
            for cl in rl.sequences:         # This is a "BFX"
                vals['<CLIP>'] = cl.name.get_value()
                if (cl.name.get_value() == clp.name.get_value() 
                        and cl.uid.get_value() == clp.uid.get_value()):
                    return vals     # found it, success
    # If not found, it's a BFX
    vals['<BATGRP>'] = "BFX"+uid_mini(batch.uid.get_value())
    vals['<BATID>'] = uid_condense(batch.uid.get_value())
    vals['<BATSML>'] = uid_mini(batch.uid.get_value())
    vals['<REEL>'] = 'none'
    vals['<CLIP>'] = clp.name.get_value()
    return vals

def uid_condense(uid):
    parts = uid.split('_')
    sum = 0
    for p in parts:
        sum += int(p, 16)
    sum = (sum + (sum>>32)) & 0xffffffff
    return hex(sum).replace('-', '')[2:]

def uid_mini(uid):
    parts = uid.split('_')
    sum = 0
    for p in parts:
        sum += int(p, 16)
    sum = (sum + (sum>>32)) & 0xffffffff
    sum = (sum + (sum>>16)) & 0xffff
    return hex(sum).replace('-', '')[2:]

# Gruesome timing detail: in a Timeline BFX, the batch is/canbe shorter
#   than the clip (which always shows up as a full-length version of source).
#   The in_mark/out_marks are NULL; that is implicit in the batch's
#   start_frame and duration. We'll compute head/tail from that,
#   which will be used in SynthEyes setup to set startFrame/endFrame.
#   But in a regular Batch Group, the clip is normally full length, EXCEPT
#   if the clip has been edited anywhere else on the timeline, then the
#   batch's clip will have a shorter duration and valid in_mark/out_mark times. 
#   In both cases, the clip's start_frame stays at 1 (project start)
#   We'll use the durations to decide what's happening; we only set
#   up head/tail for the TimelineBFX and leave Batch Groups at full length.
#   Either way, the user gets the full-length shot to work on, and
#   can adjust the start/stopframe if the head/tail change later,
#   with no animation shifting.

def GetBGTiming(batch, clip):           # from a PyClip/PySequence
    bstart = batch.start_frame.get_value()
    bdura = batch.duration.get_value()
    cstart = clip.start_frame
    cdura = clip.duration.frame
    if bdura < cdura:
        head = bstart - cstart
        tail = (cdura + cstart) - (bstart + bdura)
        dura = cdura
    else:
        head = 0
        tail = 0
        dura = bdura
    return {'head': int(head), 'tail': int(tail), 
            'batch_start': int(bstart), 'batch_dura': int(bdura),
            'clip_start': int(cstart), 'clip_dura': int(cdura),
            'duration': int(dura) }

# flame.messages.show_in_dialog("tagvals", repr(vals), 'info', ['OK'], '')

# Find the clip file where the SynthEyes export will be located
# Use this clip, or one single unique Clip

def FindClip(selection):           # PyClipNode
    if len(selection) == 1 and FindUnderlying(selection[0]) is not None:
        return selection[0]         # first one, and hopefully only!
    clipcnt = 0        # if none supplied, look at all nodes for ONE clip
    notecnt = 0
    selcnt = 0
    for nd in flame.batch.nodes:
        if FindUnderlying(nd) is not None:
            if GetNoteFile(nd) != '':
                noteclip = nd
                notecnt += 1
            elif nd.selected.get_value():
                selclip = nd
                selcnt += 1
            else:
                clip = nd
                clipcnt += 1
    if selcnt == 1:
        return selclip
    elif notecnt == 1:
        return noteclip
    elif clipcnt == 1:    # none or >1 or must have note, no good
        return clip
    return None

# Given the json configuration file dictionary
# Return the new names of the json export and the clip folder

def GetExportInfo(config, clip):        # a PyClipNode
    if clip is None:
        return ('', '', '', {})
    tagvals = DescribeClip(clip)
    if tagvals is None:
        flame.messages.show_in_dialog("Send to SynthEyes", 
                "Can't find the clip in the Batch groups?",
                'Error', ['Cancel'], '')
        return ('', '', '', {})
    projects = config.get('projects', '')
    if projects == '':
        flame.messages.show_in_dialog("Send to SynthEyes", 
                "No folder has been configured in SynthEyes's "
                "'Send to SynthEyes', you must do that first.",
                'Error', ['Cancel'], '')
        return ('', '', '', {})
    projecttags = config.get('projecttags', '<PROJ>/<BATCHGRP>_<CLIP>')
    projdir = SubstTags(tagvals, projecttags)
    clips = config.get('clips', '')
    cliptags = config.get('cliptags', 'Clips')
    if clips == '':
        clips = projects + '/' + projdir
    idx = projdir.rfind("/")
    if idx >= 0:
        sniproj = projdir[idx+1:]
    else:
        sniproj = projdir      # no subfolder, only one level such as <PROJ>
    # The basename of the jsonFile etc is the final path component
    jsonFile = projects + '/' + projdir + "/" + sniproj + ".json"
    clppath = clips + '/' + SubstTags(tagvals, cliptags)
    return (sniproj, jsonFile, clppath, tagvals)

def SetClipNote(clip, jsonFile):  # PyClipNode, done after successful export
    global synNoteTag
    cnote = ''
    if clip.note is not None:
        cnote = clip.note.get_value()
    lines = cnote.splitlines(True)
    cnote = ''
    for ln in lines:
        if synNoteTag not in ln:
            cnote += ln
    clip.note = cnote + synNoteTag + jsonFile + '\n'
    clip.note_collapsed = True

def GetNoteFile(clip):      # PyClipNode, returns the JSONfile of the export
    global synNoteTag
    note = clip.note
    if note is None:
        return ''
    note = note.get_value()
    idx = note.find(synNoteTag)
    if idx == -1:
        return ''
    fnm = note[idx + len(synNoteTag):]
    idx = fnm.find("\n")
    if idx >= 0:
        fnm = fnm[0:idx]
    if fnm[-1] == '\r':
        fnm = fnm[0:-1]
    return fnm

# Make the tag substitutions

def SubstTags(tagvals, path):
    for k,v in tagvals.items():
        path = path.replace(k, v)
    return path

def TrueBase(fnm):
    base = os.path.basename(fnm)
    base = os.path.splitext(base)[0]    # true basename here
    return base

######

def write_syntheyes_sequence(sniproj, prj, clip, clipdir, config, sinfo, tagvals):
    flame.messages.show_in_console("Writing sequence to "+clipdir, duration=15)
    os.makedirs(clipdir, mode=0o755, exist_ok=True) # 0o755 is correct octal!
    exporter = flame.PyExporter()
    exporter.foreground = True
    flame_user_pref_folder = config.get('flame_user_pref_folder', '')
    if flame_user_pref_folder == '':
        flame.messages.show_in_console("No user pref folder", duration=15)
    preset_file = flame_user_pref_folder + "/export_preset.xml"
    eff_preset_file = flame_user_pref_folder + "/export_preset_eff.xml"
    with open(preset_file, 'r') as file:    # replace tag with project start
        prdata = file.read()
    startFrame = sinfo['startFrame']
    prdata = prdata.replace("STARTFRAME_TAG", str(startFrame))
    with open(eff_preset_file, 'w') as file:    # replace tag with project start
        file.write(prdata)
    try:
        exporter.export(clip, eff_preset_file, clipdir)
    except:
        return 0
    return 1


def write_shot_information(sniproj, prj, clipname, clip, clipdir, config, tagvals):
    flame.messages.show_in_console("Writing shot information for "+sniproj, duration=3)
    clipfnm = clipname
    timing = GetBGTiming(flame.batch, clip)     # PyClip
    framePadding = config.get('framePadding', 'none')
    # In a Timeline BFX, the batch's start_frame is offset to the "in" point
    # The clip's start_frame seems to stay fixed in all cases.
    startFrame = clip.start_frame
    xtn = config.get('fileExtension', '???')
    if framePadding != 'none':
        fmt = ".{0:0" + str(framePadding) + "d}"
        clipfnm += fmt.format(startFrame)
    clipfnm += "." + xtn
    # We keep the project filenames relative so that the json file can
    # be moved to a different machine and opened there without issue.
    clipFile = clipdir + "/" + clipfnm
    if clipFile[0:len(prj)] == prj:             # convert to relative?
        clipFile = clipFile[len(prj)+1:]        # skip the separating slash
    exportType = 'Flame 2025+'
    exportFile = sniproj + ".syflame"
    sniFile = sniproj + ".sni"
    infoBase = sniproj + ".json"
    infoFile = prj + "/" + infoBase
    # Most of these are not used but are included for completeness and info.
    sinfo = {
        'bitdepth': int(clip.bit_depth),
        'clipFile': clipFile,
        'clipName': clipname,
        'frameCount': int(clip.duration.frame),     # duration is a PyTime
        'exportFile': exportFile,
        'exportType': exportType,
        'frame_rate': float(clip.frame_rate.split(' ',1)[0]),
        'height': int(clip.height),
        'infoFile': infoBase,               # only relative name here
        'syntheyesProjectName': sniproj,
        'flameProjectName': flame.project.current_project.name,
        'projectDir': prj,
        'image_aspect': float(clip.ratio),
        'sniFile': sniFile,
        'startFrame': startFrame,
        'width': int(clip.width),
        'Timing': timing,   # for bfx
    }
    flame.messages.show_in_console("Wrote json information to "+infoFile, duration=15)
    with open(infoFile, "w") as fp:
        json.dump(sinfo, fp, indent=4)
    return sinfo

def start_syntheyes(sniproj, prj, config, sinfo):
    global syntheyes_process
    app = config.get('syntheyes', '')
    infoFile = prj + "/" + sniproj + ".json"
    if platform.system() == 'Darwin':
        base = TrueBase(app)     # true basename here
        app += '/Contents/MacOS/' + base
    # See version in reopen_syntheyes also.
    cmd = '"' + app + '" -run "Flame Initial Startup" "--json:' + infoFile + '"'
    args = [app, "-run", "Flame Initial Startup", "--json:"+infoFile]
    print(cmd)
    if False:
        syntheyes_process = flame.execute_command(cmd, blocking=False, shell=False)
    else:
        syntheyes_process = subprocess.Popen(args) 
    flame.messages.show_in_console("Started SynthEyes with " + cmd, duration=15)


def reopen_syntheyes(selection):
    global synflame_config_filename, syntheyes_process

    try:
        if not FlameVersionOK():
            return
        with open(synflame_config_filename) as fp:   # TODO: check
            config = json.load(fp)
        app = config.get('syntheyes', '')
        clip = FindClip(selection)
        if clip is not None:
            (sniproj, infoFile, clppath, tagvals) = GetExportInfo(config, clip)
        else:
            infoFile = ''
        if infoFile == '' or not os.path.isfile(infoFile):
            flame.messages.show_in_dialog("Reopen SynthEyes", 
                "This doesn't seem to have been exported to SynthEyes, "
                "aborting.!",
                'error', ['Cancel'], '')
            return
        prj = os.path.dirname(infoFile)
        sniproj = TrueBase(infoFile)
        sniFile = prj + "/" + sniproj + ".sni"
        if platform.system() == 'Darwin':
            base = TrueBase(app)    # true basename here, no .app
            app += '/Contents/MacOS/' + base
        exists = os.path.isfile(sniFile)
        if not exists:
            cmd = '"' + app + '" -run "Flame Initial Startup" "--json:' + infoFile + '"'
            args = [app, "-run", "Flame Initial Startup", "--json:"+infoFile]
        else:
            cmd = '"' + app + '" "' + sniFile + '"'
            args = [app, sniFile]
        print(cmd)
        if False:
            syntheyes_process = flame.execute_command(cmd, blocking=False, shell=False)
        else:
            syntheyes_process = subprocess.Popen(args) 
        flame.messages.show_in_console("Starting: " + cmd, duration=15)
        if platform.system() == 'Darwin':
            flame.messages.show_in_dialog("SynthEyes startup", 
                "The track has been re-opened in SynthEyes; "
                "use command-H(mac) as needed "
                + "to hide Flame in order to see SynthEyes.",
                'info', ['Ok'], '')
        # flame.execute_shortcut("Minimize Application") - DNW
    except:
        flame.messages.show_in_dialog("Error!", 
                (SyLine() + "Error: " + repr(sys.exception())  
                    + '\n' + traceback.format_exc()),
                'error', ['Ok'], '')

def send_to_syntheyes(selection):
    global synflame_config_filename

    try:
        if not FlameVersionOK():
            return
        with open(synflame_config_filename) as fp:
            config = json.load(fp)
        prjct = config.get('projects', "")   # extra check only
        if prjct == '':
            flame.messages.show_in_dialog("Error!", 
                    "The SynthEyes script 'Flame/Integrate with Flame' "
                    + "must be run first.",
                    'error', ['Cancel'], '')
            return

        clip = FindClip(selection)
        if clip is None:
            flame.messages.show_in_dialog("Error!", 
                ("Exactly one Clip can be exported to SynthEyes, "+
                    "not Read Files or other nodes; none found. Aborting."),
                'error', ['Cancel'], '')
            return
        (sniproj, jsonFile, clippath, tagvals) = GetExportInfo(config, clip)
        if os.path.isfile(jsonFile):
            prj = os.path.dirname(jsonFile)
            rv = flame.messages.show_in_dialog("Attention Please!", 
                    ("We note that you've previously sent this project "
                    + "to SynthEyes. "
                    + "Erase that version so you can start over?"),
                    'warning', ['Yes'], 'Cancel')
            if rv != 'Yes':
                flame.messages.show_in_console("Send cancelled by user", duration=15)
                return
            try:
                shutil.rmtree(prj)
            except:
                flame.messages.show_in_dialog("Error!", 
                        ("Couldn't delete all the files in "
                            + prj + ". Some may be open in other applications "
                            + "including SynthEyes or Flame. "
                            + "Fix then please try again."),
                    'error', ['Cancel'], '')
                return

        prj = os.path.dirname(jsonFile)
        os.makedirs(prj, mode=0o755, exist_ok=True) # 0o755 is correct octal!
        sniproj = TrueBase(jsonFile)

        clipname = clip.name.get_value()       # string not R/W attribute!
        if clipname == '':
                flame.messages.show_in_dialog("Error!", 
                        ("The clip doesn't have a name! "
                            + "It must have a name so that we can find it. "
                            + "Please give it one, then try again."),
                    'error', ['Cancel'], '')
                return
        bare_clip = FindUnderlying(clip)       # to underlying PyClip
        sinfo = write_shot_information(sniproj, prj, clipname, bare_clip, clippath, config, tagvals)
        if not write_syntheyes_sequence(sniproj, prj, bare_clip, clippath, config, sinfo, tagvals):
            return
        SetClipNote(clip, jsonFile)
        start_syntheyes(sniproj, prj, config, sinfo)
        flame.execute_shortcut("Minimize Application")
    except:
        flame.messages.show_in_dialog("Error!", 
                (SyLine() + "Error: " + repr(sys.exception())  
                    + '\n' + traceback.format_exc()),
                'error', ['Ok'], '')

def receive_from_syntheyes(selection):
    global synflame_config_filename, synfile_fromlist, synfile_tolist

    try:
        if not FlameVersionOK():
            return
        with open(synflame_config_filename) as fp:   # TODO: check
            config = json.load(fp)
        clip = FindClip(selection)
        if clip is not None:
            (sniproj, jsonFile, clippath, tagvals) = GetExportInfo(config, clip)
        else:
            jsonFile = ''
        if jsonFile != '':
            prjdir = os.path.dirname(jsonFile)
            sniproj = TrueBase(jsonFile)
            fnm = prjdir + "/" + sniproj + ".syflame"
        else:
            fnm = ''
        if fnm == '' or not os.path.isfile(fnm):
            rv = flame.messages.show_in_dialog("Oops!", 
                ("If there are more than one SynthEyes clips in the "
                + "shot, select the one you want to Receive, "
                + "then right-click INSIDE THE NODE. "
                + "Otherwise, maybe you haven't yet exported this project "
                + "from SynthEyes " 
                + "(with 'File/Export/Flame/Flame 2025+'). "
                + "Or, did you delete the clip's note with the filename? "),
                    'error', ['Yes'], 'Cancel')
            if rv == 'Yes':
                fnm = RecoverFilename(config, clip)
                if fnm == '':
                    flame.messages.show_in_dialog("Oops!", 
                            "Select the main exported clip and try again; "
                            "otherwise this probably wasn't exported at all.",
                            'error', ['Cancel'], '')
                    return
            else:
                return
        flame.messages.show_in_console("about to read "+fnm, duration=15)
        ctx = read_syntheyes_export(fnm)
    except:
        flame.messages.show_in_dialog("Error!", 
                (SyLine() + "Error: " + repr(sys.exception()) 
                    + '\n' + traceback.format_exc()),
                'error', ['Ok'], '')

def RecoverFilename(config, clip):
    (sniproj, jsonFile, clppath, tagvals) = GetExportInfo(config, clip)
    if jsonFile == '':
        return ''
    SetClipNote(clip, jsonFile)
    prjdir = os.path.dirname(jsonFile)
    sniproj = TrueBase(jsonFile)
    fnm = prjdir + "/" + sniproj + ".syflame"
    if os.path.isfile(fnm):
        return fnm
    return ''

def FlameVersionOK():
    try:
        major = int(flame.get_version_major())
        minor = int(flame.get_version_minor())
        patch = int(flame.get_version_patch())
    except:
        major = 0
        minor = 0
        patch = 0
    if (major > 2025 or major == 2025 and minor > 0 
            or major == 2025 and minor == 0 and patch >= 1):
        return True
    flame.messages.show_in_dialog("Sorry!", 
                ("SynthEyes/Flame integration requires Flame 2025.0.1 or later. "
                "You can use the 'Flame/Autodesk Action/DVE (Older)' "
                "exporter instead, though it's much simpler."),
                'error', ['Cancel'], '')
    return False

def get_batch_custom_ui_actions():
    return [
        {
            #"name" : "BorisFX SynthEyes",
            "actions" : [
                {
                    "name": "Receive from SynthEyes",
                    "isVisible" : True,        # also isEnabled
                    "execute": receive_from_syntheyes,
                    "order": 1
                },
                {
                    "name": "Send to SynthEyes",
                    "isVisible" : True,        # also isEnabled
                    "execute": send_to_syntheyes,
                    "order": 2
                },
                {
                    "name": "Reopen in SynthEyes",
                    "isVisible" : True,        # also isEnabled
                    "execute": reopen_syntheyes,
                    "order": 3
                },
            ]
        }
    ]


def get_action_custom_ui_actions():
    return [
        {
            #"name" : "BorisFX SynthEyes",
            "actions" : [
                {
                    "name": "Receive from SynthEyes",
                    "isVisible" : True,        # also isEnabled
                    "execute": receive_from_syntheyes,
                    "order": 1
                },
                {
                    "name": "Reopen in SynthEyes",
                    "isVisible" : True,        # also isEnabled
                    "execute": reopen_syntheyes,
                    "order": 2
                }
            ]
        }
    ]

# This enables the copy of the script placed in the project's folder
#   to automatically read the exported syflame file, when run from
#   the python console:

if 'syflame_filename' in globals():
    try:
        if FlameVersionOK():
            if not os.path.isfile(syflame_filename):
                base = os.path.basename(syflame_filename)
                flame.browser.show(
                        os.getcwd(),    # initial path
                        title="Please locate the "+base+ " file",
                        extension="syflame", 
                        select_directory=False, 
                        multi_selection=False, 
                        include_resolution=False)
                fnms = flame.browser.selection
                if len(fnms) == 1:  # 0, assume cancelled. Shouldn't be >1!
                    syflame_filename = fnms[0]
                    read_syntheyes_export(syflame_filename)
            else:
                read_syntheyes_export(syflame_filename)
    except:
        flame.messages.show_in_dialog("Error!", 
                (SyLine() + "Error: " + repr(sys.exception())
                    + '\n' + traceback.format_exc()),
                'error', ['Ok'], '')

# 'Send to SynthEyes' testing --- uncomment the next line of code, then run
#   this script in the python console:
#send_to_syntheyes([])     # <<<--- uncomment this line.


