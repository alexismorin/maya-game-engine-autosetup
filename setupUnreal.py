import maya.cmds as cmds

def main():
    cmds.currentUnit( l='cm' )
    cmds.currentUnit( t='ntsc' )
    cmds.upAxis( ax='z' )
    cmds.grid( reset=True )
    cmds.grid( s=500,d= 4,sp=100 , dab = True,ddl = True, dpl = True)
    
main()