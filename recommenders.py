class popularity_recommender() :
    def __init__(self) :
        self.train_data = None
        self.user = None
        self.song = None
        self.playcount = None
        self.recommendations = None
    def create(self, train_data, user, song, playcount) :
        self.train_data = train_data
        self.user = user
        self.song = song
        self.playcount = playcount 

        train_data_grouped = train_data.groupby([self.song]).agg({self.playcount : 'mean'}).sort_values([self.playcount], ascending = False)
        train_data_grouped['score'] = train_data_grouped[self.playcount] / train_data_grouped[self.playcount].count() * 100
        self.recommendations = train_data_grouped.reset_index()
    # recommend (non-rated) songs to a user
    def recommend(self, user) :
        user_recommendations = self.recommendations
        user_recommendations['user'] = user
        return user_recommendations
    # Predict the rating a user would give to a song
    def predict(self, song, name) :
        user_recommendations = self.recommendations
        self.song = song
        return user_recommendations[user_recommendations[self.song] == name]['score']

poprec = popularity_recommender()
poprec.create('songs_train', 'user', 'song', 'rating')
poprec.recommend('X').head(10)