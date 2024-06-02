
"""
CMSC 14100 Project Aut 22
"""
from version import Version


class LibraryException(Exception):
    """
    A simple exception for described error conditions. You should not
    modify this Class at all.
    """
    pass


class Library:
    """
    A class to represent a published library. This will have:  
        - A name  
        - An exact version (major, minor, and patch)  
        - is_testing flag/attribute which indicates this library is "not ready"
    """
    def __init__(self,
                 name,  # Name of the library
                 version,  # Version number
                 is_testing = False,  # Library is in testing
                 ):
        """
        Create a new library. Raise a LibraryException if the version is not 
        exact.

        Inputs:  
            name(str): The name of the library  
            version(str): The semantic version number  
            is_testing(bool): If the library is for testing only  
        """

        v = version.split(".")

        for idx, val in enumerate(v):
            if v[idx] != "":
                v[idx] = int(val)
            elif v[idx] == "":
                v.remove(v[idx])

        if len(v) < 3:
            raise LibraryException("Exception")

        while len(v) < 3:
            v.append(-1)

        v = tuple(v)

        self.name = name

        self.is_testing = is_testing

        self.version = Version(version)

        Version.__init__(self, version)

  
    def compare_version(self, other):
        """
        Check if this version is smaller, the same, or greater than the
        other version. Throws a Library Exception if the names are not the same.

        Inputs:  
            other (Library): a Library to compare against

        Returns (int):  
          -1 if self is smaller than other,  
          0 if they have the same version number,  
          1 if self is larger than other
        """
        assert isinstance(other, Library)

        if self.name != other.name:
            raise LibraryException("Exception")

        return self.version.compare_version(other.version)   
   
    def meets_version_req(self, version_needed):
        """
        Checks if this Library meets the version number requirement.

        Inputs:  
            version_number(str): The required version as a string  

        Returns (bool): If the library meets the requirement
        """
        assert isinstance(version_needed, str)

        v = Version(version_needed)

        return self.version.meets_requirement(v)