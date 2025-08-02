import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import os

class ProfileClassifier:
    def __init__(self):
        self.model = None
        self.scaler = None
        self.load_model()
        
    def train_model(self):
        # This is a placeholder - in production you would use real labeled data
        print("Training new model...")
        
        # Dummy data with the same structure as our features
        X = np.random.rand(100, 12)  # 12 features
        y = np.random.randint(0, 2, 100)  # Binary labels
        
        # Scale features
        self.scaler = StandardScaler()
        X_scaled = self.scaler.fit_transform(X)
        
        # Train model
        self.model = RandomForestClassifier(
            n_estimators=200,
            max_depth=10,
            random_state=42,
            class_weight='balanced'
        )
        self.model.fit(X_scaled, y)
        
        # Save model
        self.save_model()
        
    def save_model(self):
        with open('model.pkl', 'wb') as f:
            pickle.dump({
                'model': self.model,
                'scaler': self.scaler
            }, f)
            
    def load_model(self):
        try:
            if os.path.exists('model.pkl'):
                with open('model.pkl', 'rb') as f:
                    data = pickle.load(f)
                    self.model = data['model']
                    self.scaler = data['scaler']
            else:
                self.train_model()
        except Exception as e:
            print(f"Error loading model: {e}")
            self.train_model()
            
    def predict(self, features):
        if features is None:
            return 0.5  # Neutral probability if features are invalid
            
        try:
            # Scale features
            features_scaled = self.scaler.transform(features)
            # Get probability of being fake (class 1)
            return float(self.model.predict_proba(features_scaled)[0][1])
        except Exception as e:
            print(f"Prediction error: {e}")
            return 0.5