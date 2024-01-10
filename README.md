# Import packages and modules from the root of a monorepo

Instructions:

1. First create a file named `.monorepo_root` at the root of your monorepo.
2. Use `monorepo.load_package` (or `monorepo.load_module`) to load packages (or modules) from anywhere in your monorepo.

Example usage for `load_package`:
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


# Also works with renaming packages (useful for invalid package names or for name clashes):
monorepo.load_package("invalid-namge", package_name = "pkg3")
from pkg3 import mymodule3
```

Example usage for `load_module`:
```python
import monorepo

# The `load_module` function will search up from the current directory for a
# file named `.monorepo_root`, which is used to determine the root directory
# from which to load the module:
mymodule = monorepo.load_module("pkg1.module1")
mymodule.my_function()

mymodule2 = monorepo.load_module("pkg1.pkg2.module2")
mymodule2.my_function()
```
