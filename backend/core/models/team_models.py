from backend.core import db


class Team(db.Model):
    __tablename__ = 'teams'
    team_id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.String(255), nullable=True)

    team_lead_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    team_lead = db.relationship('User', foreign_keys=[team_lead_id])

    members = db.relationship('User', secondary='team_members', backref='teams')

    cases = db.relationship('HackathonCase', secondary='team_cases', backref='teams')

    def __repr__(self):
        return f"<Team {self.team_name}>"

    def to_dict(self):
        # Получаем оценки команды
        reviews = self.artifact_reviews
        review_data = []
        for review in reviews:
            review_data.append({
                "jury_id": review.jury_id,
                "criteria": {
                    "criterion_1": review.criterion_1,
                    "criterion_2": review.criterion_2,
                    "criterion_3": review.criterion_3,
                    "criterion_4": review.criterion_4,
                    "criterion_5": review.criterion_5
                },
                "comment": review.comment
            })

        return {
            "team_id": self.team_id,
            "team_name": self.team_name,
            "description": self.description,
            "team_lead": {
                "user_id": self.team_lead.user_id,
                "username": self.team_lead.username,
                "full_name": self.team_lead.full_name
            } if self.team_lead else None,
            "members": [member.to_dict() for member in self.members],
            "cases": [case.title for case in self.cases],
            "artifacts": self.artifacts.to_dict() if self.artifacts else None,
            "reviews": review_data  # Добавляем оценки
        }


class TeamMember(db.Model):
    __tablename__ = 'team_members'
    team_id = db.Column(db.Integer, db.ForeignKey('teams.team_id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), primary_key=True)


from backend.core import db


class TeamCase(db.Model):
    __tablename__ = 'team_cases'
    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.team_id'))  # фикс тут
    case_id = db.Column(db.Integer, db.ForeignKey('hackathon_cases.case_id'))


class TeamArtifacts(db.Model):
    __tablename__ = 'team_artifacts'
    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.team_id'), nullable=False, unique=True)

    github_url = db.Column(db.String(255))
    figma_url = db.Column(db.String(255))
    hosting_url = db.Column(db.String(255))
    presentation_url = db.Column(db.String(255))
    extra_links = db.Column(db.Text)

    team = db.relationship('Team', backref=db.backref('artifacts', uselist=False))

    def to_dict(self):
        return {
            "team_id": self.team_id,
            "github_url": self.github_url,
            "figma_url": self.figma_url,
            "hosting_url": self.hosting_url,
            "presentation_url": self.presentation_url,
            "extra_links": self.extra_links,
        }


class ArtifactReview(db.Model):
    __tablename__ = 'artifact_reviews'
    id = db.Column(db.Integer, primary_key=True)

    jury_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.team_id'), nullable=False)

    criterion_1 = db.Column(db.Integer, nullable=False)
    criterion_2 = db.Column(db.Integer, nullable=False)
    criterion_3 = db.Column(db.Integer, nullable=False)
    criterion_4 = db.Column(db.Integer, nullable=False)
    criterion_5 = db.Column(db.Integer, nullable=False)

    comment = db.Column(db.Text)

    jury = db.relationship("User", backref="artifact_reviews")
    team = db.relationship("Team", backref="artifact_reviews")

    __table_args__ = (
        db.UniqueConstraint('jury_id', 'team_id', name='uq_jury_team_review'),
    )
