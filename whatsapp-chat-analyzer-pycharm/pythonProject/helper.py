from urlextract import URLExtract


def fetch_stats(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    # fetch the number of messages
    num_messages = df.shape[0]

    # fetch the number of words
    words = []
    for message in df['message']:
        words.extend(message.split())

    # fetch the number of media messages
    num_media_messages = df[df['message'] == '<Media omitted>\n'].shape[0]

    # fetch number of links shared
    # links = []
    # for message in df['message']:
    #     links.extend(extractor.find_urls(message))

    # Initialize URLExtract object
    extractor = URLExtract()

    links = []
    for message in df['message']:
        links.extend(extractor.find_urls(message))

    return num_messages, len(words), num_media_messages, len(links)

    # it is due to the above if condition that we are not using the below code
    # by using the code below we have reduced the length of the code

    # if selected_user == 'Overall':
    #     # 1. Fetch number of messages
    #     num_messages = df.shape[0]  # returning the total number of messages
    #
    #     # 2. Fetch number of words
    #     words = []
    #     for message in df['message']:
    #         words.extend(message.split())
    #
    #     return num_messages, len(words)
    #
    # # else we need to return the count of messages for the particular user
    # # for that we need to use the concept of masking
    #
    # else:
    #     new_df = df[df['user'] == selected_user]
    #     num_messages = new_df.shape[0]
    #
    #     words = []
    #     for message in new_df['message']:
    #         words.extend(message.split())
    #
    #     return num_messages, len(words)


def most_busy_users(df):
    x = df['user'].value_counts().head()
    # percentage of messages by a user
    df = round((df['user'].value_counts() / df.shape[0]) * 100, 2).reset_index().rename(
        columns={'index': 'name', 'user': 'percent'})
    return x, df
