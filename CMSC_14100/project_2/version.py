
"""
CMSC 14100 Project Aut 22
"""

class Version:
    """
    A class to represent a semantic version which includes a:  
        - major version number  
        - an optional minor number  
        - an optional patch number  

    A published library will have an exact version with major, minor, and patch
    values, such as 1.0.3 where 1 is the major, 0 is the minor, and 3 is the
    patch. A version used for searching or library matching could be partial,
    such as 1, 1., 2.1 or 2.1.
    """
    def __init__(self, version_str):
        """
        Create a new Version instance based on a version string in the form of
        X, X., X.Y, X.Y., or X.Y.Z where X,Y,and Z are natural numbers.

        Inputs:
            version_str(str): The given semantic version number
        """
        
        #v = version_str.split(".")

        #for idx, val in enumerate(v):
         #   if v[idx] != "":
          #      v[idx] = int(val)
           # elif v[idx] == "":
            #    v.remove(v[idx])

        #while len(v) < 3:
         #   v.append(-1)

        #v = tuple(v)

        self.v = version_str



    def compare_version(self, other):
        """
        Check if this version is smaller, the same, or greater than the
        other version. If a version is partial assume the missing components
        are the smallest possible value (e.g. < 0).

        Inputs:
            other (Version): a Version to compare against

        Returns (int):  
            -1 if self is smaller than other,  
            0 if they have the same version number,  
            1 if  self is larger than other
        """
        assert isinstance(other, Version)

        v = self.v.split(".")

        for idx, val in enumerate(v):
            if v[idx] != "":
                v[idx] = int(val)
            elif v[idx] == "":
                v.remove(v[idx])

        while len(v) < 3:
            v.append(-1)

        v = tuple(v)

        o = other.v.split(".")

        for idx, val in enumerate(o):
            if o[idx] != "":
                o[idx] = int(val)
            elif o[idx] == "":
                o.remove(o[idx])

        while len(o) < 3:
            o.append(-1)

        o = tuple(o)

        maj, min, pat = o
        vmaj, vmin, vpat = v

        if self.v == other.v:
            return 0

        if vmaj < maj:
            return -1

        if vmaj > maj:
            return 1

        if vmaj == maj and vmin != min:
            if vmin < min:
                return -1
            if vmin > min:
                return 1
    
        if vmaj == maj and vmin == min:
            if vpat < pat:
                return -1
            if vpat > pat:
                return 1
        
    def meets_requirement(self, req):
        """
        Checks to see if this version satisfies the requirement.
        Req is a version that was initialized with a string like
        X, X., X.Y, X.Y., or X.Y.Z,
        where X is the major number, Y is the minor, and Z is patch.

        For exact requirement versions (X.Y.Z) this Version will evaluate to
        True if the versions are the same.

        For partial requirement versions (e.g. X or X.Y) this Version will
        evaluate to true if the given parts (X and/or Y) are the same.
      
        Inputs:  
            req(Version): The required version

        Output(bool): If this Version satisfies the requirement
        """

        v = self.v.split(".")

        for idx, val in enumerate(v):
            if v[idx] != "":
                v[idx] = int(val)
            elif v[idx] == "":
                v.remove(v[idx])

        while len(v) < 3:
            v.append(-1)

        v = tuple(v)

        r = req.v.split(".")

        for idx, val in enumerate(r):
            if r[idx] != "":
                r[idx] = int(val)
            elif r[idx] == "":
                r.remove(r[idx])

        while len(r) < 3:
            r.append(-1)

        r = tuple(r)

        maj, min, pat = r
        vmaj, vmin, vpat = v

        if pat != -1 and min != -1 and maj != -1:
            if self.v == req.v:
                return True
            if self.v != req.v:
                return False

        if pat == -1 and min != -1 and maj != -1:
            if maj == vmaj and min == vmin:
                return True
            else:
                return False

        if pat == -1 and min == -1 and maj != -1:
            if maj == vmaj:
                return True
            else:
                return False