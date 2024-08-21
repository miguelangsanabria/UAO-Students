from catboost import CatBoostClassifier
import threading


class ModelLoader:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(ModelLoader, cls).__new__(cls)
                    cls._instance.model = CatBoostClassifier()
                    cls._instance.model.load_model("models/catboost_model.cbm")
        return cls._instance

    def predict(self, X):
        return self.model.predict(X)
