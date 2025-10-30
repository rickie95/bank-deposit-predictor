import pandas as pd


def load_dataset(path: str) -> tuple[pd.DataFrame, pd.Series]:
    data = pd.read_csv(path, index_col='id')

    nominal_columns = ['job', 'marital', 'contact']

    data = data[data['education'] != "unknown"]
    encoded = pd.get_dummies(data, columns=nominal_columns, drop_first=True)
    encoded['education'] = encoded['education'].replace({
        "primary": 1,
        "secondary": 2,
        "tertiary": 3
    })
    encoded['housing'] = encoded['housing'].replace({"no": False, "yes": True})
    encoded['loan'] = encoded['loan'].replace({"no": False, "yes": True})
    encoded['default'] = encoded['default'].replace({"no": False, "yes": True})

    x_data = encoded
    x_data = x_data.drop(columns=['poutcome', 'day', 'month', 'y'])
    y_data = encoded['y']

    return x_data, y_data