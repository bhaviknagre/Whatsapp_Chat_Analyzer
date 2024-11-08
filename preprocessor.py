import pandas as pd
import re
from datetime import datetime

def preprocess(data):
    pattern = r'\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\u202f(?:am|pm|AM|PM)\s-\s'
    messages = re.split(pattern, data)[1:]
    dates = re.findall(pattern, data)
    cleaned_dates = [date.replace(" - ", "") for date in dates]

    df = pd.DataFrame({'user_message': messages, 'message_date': cleaned_dates})

    df['message_date'] = pd.to_datetime(df['message_date'], format='%d/%m/%y, %I:%M %p')

    df['message_date'] = df['message_date'].dt.strftime('%Y-%m-%d, %I:%M %p')

    df.rename(columns={'message_date': 'date'}, inplace=True)

    users = []
    messages = []

    for message in df['user_message']:
        entry = re.split(r'([\w\W]+?):\s', message)
        if entry[1:]:
            users.append(entry[1])
            messages.append(entry[2])
        else:
            users.append('group notification')
            messages.append(entry[0])
    df['user'] = users
    df['message'] = messages
    df.drop(columns=['user_message'], inplace=True)
    df['date'] = df['date'].str.split(',').str[0]
    df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d', errors='coerce')
    df['year'] = df['date'].dt.year
    df['month_num'] = df['date'].dt.month
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    return df