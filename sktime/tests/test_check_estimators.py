import os
from sktime.experiments import orchestrator
import pkgutil
import sktime
from sktime.utils.estimator_checks import check_ts_estimator
import inspect
from sklearn.base import BaseEstimator

def test_estimators():
    errors = []

    path = sktime.__path__

    modules_to_check = ['regressors', 'classifiers']
    not_test = ['BaseEstimator', 'BaseClassifier', 'BaseRegressor']
    for importer, modname, ispkg in pkgutil.walk_packages(
        path=path, prefix='sktime.', onerror=lambda x: None):
        for m in modules_to_check:  
            if m in modname:
                module = __import__(modname, fromlist="dummy")
                classes = inspect.getmembers(module, inspect.isclass)
                for c in classes:
                    try:
                        check_ts_estimator(c[1])
                    except:
                        errors.append(f'Estimator {c[0]} failed estimator checks')
        
    assert not errors, "errors occured:\n{}".format("\n".join(errors))
            
    
