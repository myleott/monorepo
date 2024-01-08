import inspect
import os
import sys
from importlib import util
from pathlib import Path

def _find_root(root):
    if not root:
        # Find `.monorepo_root` relative to the importing code.
        root = importer = Path(inspect.stack()[2].filename).resolve()
    else:
        root = Path(root).resolve()
    while not (root / ".monorepo_root").exists():
        if root == root.parent:
            raise FileNotFoundError(
                f"Couldn't find .monorepo_root in parents of {importer}"
            )
        root = root.parent
    return str(root)

def load_package(package, root:str = None, package_name = None):
    root = _find_root(root)
    name_parts = package.split(".")
    package_name = package_name or name_parts[-1]
    package_dir = os.path.join(*([root] + name_parts))
    location = os.path.join(package_dir, "__init__.py")

    spec = util.spec_from_file_location(package_name, location)
    package = util.module_from_spec(spec)
    sys.modules[package_name] = package
    spec.loader.exec_module(package)

    return package

def load_module(package, root:str = None):
    root = _find_root(root)
    if root not in sys.path:
        sys.path.append(root)
    import importlib
    return importlib.import_module(package)
