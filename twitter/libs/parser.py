
def parse_tweet(tweet):
    
    data = [
            "None" if tweet.community_note == None else  tweet.community_note,
            tweet.created_at,
            tweet.edits_remaining,
            tweet.favorite_count,
            tweet.full_text.encode("utf-8").decode('utf-8', errors='ignore'),
            "None" if tweet.has_card == None else tweet.has_card,
            "None" if tweet.has_community_notes == None else  tweet.has_community_notes,
            ",".join(tweet.hashtags),
            tweet.id,
            "None" if tweet.in_reply_to == None else tweet.in_reply_to,
            tweet.is_quote_status,
            tweet.is_translatable,
            tweet.lang,
            parse_media(tweet.media),
            "None" if tweet.place == None else  tweet.place,
            "None" if tweet.poll == None else tweet.poll,
            tweet.possibly_sensitive,
            "None" if tweet.quote == None else tweet.quote.id,
            tweet.quote_count,
            tweet.reply_count,
            tweet.retweet_count,
            "None" if tweet.retweeted_tweet == None else tweet.retwetted_tweet.id,
            "None" if tweet.thumbnail_title == None else tweet.thumbnail_title,
            "None" if tweet.thumbnail_url == None else tweet.thumbnail_url,
            parse_urls(tweet.urls),
            tweet.user.id,
            "Unavailable" if tweet.view_count == None else tweet.view_count,
            "Unavailable" if tweet.view_count_state == None else tweet.view_count_state
            ]

    for i in range(len(data)):
        data[i] = str(data[i]).encode("utf-8").decode('utf-8', errors='ignore')

    return data


def parse_media(media):
    if not media:
        return "None"
    media_urls = []
    for m in media:
        media_urls.append(m["media_url_https"])
    return ",".join(media_urls)


def parse_urls(urls):
    if urls == [] or not urls:
        return "None"
    
    url_list = []
    for url in urls:
        url_list.append(url["expanded_url"])

    return ",".join(url_list)


def parse_user(user):

    data = [
        user.can_dm,
        user.can_media_tag,
        user.created_at,
        user.default_profile,
        user.default_profile_image,
        user.description.encode("utf-8").decode('utf-8', errors='ignore'),
        parse_urls(user.description_urls),
        user.fast_followers_count,
        user.favourites_count,
        user.followers_count,
        user.following_count,
        user.has_custom_timelines,
        user.id,
        user.is_blue_verified,
        user.is_translator,
        user.listed_count,
        handle_location(user.location),
        user.media_count,
        user.name.encode("utf-8").decode('utf-8', errors='ignore'),
        user.normal_followers_count,
        handle_pinned_tweets(user.pinned_tweet_ids).encode("utf-8").decode('utf-8', errors='ignore'),
        user.possibly_sensitive,
        user.profile_banner_url,
        user.profile_image_url,
        user.protected,
        user.screen_name,
        user.statuses_count,
        user.translator_type,
        "None" if user.url == None else user.url,
        parse_urls(user.urls),
        user.verified,
        user.want_retweets,
    ]

    for i in range(len(data)):
        data[i] = str(data[i]).encode("utf-8").decode('utf-8', errors='ignore')

    return data


def handle_location(location):
    if type(location) == type(""):
        return location
    return ("Location")

def handle_pinned_tweets(lst):
    if lst == [] or not lst:
        return "None"
    
    tweet_list = []
    for tweet in lst:
        tweet_list.append(tweet)

    return ",".join(tweet_list)