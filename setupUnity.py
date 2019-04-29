import maya.cmds as cmds

def main():
    cmds.currentUnit( l='m' )
    cmds.currentUnit( t='ntsc' )
    cmds.upAxis( ax='y' )
    cmds.grid( reset=True )
    cmds.grid( s=5,d= 4,sp=1 , dab = True,ddl = True, dpl = True)
    
main()