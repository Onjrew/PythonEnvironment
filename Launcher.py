# This is the launcher script. I'm using XCode
# to edit the .py files, and so each script that
# gets run is supposed to be added to the project.
# I'm using this to import whichever script I'm
# currently working on. This way I only need to
# add this file to the project path.

# To run a script, simply replace the file name
# in the import statement, and ensure the
# imported script's main() function does all
# required calling.

import HelloWorld2 as script

if __name__ == '__main__':

    script.main()