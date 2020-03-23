from clear_shell_automatically import *
list = ['shark', 'cuttlefish', 'squid', 'mantis shrimp', 'anemone']
list.append('monkey')
list.insert(0,'hippo')
list.extend(['cat','dog'])

print(list.index('squid'))
print(list)
list_no = [12,4,145,14,1]
print(list_no)
sorted(list_no)
print(list_no)
# help(list.append)
# help(os)
# help(sys)
# dir(sys)
## Example pulls filenames from a dir, prints their relative and absolute paths
def printdir(dir):
  filenames = os.listdir(dir)
  for filename in filenames:
    print(filename)  ## foo.txt
    print(os.path.join(dir, filename)) ## dir/foo.txt (relative to current dir)
    print(os.path.abspath(os.path.join(dir, filename))) ## /home/nick/dir/foo.txt

# printdir(r"C:\Users\Lilti\Documents\Python\Python_ATOM\Django\Python_core_code\ch2\list.py")
