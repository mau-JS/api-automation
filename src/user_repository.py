import pandas as pd
import logging

logger = logging.getLogger(__name__)

def get_user_data(user_id):
    df_user = pd.read_csv('data/user_data_sample.csv')
    df_preferences = pd.read_csv('data/user_register_data_sample.csv')
    df = df_user.merge(df_preferences, on="user_id",how="inner")
    user = df[df['user_id']==user_id]
    if user.empty:
        raise ValueError(f'User {user_id} was not found')
    return {
        "email": user["email"].iloc[0],
        "category": user["categoria_favorita"].iloc[0],
        "name": user["nombre"].iloc[0]
    }