import pandas as pd


def average_age_by_position(file_path: str):
    data = pd.read_csv(file_path)
    if {'Имя', 'Возраст', 'Должность'}.issubset(set(data.columns)):
        average_age = data.groupby('Должность')['Возраст'].mean().to_dict()
        processed_data = {key: None if pd.isna(value) else value for key, value in average_age.items()}
        return {"status_code": 200, "data": processed_data}
    else:
        return {"status_code": 400, "data": "Невалидный файл"}


print(average_age_by_position("employees.csv"))