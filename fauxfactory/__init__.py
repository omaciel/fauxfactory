"""Generate random data for your tests."""
from importlib import import_module
import os

methods = []

# location for factory modules
factory_dir = os.path.join(os.path.dirname(__file__), 'factories')

# Loop through all factory modules...
for d in os.listdir(factory_dir):
    # ... check that we have a '.py' file...
    if d.endswith('.py') and not d.startswith('__'):
        # Module name is '.factories.<module_name>' without '.py'
        name = ''.join(['.factories.', d[:-3]])
        # Import the module
        module = import_module(name, __package__)
        # Fetch all of its attributes
        for attr in module.__dict__.keys():
            # If attribute name starts with 'gen_'...
            if attr.startswith('gen_'):
                # Add reference to it to locals()
                locals()[attr] = getattr(module, attr)
                # Keep track of all methods being added
                methods.append(attr)

# Add all method names to __all__
__all__ = methods
