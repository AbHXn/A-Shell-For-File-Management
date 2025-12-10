from .GlobalMap import GlobalMap

REMOVE      	= '-'
CREATE      	= '+'
COPY        	= '+='
CUT         	= '-='
CHDIR       	= '*'
INPUT       	= '#'
LIST_OPEN   	= '['
LIST_CLOSE  	= ']'
LIST_CONTENTS 	= '!'
APPO			= '"'
FIND			= '@'
MAP				= '->'
MAP_PATH		= '&'

# didn't implemented
RE_APPEND 		= "=="
RE_ASSIGN		= "="

D_CMDS   = ( REMOVE, CREATE, COPY, CUT, RE_ASSIGN, RE_APPEND, FIND, MAP )
S_CMDS_A = ( LIST_CONTENTS, )
S_CMDS_B = ( INPUT, CHDIR , MAP_PATH )

BASE_DIR = '.'

GLOBAL_MAP = GlobalMap();