def fetch_stats(selected_user, df):

    if selected_user == 'Overall':
        return df.shape[0]  # returning the total number of messages

    # else we need to return the count of messages for the particular user
    # for that we need to use the concept of masking

    else:
        return df[df['user'] == selected_user].shape[0]
