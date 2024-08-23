from catboost import CatBoostClassifier
import threading

"""
ModelLoader Singleton para cargar y usar el modelo de clasificación CatBoost

Esta clase implementa el patrón de diseño Singleton para asegurar que solo una instancia del modelo 
CatBoostClassifier sea creada y utilizada a lo largo de la aplicación. Utiliza un bloqueo de 
hilos para garantizar la seguridad en entornos multi-hilo.
"""


class ModelLoader:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        """
        Crea una nueva instancia de la clase si aún no existe. Carga el modelo CatBoost desde un archivo.
        """
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(ModelLoader, cls).__new__(cls)
                    cls._instance.model = CatBoostClassifier()
                    cls._instance.model.load_model("models/catboost_model.cbm")
        return cls._instance

    def predict(self, X):
        """
        Realiza predicciones utilizando el modelo CatBoost cargado.
        """
        return self.model.predict(X)
