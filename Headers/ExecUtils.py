from termcolor import cprint, colored
import time
import shutil
import os

class ExecUtils:
	DANGEROUS_PATHS = {
		"/", "/boot", "/usr", "/lib", "/lib64", "/etc", "/root",
        "C:\\", "C:\\Windows", "C:\\Program Files", "C:\\Program Files (x86)", "C:\\Users\\Administrator"
	}
	
	@staticmethod
	def is_dangerous(path):
		path = os.path.abspath(path)
		
		for dangerous in ExecUtils.DANGEROUS_PATHS:
			dangerous = os.path.abspath(dangerous)
			
			if path == dangerous or path.startswith(dangerous + os.sep):
				return True
		
		return False

	@staticmethod
	def print_dir_structure( dir_path, Msg ):	
		if not isinstance( dir_path, str ):
			raise TypeError( "Invalid Directory Argument" )
		
		try:
			dir_path = dir_path.strip()

			if not dir_path: 
				return 

			for dirs, _, files in os.walk( dir_path ):
				for file in files:					
					full_path = os.path.join( dirs, file )
					cprint( f"{Msg}: {full_path}" , "green")

		except Exception as _: 
			pass


	@staticmethod
	def create_file( base, name ):
		if not isinstance( base, str ) or not isinstance( name, str ):
			raise TypeError( "File path should be a string" )

		try:
			base, name = base.strip(), name.strip()
			path = os.path.join( base, name )

			if not path: return 

			if name.endswith( os.sep ):
				os.makedirs( path, exist_ok=True )
				cprint(f"{name} Folder created", "green")
			else:
				os.makedirs( base, exist_ok=True )
				if not os.path.exists( path ):
					with open(path, "w") as file:
						pass
					cprint(f"{path} File created", "green")
				else:
					raise FileExistsError( "File already exists" )

		except Exception as e:
			cprint( f"File Creation Failed: {e}", "red" )

	@staticmethod
	def remove_file( path ):
		try:
			path = path.strip()	
			
			if not path: return 		

			if ExecUtils.is_dangerous(path):
				cprint(f"Operation blocked! '{path}' is a dangerous system path.", "red")
				return

			if os.path.isdir( path ):
				ExecUtils.print_dir_structure( path, "Remove" )

				ch = input("Are you sure to Remove These files? (Y/N): ")
				if not ch.lower() in ('y', 'yes'):
					return

				if not path.endswith( os.sep ):
					shutil.rmtree( path )
				else:
					for file in os.scandir( path ):
						if file.is_dir():
							shutil.rmtree( file )
						else: os.remove( file )
				
				cprint("DONE!", "green")

			elif os.path.exists( path ):
				cprint( f"Removing File: {path}", "green" )
				time.sleep( 0.2 )
				os.remove( path )

			else: 
				FileNotFoundError( "Failed to remove file" )

		except Exception as e:
			cprint( f"File Remove Error: {e}", "red" )

	@staticmethod
	def copy_file(src, dst):
		if not isinstance(src, str) or not isinstance(dst, str):
			raise TypeError("File path should be a string")
		try:
			src, dst = src.strip(), dst.strip()

			if not src or not dst:
				return

			if not os.path.exists(src):
				raise FileNotFoundError(src)	

			if ExecUtils.is_dangerous(src) or ExecUtils.is_dangerous(dst):
				cprint(f"Operation blocked! '{src}' or '{dst}' is a dangerous system path.", "red")
				return

			os.makedirs(dst, exist_ok=True)

			if os.path.isfile(src):
				shutil.copy2(src, os.path.join(dst, os.path.basename(src)))
				return

			if src.endswith(os.sep):
				for item in os.listdir(src):
					sr = os.path.join(src, item)
					dt = os.path.join(dst, item)
					if os.path.isdir(sr):
						shutil.copytree(sr, dt, dirs_exist_ok=True)
					else:
						shutil.copy2(sr, dt)
				cprint("Files Copied", "green")
			else:
				shutil.copytree(
					src,
					os.path.join(dst, os.path.basename(src)),
					dirs_exist_ok=True
				)
				cprint("Folder Copied", "green")

		except Exception as e:
			cprint(f"File Copy Error: {str(e)}", "red")


	@staticmethod
	def move_file( src, dst ):
		if not isinstance( src, str ) or not isinstance( dst, str ):
			raise TypeError( "File path should be a string" )

		try:
			src, dst = src.strip(), dst.strip()
			if src == '' or dst == '':
				return

			if ExecUtils.is_dangerous(src) and ExecUtils.is_dangerous(dst):
				cprint(f"Operation blocked! '{src}' or '{dst}' is a dangerous system path.", "red")
				return

			if os.path.exists( src ) and os.path.exists( dst ):
				ExecUtils.print_dir_structure( src, "Move" )

				ch = input("Continue to Move(Y/N): ")
				if not ch.lower() in ('y', 'yes'):
					return

				if os.path.isdir( src ) and src.endswith( os.sep ):
					for item in os.listdir(src):
						s = os.path.join(src, item)
						d = os.path.join(dst, item)
						shutil.move(s, d)
				else: shutil.move( src, dst )
				cprint("File Moved", "green")
			else: 
				os.rename(src, dst)
				cprint("Renamed", "green")

		except Exception as e:
			cprint( f"File Move Error: {e}" , "red")

	@staticmethod
	def list_contents( folders, BASE_DIR ):
		if not isinstance( folders, list ):
			folders = [ ( BASE_DIR, folders ) ]
		try:
			for parent, child in folders:
				folder = os.path.join( parent, child ) 

				if os.path.exists( folder ) and os.path.isfile( folder ):
					with open( folder, "r", encoding="utf-8" ) as txt_file:
						print( txt_file.read() )
					return

				with os.scandir( folder ) as d_files:
					for file in d_files:
						name = file.name
						name = colored(name, 'blue') if file.is_dir() else name
						print(f"{name}", end="  ")
					print()

		except Exception as e:
			cprint( f"Listing Error: {e}", "red" )

	@staticmethod
	def input_file( file_name ):
		if not isinstance( file_name, str ):
			raise TypeError( "Filname should be a str" )

		print(f"Enter text for {file_name} (Ctrl+C to save):")
		try:
			with open(file_name, "w", encoding='utf-8') as w_file:
				while True:
					line = input()
					w_file.write(line + '\n')
			cprint("File saved", "green")
		except KeyboardInterrupt:
			cprint( "File Saved", "green" )
	
	@staticmethod
	def list_files_given( folders, files ):
		if not isinstance( folders, list ):
			folders = [ folders ]
		try:
			files_script = False
			if isinstance( files, str ):
				files = [ files ]

			for folder in folders:
				cprint(f"{folder}: ", "blue")
				with os.scandir( folder ) as d_files:
					for file in d_files:
						
						if not any( sfile in file.name for sfile in files ):
							continue

						name = file.name + '/' if file.is_dir() else file.name
						name = colored(name, 'red') 
						print(f"{name}", end="  ")
					print()

		except Exception as e:
			cprint( f"Listing Error: {e}", "red" )

	@staticmethod
	def file_optr( fromFile, toFile, off='w' ):
		try:
			if os.path.exists( fromFile ) and not os.path.isdir( fromFile ):
				with open( fromFile, "r" ) as from_file:
					with open( toFile, off ) as to_file:
						to_file.write( from_file.read() )
				return;
			else: 
				raise TypeError( "Invalid Args for Redirection" )
		except Exception as e:
			cprint( f"Redirection Error: {e}", "red" )
