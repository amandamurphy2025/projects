
"""
CMSC 14100 Project Aut 22
"""

from library import Library, LibraryException
from version import Version

def make_tuple(version):
    """
    takes a version of the form "#.#.#" which can have any amount of integers
    up to 3, and can have trailing periods.  Turns this into a tuple of the
    form (#, #, #).
    
    Input:
        version (str): version number as a string
    Output:
        tuple: tuple with the integers of the version as values
    """
    
    v = version.split(".")

    for idx, val in enumerate(v):
        if v[idx] != "":
            v[idx] = int(val)
        elif v[idx] == "":
            v.remove(v[idx])

    v = tuple(v)

    return v

class LibraryHub:

    """
    A class for a registry managing libraries.
    """
    def __init__(self):
        """
        Create a new LibraryHub instance.
        """
        self.hub = {}
        


    def register_new_library(self,
                             name,  # Name of the library
                             version,  # Version number
                             is_testing = False,  # Is not ready to be used.
                             ):
        """
        Creates a new Library and registers it with the LibraryHub for later
        lookup/use. Should raise a LibraryException is the Library version is 
        not exact (e.g. could match to more than one version stored) OR if the 
        exact Library already exists.

        Inputs:  
            name (str): The library name. Case sensitive  
            version(str): The exact library version number  
            is_testing(bool): If the library is not ready for use  

        Returns(Library): The newly created Library object
        """

        v = version.split(".")

        for idx, val in enumerate(v):
            if v[idx] != "":
                v[idx] = int(val)
            elif v[idx] == "":
                v.remove(v[idx])

        if len(v) < 3:
            raise LibraryException("Exception")

        Lib = Library(name, version, is_testing)

        if name in self.hub:
            for library in self.hub[name]:
                if Lib.compare_version(library) == 0:
                    raise LibraryException("Exception")

        if name in self.hub:
            self.hub[name].append(Lib)
        else:
            self.hub[name] = []
            self.hub[name].append(Lib)

        return Lib




    def find_latest_version(self, name, include_testing = False):
        """
        Find the latest version of a library name.  Should raise a
        LibraryException is the Library name cannot be found

        Inputs:  
            name(str): The name of the library  
            include_testing(bool): Consider testing libraries  

        Returns (Library): The largest version for a library name
        """
        
        if not name in self.hub:
            raise LibraryException("Exception")
 
        lst = self.hub[name]

        if include_testing == False:
            for library in lst:
                if not library.is_testing == False:
                    lst.remove(library)
                if len(lst) == 0:
                    return None
 
        latest_version = lst[0]

        for library in lst:
            if library.compare_version(latest_version) == 1:
                latest_version = library
 
        return latest_version

    def get_library(self, name, version_requirement):
        """
        Find a registered Library object by the name and version.
        If more than one registered version satisfies the version requirement,
        return the Library with the highest version number that satisfies the
        requirement and is not in testing.
        If only one registered version satisfies the requirment, return the
        library regardless if in testing or not. If version_requirement is
        exact, then only an exact match should be found.

        Inputs:  
          name (str): The library name to match. Case sensitive  
          version_requirement(str): The library version requirement  

        Returns (Library | None): The Library that satisfies the
        version_requirement. If more than one are registered, then the
        largest/highest one that is not testing should be returned.
        None is returned if no valid library can be found.
        """

        v = version_requirement.split(".")

        for idx, val in enumerate(v):
            if v[idx] != "":
                v[idx] = int(val)
            elif v[idx] == "":
                v.remove(v[idx])

        v = tuple(v)
        
        if name in self.hub:
            lst = self.hub[name]
        else:
            return None

        matches = LibraryHub()

        matches.hub[name] = []

        match = []

        for library in lst:
            if library.meets_version_req(version_requirement) == True:
                matches.hub[name].append(library)
                match.append(library)

        if len(matches.hub[name]) == 1:
            if len(v) == 3:
                for library in match:
                    if len(make_tuple(library.version.v)) == 3:
                        return match[0]
                    else:
                        return None
            else:
                return match[0]

        if len(match) == 0:
            return None

        istesting = []

        if len(matches.hub[name]) > 1:
            for library in match:
                if library.is_testing == True:
                    istesting.append(library)
            if len(istesting) == len(match):
                return None
            else:
                return matches.find_latest_version(name, False)