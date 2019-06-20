import warnings

from . import bmkgkit, datakit, dlkit, prepkit, viewkit

warnings.warn("bmkgkit will be removed in version 0.2.0, "
              "use prepkit instead",
              DeprecationWarning, stacklevel=2)
