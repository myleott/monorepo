# Import packages from the root of a monorepo

Instructions:

1. First create a file named `.monorepo_root` at the root of your monorepo.
2. Use `monorepo.load_package` to load packages from anywhere in your monorepo.

Example usage:
```python
import monorepo

# The `load_package` function will search up from the current directory for a
# file named `.monorepo_root`, which is used to determine the root directory
# from which to load `example.package.foo`:
foo = monorepo.load_package("example.package.foo")

# The foo package can be used directly:
foo.bar_function()

# We can also import other subpackages:
from foo.bar import baz
```
