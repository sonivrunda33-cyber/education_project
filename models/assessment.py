class Assessment:
    def __init__(
        self,
        score,
        strengths=None,
        weaknesses=None,
        skills=None,
        recommendation=""
    ):
        self.score = score
        self.strengths = strengths or []
        self.weaknesses = weaknesses or []
        self.skills = skills or {}
        self.recommendation = recommendation

    def get_score(self):
        return self.score

    def get_strengths(self):
        return self.strengths

    def get_weaknesses(self):
        return self.weaknesses

    def get_skills(self):
        return self.skills