import torch
import pandas as pd
import os

model = torch.load("model/AgriLoan.pt")
model.eval()

def preprocess(data_dict):
    features = [data_dict["age"], data_dict["farm_size"], data_dict["income"], data_dict["loan_amount"]]
    return torch.tensor(features).float().unsqueeze(0)

def predict(input_data):
    x = preprocess(input_data)
    with torch.no_grad():
        y = model(x)
        return int(y.round().item())

def preprocess_and_save(input_data):
    prediction = predict(input_data)
    input_data["prediction"] = prediction
    df = pd.DataFrame([input_data])

    os.makedirs("data", exist_ok=True)
    if not os.path.exists("data/entries.csv"):
        df.to_csv("data/entries.csv", index=False)
    else:
        df.to_csv("data/entries.csv", mode="a", header=False, index=False)
