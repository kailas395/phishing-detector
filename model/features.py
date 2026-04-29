import re
from sklearn.base import BaseEstimator, TransformerMixin

class URLFeatures(BaseEstimator, TransformerMixin):
    def fit(self, x, y=None):
        return self
    
    def transform(self, texts):
        features = []
        for text in texts:
            urls = re.findall(r'http[s]?://\S+', text)
            num_urls = len(urls)
            has_ip = any(re.search(r'\d+\.\d+\.\d+\.\d+', url) for url in urls)
            suspicious_words = ['login', 'verify', 'bank', 'urgent', 'password']
            contains_suspicious = any(word in text.lower() for word in suspicious_words)

            features.append([num_urls, int(has_ip), int(contains_suspicious)])
        return features