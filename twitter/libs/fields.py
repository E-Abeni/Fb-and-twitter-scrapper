selected_tweet_attributes = ['community_note',
                             'created_at',
                             'edits_remaining',
                             'favorite_count',
                             'full_text',
                             'has_card',
                             'has_community_notes',
                             'hashtags',
                             'id',
                             'in_reply_to',
                             'is_quote_status',
                             'is_translatable',
                             'lang',
                             'media',
                             'place',
                             'poll',
                             'possibly_sensitive',
                             'quote',
                             'quote_count',
                             'reply_count',
                             'retweet_count',
                             'retweeted_tweet',
                             'thumbnail_title',
                             'thumbnail_url',
                             'urls',
                             'user',
                             'view_count',
                             'view_count_state']

removed_tweet = 'created_at_datetime, related_tweets, thread, replies, reply_to'


selected_tweet_functions = ['get_favoriters',
                            'get_retweeters',
                            'get_similar_tweets']


selected_user_attributes = ['can_dm',
                            'can_media_tag',
                            'created_at',
                            'default_profile',
                            'default_profile_image',
                            'description',
                            'description_urls',
                            'fast_followers_count',
                            'favourites_count',
                            'followers_count',
                            'following_count',
                            'has_custom_timelines',
                            'id',
                            'is_blue_verified',
                            'is_translator',
                            'listed_count',
                            'location',
                            'media_count',
                            'name',
                            'normal_followers_count',
                            'pinned_tweet_ids',
                            'possibly_sensitive',
                            'profile_banner_url',
                            'profile_image_url',
                            'protected',
                            'screen_name',
                            'statuses_count',
                            'translator_type',
                            'url',
                            'urls',
                            'verified',
                            'want_retweets'
                            ]

removed_user = [
    'created_at_datetime',
    'withheld_in_countries'
]

selected_user_functions = ['get_dm_history',
                            'get_followers',
                            'get_followers_you_know',
                            'get_following',
                            'get_highlights_tweets',
                            'get_latest_followers',
                            'get_latest_friends',
                            'get_subscriptions',
                            'get_tweets',
                            'get_verified_followers',
                           ]

    
