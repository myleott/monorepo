import inspect
import os
import sys
from importlib import util
from pathlib import Path


def load_package(package, root:str = None):
    if not root:
        # Find `.monorepo_root` relative to the importing code.
        root = importer = Path(inspect.stack()[1].filename).resolve()
    else:
        root = Path(root).resolve()
    while not (root / ".monorepo_root").exists():
        if root == root.parent:
            raise FileNotFoundError(
                f"Couldn't find .monorepo_root in parents of {importer}"
            )
        root = root.parent

    name_parts = package.split(".")
    package_name = name_parts[-1]
    package_dir = os.path.join(*([str(root)] + name_parts))
    location = os.path.join(package_dir, "__init__.py")

    spec = util.spec_from_file_location(package_name, location)
    package = util.module_from_spec(spec)
    sys.modules[package_name] = package
    spec.loader.exec_module(package)

    return package
