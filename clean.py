import os

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
clean_folder = 'saker'

def clean(from_dir, spec_dir):
    for file in os.listdir(from_dir):
        if not '.lnk' in file and file != clean_folder:
            try:
                os.rename(from_dir + '\\' + file, spec_dir + '\\' + file)
            except:
                pass

def fu_clean():
    curr_dir = os.getcwd()
    os.chdir(desktop)
    clean(desktop, desktop + '\\' + clean_folder)
    os.chdir(curr_dir)

if not clean_folder in os.listdir(desktop):
    os.mkdir(desktop + '\\' + clean_folder)

fu_clean()
