
class MR_Popular:
	def __init__(self, data, n):
		self.data = data;
		self.avg_votes = 0;
		self.vote_counts = 0;
		self.popular = {};
		self.n = n;

	def set_avg_votes(self):
		votes = self.data[self.data['vote_average'].notnull()]['vote_average'].astype('int');
		self.avg_votes = votes.mean();

	def set_vote_counts(self, pourcentage=0.90):
		votes_c = self.data[self.data['vote_count'].notnull()]['vote_count'].astype('int');
		self.vote_counts = votes_c.quantile(pourcentage);

	def set_nb_popular(self, n):
		self.n = n;

	def rating(self, pop):
		vc = pop['vote_count'];
		va = pop['vote_average'];
		return (vc / (vc + self.vote_counts) * va) + \
		       (self.vote_counts / (self.vote_counts + vc) * self.avg_votes);

	def get_popular_movies(self):
		self.set_avg_votes();
		self.set_vote_counts();
		features = ['title', 'release_date', 'vote_count', 'vote_average', 'popularity'];
		
		self.popular = self.data[(self.data['vote_count'] >= self.avg_votes) & 
		                         (self.data['vote_count'].notnull()) & 
		                         (self.data['vote_average'].notnull())][features];
		self.popular['vote_count'] = self.popular['vote_count'].astype('int');
		self.popular['vote_average'] = self.popular['vote_average'].astype('int');
		self.popular['rating'] = self.popular.apply(self.rating, axis=1);
		self.popular = self.popular.sort_values('rating', ascending=False);
		self.popular = self.popular.head(self.n);
		print(self.popular);