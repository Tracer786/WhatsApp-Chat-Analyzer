def fetch_stats(selected_user, df):

    if selected_user == 'Overall':
        # 1. Fetch number of messages
        num_messages = df.shape[0]  # returning the total number of messages

        # 2. Fetch number of words
        words = []
        for message in df['message']:
            words.extend(message.split())

        return num_messages, words

    # else we need to return the count of messages for the particular user
    # for that we need to use the concept of masking

    else:
        return df[df['user'] == selected_user].shape[0]
