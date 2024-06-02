
"""
CMSC 14100 Project Aut 22
"""
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
                 dependencies = None):
        """
        Create a new library. Raise a LibraryException if the version is not 
        exact.

        Inputs:  
            name(str): The name of the library  
            version(str): The semantic version number  
            is_testing(bool): If the library is for testing only  
        """


        self.name = name

        self.is_testing = is_testing

        if dependencies != None:
            for libr in dependencies:
                if len(make_tuple(libr.version.v)) != 3:
                    raise LibraryException("Exception")
                if libr.is_testing == True:
                    raise LibraryException("Exception")

        names = []
        if dependencies != None:

            for lib in dependencies:
                names.append(lib.name)

        
        n = list(set(names))

        if len(n) < len(names):
            raise LibraryException("Exception")



        self.dependencies = dependencies

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

    def equals(self, lib):


        if self.name == lib.name and self.version == lib.version:
            return True

    def check_cycle(self, lib):

        if self.name == lib.name:
            raise LibraryException("Exception")

        deps = lib.dependencies

        if deps != None:
            for libr in deps:
                if self.equals(libr) == True:

                    return False
                    
        if deps == None:

            return True
        else:
            for libr in deps:
                if self.check_cycle(libr):
                    return True
            return False

    def add_dependency(self, lib):
        """
        Add the given library as a dependency for this library. A library can 
        be added as a dependency if it is not in testing and another version of
        the same library is not already a dependency.

        A LibraryException is raised if the given library is not a valid
        dependency.

        Input:
            lib (Library): the dependency
        """
        assert isinstance(lib, Library)

        if self.dependencies == None:
            self.dependencies = []
        
        if lib.is_testing == True:
            raise LibraryException("Exception")
        
        for library in self.dependencies:
            if library.name == lib.name:
                raise LibraryException("Exception")

        if self.check_cycle(lib) == False:
            raise LibraryException("Exception")

        self.dependencies = self.dependencies + [lib]

    def get_dependencies(self, depth=0):
        """
        Produces the list of libraries that this library depends on. Libraries 
        with the same name but different versions can appear, but specific
        versions of libraries can only appear at most once.

        Input:
            depth (int): How many levels of dependencies to retrieve, given as a
                natural number. By default, depth = 0 and only produces the list
                of immediate dependencies for the library.

        Returns (list[Library]): The list of libraries that are dependencies for
            this library.
        """
        assert depth >= 0

        list_of_current_dependencies = []
        
        list_of_libraries = [self]

        for i in range(0, depth + 1):
            for libr in list_of_libraries:
                if libr.dependencies != None:
                    list_of_current_dependencies.extend(libr.dependencies)
            list_of_libraries.extend(list_of_current_dependencies)
        
        return list_of_libraries[1::]
        
        # return self.dependencies

    def update_dependency(self, lib):
        """
        Updates an existing dependency to a different version. The library must
        already be a dependency for this library and the update must be a 
        different version than the existing dependency.

        A LibraryException is raised if the given library cannot be updated.

        Input:
            lib (Library): different version of the dependency
        """
        assert isinstance(lib, Library)

        if lib.is_testing == True:
            raise LibraryException("Exception")

        existing_dep = []
        
        for libr in self.dependencies:
            if libr.name == lib.name:
                existing_dep.append(libr)

        if len(existing_dep) == 0:
            raise LibraryException("Exception")

        for libr in existing_dep:
            if libr.version.compare_version(lib.version) == 0:
                raise LibraryException("Exception")

        for idx, libr in enumerate(self.dependencies):
            if libr.name == lib.name:
                self.dependencies[idx] = lib