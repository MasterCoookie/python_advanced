'''Os module'''
import os

#changing dir
os.chdir('D:/XAMPP/htdocs/Python/Advanced/os')

#getting current dir
print(os.getcwd())

#listing all files
print(os.listdir())

#making directories and subdirectories
os.mkdir('SingleDir')
os.makedirs('Dir/SubDir')
#only makedirs is capable of making subdirectories

#deleting directories and subdirectories, same deal as with creating them
os.rmdir('SingleDir')
os.removedirs('Dir/SubDir')

#exist_ok stops an error from occuring if trying to create already existing dir
os.makedirs('notrenamed', exist_ok=True)

#renaming, works with both folders and files
os.rename('notrenamed', 'renamed')
os.rmdir('renamed')

#accesing file info
print(os.stat('test.txt'))

#os.walk() method allows to acces the full tree in given direcory
#returns 3 tuples of lists
for dirpath, dirnames, filenames in os.walk('D:/XAMPP/htdocs/Python/advanced/os'):
    print('Directory: ', dirpath)
    print('Folders: ', dirnames)
    print('Files: ', filenames, '\n')

#accesing envronment varialbes
print(os.environ.get('NUMBER_OF_PROCESSORS'))
