"""Store all modules that generate data here."""

import os
import random

if "FAUXFACTORY_DISABLE_SEED_RANDOMIZATION" not in os.environ:
    random.seed()
