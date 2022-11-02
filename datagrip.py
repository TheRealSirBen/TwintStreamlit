# import nest_asyncio
import twint


def tweets(
        keyword: str,
        username: str,
        near: str,
        show_following: bool,
        show_followers: bool,
        show_user_full: bool,
        show_popular_tweets: bool,
        limit=None
):
    # nest_asyncio.apply()
    # Twint Configuration
    c = twint.Config()
    c.Username = username
    c.Following = show_following
    c.Followers = show_followers
    c.User_full = show_user_full
    c.Search = keyword
    c.Near = near
    c.Limit = limit
    c.Popular_tweets = show_popular_tweets

    c.Pandas = True
    c.Hide_output = True
    twint.run.Search(c)

    data = twint.storage.panda.Tweets_df
    return data
