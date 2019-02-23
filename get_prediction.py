import json
import pickle
import logging
import numpy as np
from sklearn.linear_model import LogisticRegression

logger = logging.getLogger()
logger.setLevel(logging.INFO)

model = pickle.load(open("model/wine_model.pkl", "rb"))


def handler(event, context):
    logger.info("EVENT:{}".format(event))
    payload = event.get("body")
    data = json.loads(payload).get("data")
    pred = list(model.predict_proba(np.array(data).reshape(1, -1))[0])
    return {"statusCode": 200, "body": json.dumps(str(pred))}
