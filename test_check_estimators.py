import os
from sktime.experiments import orchestrator
import pkgutil
import sktime
from sktime.utils.estimator_checks import check_ts_estimator
import inspect

path = sktime.__path__

moduels_to_check = ['regressors', 'classifiers']

for importer, modname, ispkg in pkgutil.walk_packages(
    path=path, prefix='sktime.', onerror=lambda x: None):
    for m in moduels_to_check:  
        if m in modname:
            module = __import__(modname, fromlist="dummy")
            classes = inspect.getmembers(module, inspect.isclass)
            for c in classes:
                class_name = c[0]
                class_loaded = c[1]
                check_ts_estimator(class_loaded)
    
    