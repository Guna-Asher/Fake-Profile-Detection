import numpy as np
from datetime import datetime

class FeatureExtractor:
    @staticmethod
    def extract_features(user_data):
        if not user_data:
            return None
            
        try:
            # Calculate account age in days
            created_at = datetime.fromisoformat(user_data['created_at'])
            account_age_days = (datetime.now() - created_at).days
            
            # Calculate activity ratio (tweets per day)
            tweet_count = user_data.get('tweet_count', 1)
            activity_ratio = tweet_count / max(account_age_days, 1)
            
            features = {
                'verified': int(user_data.get('verified', False)),
                'followers_count': np.log1p(user_data.get('followers_count', 0)),
                'following_count': np.log1p(user_data.get('following_count', 0)),
                'tweet_count': np.log1p(user_data.get('tweet_count', 0)),
                'listed_count': np.log1p(user_data.get('listed_count', 0)),
                'account_age_days': account_age_days,
                'followers_following_ratio': user_data.get('followers_count', 1) / max(user_data.get('following_count', 1), 1),
                'activity_ratio': activity_ratio,
                'username_length': len(user_data.get('username', '')),
                'name_length': len(user_data.get('name', '')),
                'description_length': len(user_data.get('description', '')),
                'has_description': int(bool(user_data.get('description', ''))),
                'has_profile_image': int(bool(user_data.get('profile_image_url', '')))
            }
            
            return np.array(list(features.values())).reshape(1, -1)
            
        except Exception as e:
            print(f"Feature extraction error: {e}")
            return None