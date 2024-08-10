import os

path1 = '/path/to/directory'
path2 = '/path/to/other/directory'

if os.path.commonprefix([path1, path2]) == path1:
    print('path1 is contained in path2')
elif os.path.commonprefix([path1, path2]) == path2:
    print('path2 is contained in path1')
else:
    print('Neither path1 nor path2 is contained in the other')
