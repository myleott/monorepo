## Import packages from the root of a monorepo

Instructions:

1. First create a file named `.monorepo_root` at the root of your monorepo.
2. Use `monorepo.load_package` to load packages from anywhere in your monorepo.

Example usage:
```python
import monorepo

# The `load_package` function will search up from the current directory for a
# file named `.monorepo_root`, which is used to determine the root directory
# from which to load the package:
monorepo.load_package("pkg1")

# The pkg1 package can be used directly:
from pkg1 import mymodule1

# Also works with sub-packages:
monorepo.load_package("pkg1.pkg2")
from pkg2 import mymodule2

# Also works functions in the package's __init__.py:
monorepo.load_package("pkg3")
pkg3.some_init_fn()
```

## Caveats
`load_package` breaks modularity: a module `mymodule` imported through a package loaded by `load_package` will result in a separate module from importing that module directly (unlike import aliases):
```py
import monorepo
monorepo.load_package("pkg1.pkg2")
from pkg2.mymodule import fun
fun()
import mymod
mymod.fun()
print(mymod.fun == fun) # False
```
For example, any module initialization code will be executed twice (in `fun()` and then in `mymod.fun()`), there will be duplicate entries in `sys.modules`, etc.


* This can cause module name clashes, at best giving undefined errors, at worst (if a function is defined in different modules) causing silent runtime differences:
```py
# foo.py:
import monorepo
monorepo.load_package("audio.utils")
from utils import fn1

# main.py:
import monorepo
monorepo.load_package("server.utils")
import foo # now sys.modules[utils] is over-written
from utils import fn2 # error: picks audio.utils.foo instead of server.utils.foo
```

## What to use instead:
PYTHONPATH=/path/to/root python main.py
```py
# absolute import from root works from anywhere:
from pkg1.pkg2 import mymod
mymod.fun()

# relative import also works:
from ..pkg2 import mymod
mymod.fun()

# dynamic import also works from anywhere:
import importlib
mymod2 = importlib.import_module("pkg1.pkg2.mymod") # or also relative import path
mymod2.fun()
```
