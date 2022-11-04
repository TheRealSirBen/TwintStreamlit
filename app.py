import streamlit as st
from pandas import DataFrame

from datagrip import tweets


class TweetsData:
    data = DataFrame()
    data_photos = []

    def get_tweets(
            self,
            _keyword: str = None,
            _username: str = None,
            _near: st = None,
            _show_following: bool = False,
            _show_followers: bool = False,
            _show_popular_tweets: bool = False,
            _show_user_full: bool = False,
            _limit=2
    ):
        if _keyword or _username:

            if not _username:
                _username = None

            _tweets = tweets(
                keyword=_keyword,
                username=_username,
                near=_near,
                show_following=_show_following,
                show_followers=_show_followers,
                show_popular_tweets=_show_popular_tweets,
                show_user_full=_show_user_full,
                limit=_limit
            )
            self.update_data(_tweets)

    def update_data(self, dataframe: DataFrame):
        self.data = dataframe

    def get_images(self, tweet_idx):
        images = self.data['photos'][tweet_idx]
        self.data_photos = images


tweets_data = TweetsData()

st.set_page_config(
    page_title="Twitter Intelligence Tool",
    page_icon="💡",
)

# Heading
st.header('Twitter Open Source Intelligence Tool')
st.write("CUT: Group 7")

with st.sidebar:
    form = st.form(key="user_form")
    app_username = form.text_input("Username", placeholder='Type username here')
    app_keyword = form.text_input("Keyword", placeholder='Type keyword here')
    app_near = form.text_input("Location", placeholder='Type Location or Nearby area')
    form.form_submit_button(
        label='Get Tweets',
        type='primary',
        on_click=tweets_data.get_tweets(_keyword=app_keyword, _near=app_near, _username=app_username)
    )

tab_raw_data, tab_media = st.tabs(["Raw Data", "Media Data"])

# Hashtags, Geo

if len(tweets_data.data) not in [0, None]:

    # Raw Dataframe
    with tab_raw_data:
        st.write('Raw Data Quick View')
        tweets_df = tweets_data.data
        tweets_columns = [
            'date', 'username', 'name', 'tweet',
            'nreplies', 'nretweets', 'nlikes',
            'near', 'geo'
        ]
        display_df = tweets_df[tweets_columns]
        st.dataframe(display_df)
