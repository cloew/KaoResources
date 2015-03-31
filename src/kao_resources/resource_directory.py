import os

class ResourceDirectory:
    """ Represents a directory that contains resources """
    
    def __init__(self, root):
        """ Initialize the Resource Directory with its root filepath """
        self.root_dir = self.getRootDirectory(root)
        
    def getRootDirectory(self, root):
        """ Return the proper root directory """
        if not os.path.isdir(root):
            root = os.path.dirname(root)
        return root
        
    def getProperPath(self, filename):
        """ Return the actual path to the resource file given """
        return os.path.join(self.root_dir, filename)
        