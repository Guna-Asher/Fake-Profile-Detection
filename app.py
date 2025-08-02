from flask import Flask, request, jsonify, render_template
from twitter_api import TwitterAPI
from twitter_api import TwitterAPI
from features import FeatureExtractor
from model import ProfileClassifier

app = Flask(__name__)
twitter_api = TwitterAPI()
classifier = ProfileClassifier()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_profile', methods=['GET'])
def check_profile():
    username = request.args.get('username', '').strip()
    if not username:
        return jsonify({'error': 'Username is required'}), 400
    
    # Get profile data
    user_data = twitter_api.get_user_profile(username)
    if not user_data:
        return jsonify({'error': 'Profile not found or API error'}), 404
    
    # Extract features
    features = FeatureExtractor.extract_features(user_data)
    
    # Make prediction
    fake_probability = classifier.predict(features)
    
    # Prepare response
    response = {
        'username': user_data['username'],
        'name': user_data['name'],
        'verified': user_data['verified'],
        'profile_image': user_data['profile_image_url'],
        'followers_count': user_data['followers_count'],
        'following_count': user_data['following_count'],
        'tweet_count': user_data['tweet_count'],
        'account_created': user_data['created_at'],
        'description': user_data['description'],
        'fake_probability': fake_probability,
        'is_fake': fake_probability > 0.7,  # Using 0.7 threshold
        'fake_confidence': f"{fake_probability*100:.1f}%",
        'status': 'success'
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)