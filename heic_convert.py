import os
import subprocess
basedir = './'
#cmd = "ls"
#cmd = 'heif-info'
cmd = 'heif-convert'
ext_convert = '.jpg'

def main():
    root, dirs, files = next(os.walk(basedir))
#    print (root)
#    print (dirs)
#    print (files)
    for file in files:
        filename = os.path.splitext(file)
        if filename[1] == '.heic':
            shellexec = []
            shellexec.append(cmd)
            shellexec.append(file)
            shellexec.append(filename[0] + ext_convert)
#            shellexec.append('-al')
            print (shellexec)
            subprocess.call(shellexec)
#            print (filename)

#Driver Code
if __name__ == '__main__':
    main()
