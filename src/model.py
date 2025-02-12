import numpy as np
import mlflow
from mlflow.models import set_model


class Embedder(mlflow.pyfunc.PythonModel):
    def load_context(self, context):
        pass

    def predict(self, context, model_input):
        return np.random.random((len(model_input), 200))


set_model(Embedder())
