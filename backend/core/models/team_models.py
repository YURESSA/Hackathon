from backend.core import db


class Team(db.Model):
    __tablename__ = 'teams'
    team_id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.String(255), nullable=True)

    team_lead_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    team_lead = db.relationship('User', foreign_keys=[team_lead_id])

    members = db.relationship('User', secondary='team_members', backref='teams')

    def __repr__(self):
        return f"<Team {self.team_name}>"


class TeamMember(db.Model):
    __tablename__ = 'team_members'
    team_id = db.Column(db.Integer, db.ForeignKey('teams.team_id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), primary_key=True)
