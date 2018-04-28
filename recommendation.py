import numpy as np
from lightfm.datasets import fetch_movielens
from lightfm import LightFM

#fetch data and format it
data = fetch_movielens(min_rating=4.0)

#print training and testing data
print(repr(data['train']))
print(repr(data['test']))

#create model
model = LightFM(loss = 'warp')

#train model
model.fit(data['train'], epochs=30, num_threads=2)

def sample_recommendations(model, data, user_ids):
    
    #no. of user and movies in training data
    n_users, n_items = data['train'].shape
    
    #generate recommendation ffor each user we input
    for user_id in user_ids:
        
        #movies they already like
        known_posititves = data['item_labels'][data['train'].tocsr()[user_id].indices]
