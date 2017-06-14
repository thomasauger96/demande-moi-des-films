class User:

    def __init__(self, sender_id):
        self.id = sender_id
        self.good_ratings = []
        self.bad_ratings = []
        self.neutral_ratings = []
        self.ratings = dict()
        self.average_rating = 0
        self.latest_movie_asked = None
        self.questions_before_recommendation = None

    def has_been_asked_a_question(self):
        return self.latest_movie_asked is not None

    # Si l'utilisateur a répondu oui
    def answer_yes(self):
        self.good_ratings.append(self.latest_movie_asked)
        self.questions_before_recommendation -= 1

    # Si l'utilisateur a répondu non
    def answer_no(self):
        self.bad_ratings.append(self.latest_movie_asked)
        self.questions_before_recommendation -= 1

    # Si l'utilisateur a répondu autre chose
    def answer_neutral(self):
        self.neutral_ratings.append(self.latest_movie_asked)

    # Enregistre le film qu'on a demandé à l'utilisateur pour le traiter au prochain message
    def set_question(self, movie_number):
        self.latest_movie_asked = movie_number
        if self.questions_before_recommendation is None or self.questions_before_recommendation <= 0:
            self.questions_before_recommendation = 5

    # Traite le message de l'utilisateur
    def give_message(self, message):
        # Si on a rien demandé à l'utilisateur alors on ne fait rien
        if self.latest_movie_asked is None:
            return

        # On enlève les espaces en trop et on met tout le message en miniscule
        clean_message = message.lower().strip()
        self.latest_movie_asked = None

        # Il faut traiter ici le message
        return

    # Détermine si l'utilisateur a répondu à suffisamment de questions pour lui faire une recommandation.
    def should_make_recommendation(self):
        if self.questions_before_recommendation is None:
            return False
        return self.questions_before_recommendation <= 0

    # Donne la norme de l'utilisateur
    def get_norm(self):
        return 1
