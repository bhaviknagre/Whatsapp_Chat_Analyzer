from urlextract import URLExtract

def fetch_stats(selected_user,df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    num_messages = df.shape[0]
    words = []
    for message in df['message']:
        words.extend(message.split())

    num_media_messages = df[df['message'] == '<Media omitted>\n'].shape[0]

    extractor = URLExtract()
    links = []
    for message in df['message']:
        links.extend(extractor.find_urls(message))

    return num_messages, len(words),num_media_messages,len(links)

def most_busy_users(df):
    x = df['user'].value_counts().head()
    df = round((df['user'].value_counts()/df.shape[0])*100,2).reset_index().rename(columns={'count':'percent', 'user':'name'})
    return x,df


def monthly_timeline(selected_user,df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    timeline = df.groupby(['year','month_num','month']).count()['message'].reset_index()
    time = []

    for i in range(timeline.shape[0]):
        time.append(timeline['month'][i] + "-" + str(timeline['year'][i]))
    timeline['time'] = time

    return timeline