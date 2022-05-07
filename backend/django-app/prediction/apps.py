from django.apps import AppConfig
import pandas as pd
from joblib import load
import os


class PredictionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'prediction'
    MLMODEL_FOLDER = os.path.join(BASE_DIR, 'prediction/mlmodel/')
    MLMODEL_FILE = os.path.join(MLMODEL_FOLDER, "IRISRandomForestClassifier.joblib")
    mlmodel = load(MLMODEL_FILE)
