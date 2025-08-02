import tweepy
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

class TwitterAPI:
    def __init__(self):
        self.client = tweepy.Client(
            bearer_token=os.getenv('TWITTER_BEARER_TOKEN'),
            consumer_key=os.getenv('TWITTER_API_KEY'),
            consumer_secret=os.getenv('TWITTER_API_SECRET'),
            access_token=os.getenv('TWITTER_ACCESS_TOKEN'),
            access_token_secret=os.getenv('TWITTER_ACCESS_SECRET')
        )
        
    def get_user_profile(self, username):
        try:
            # Get basic user info
            user = self.client.get_user(
                username=username,
                user_fields=[
                    'created_at',
                    'description',
                    'verified',
                    'profile_image_url',
                    'public_metrics'
                ]
            )
            
            if not user.data:
                return None
                
            # Format response
            profile_data = {
                'id': user.data.id,
                'name': user.data.name,
                'username': user.data.username,
                'created_at': user.data.created_at.isoformat(),
                'description': user.data.description or '',
                'verified': user.data.verified,
                'profile_image_url': user.data.profile_image_url.replace('_normal', ''),
                'followers_count': user.data.public_metrics['followers_count'],
                'following_count': user.data.public_metrics['following_count'],
                'tweet_count': user.data.public_metrics['tweet_count'],
                'listed_count': user.data.public_metrics['listed_count']
            }
            
            return profile_data
            
        except tweepy.errors.TweepyException as e:
            print(f"Twitter API Error: {e}")
            return None
        except Exception as e:
            print(f"Unexpected Error: {e}")
            return None