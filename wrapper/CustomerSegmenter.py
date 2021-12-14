import joblib
import logging
import numpy as np
from typing import Dict, List, Union, Iterable

logger = logging.getLogger(__name__)

class CustomerSegmenter(object):
   def __init__(self):
       self.ready = False

   def load(self):
       logger.info("Loading...")
       self._model = joblib.load('models/lr/model.joblib')
       self.ready = True

   def predict(self, X: np.ndarray, names: Iterable[str], meta: Dict = None) -> Union[np.ndarray, List, str, bytes]:
       try:
           if not self.ready:
               self.load()

           logger.info("Calling predict_proba...")
           return self._model.predict_proba(X)

       except Exception as ex:
           logging.exception("Exception during predict!")
           logging.exception(f"{ex}")
