from .GlobalMap import GlobalMap
from termcolor import colored
from datetime import date

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
RE_APPEND 		= "=="
RE_ASSIGN		= "="

D_CMDS   = ( REMOVE, CREATE, COPY, CUT, RE_ASSIGN, RE_APPEND, FIND, MAP )
S_CMDS_A = ( LIST_CONTENTS, )
S_CMDS_B = ( INPUT, CHDIR )

BASE_DIR = '.'
BADGE 	 = colored( f"{date.today()}@FSHELL" , "green")

GLOBAL_MAP = GlobalMap();