from flask import Flask, jsonify
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__) # Creates Flask app
api = Api(app) # Creates API
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123password@localhost:3306/nflstats' # Database connection
db = SQLAlchemy(app) # Creates MySQL database

# Base URL for API
BASE = "http://127.0.0.1:5000/"

# Create Models, return dictionaries to each model to display as json.

class PlayerModel(db.Model):

    # Gather basic player information
    __tablename__ = 'players_2013-12-12 1(in)'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)  
    college = db.Column(db.String, nullable=False)
    position = db.Column(db.String, nullable=False)
    draft_year = db.Column(db.String, nullable=False)
    draft_team = db.Column(db.String, nullable=False)

    # Extend existing table 
    __table_args__ = {'extend_existing': True}

    def to_dict(self): 
        return {
        "id": self.id,
        "name": self.name,
        "college": self.college,
        "position": self.position,
        "draft_year": self.draft_year,
        "Draft Team": self.draft_team
        }
    

class DraftPickModel(db.Model):

    # Specific draft pick: player, # drafted, team drafted to.
    __tablename__ = 'players_2013-12-12 1(in)'

    id = db.Column(db.Integer, primary_key=True)
    draft_pick = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    draft_team = db.Column(db.String, nullable=False)

    __table_args__ = {'extend_existing': True}

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "draft pick": self.draft_pick,
            "team": self.draft_team
        }
    

class TeamModel(db.Model):

    # Players that were on specific team, prompts: name, team, position, draft year. 
    __tablename__ = 'players_2013-12-12 1(in)'

    id = db.Column(db.Integer, primary_key=True)
    draft_team = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    position = db.Column(db.String, nullable=True)
    
    __table_args__ = {'extend_existing': True}

    def to_dict(self):
        return {
            "id": self.id,
            "team": self.draft_team,
            "player": self.name,
            "position": self.position
        }
    

class DraftClassModel(db.Model):

    # Player data from draft class, how long they were in the league.
    __tablename__ = 'players_2013-12-12 1(in)'

    id = db.Column(db.Integer, primary_key=True)
    year_start = db.Column(db.Integer, nullable=False)
    draft_pick = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    __table_args__ = {'extend_existing': True}

    def to_dict(self):
        return {
            "id": self.id,
            "player": self.name,
            "draft year": self.year_start,
            "draft pick": self.draft_pick
        }


class Player(Resource):
    
    @app.route('/player/<string:name>', methods=["GET"])
    def get_player(name):

        player = PlayerModel.query.filter_by(name=name).first() # Collects only one player (full name: name)
        if player:
            return PlayerModel.to_dict(player)
        return jsonify({'message': 'Player not found'}), 404 # Abort, if player not found in MySQL database.
    

class PlayerIDClass(Resource):
    @app.route('/playerid/<int:id>', methods=["GET"])
    def get_player_id(id):

        player_id = PlayerModel.query.filter_by(id=id).first()

        if player_id:
            return jsonify(PlayerModel.to_dict(player_id))
        return jsonify({'message': 'Player not found by ID'})


class DraftPick(Resource):
    @app.route('/draftpick/<string:pick>', methods=["GET"])
    def get_draft_pick(pick):

        draft_pick = DraftPickModel.query.filter_by(draft_pick=pick).all() # Collects all players who were drafted at "pick"
        if draft_pick:
            return jsonify([pick.to_dict() for pick in draft_pick])
        return jsonify({'message': 'Draft pick not found'}), 404 # Prompts if value isn't a string, or if draft pick isn't found.
    

class Team(Resource):
    @app.route('/team/<string:draft_team>', methods=["GET"])
    def get_team(draft_team):

        team = TeamModel.query.filter_by(draft_team=draft_team).all() # Collects all players who were apart of "draft_team"
        if team:
            return jsonify([team_name.to_dict() for team_name in team])
        return jsonify({'message': "Team not found"}), 404 # Abort, if team isn't found in MySQL database.
    

class DraftClass(Resource):
    @app.route('/draftclass/<string:year_start>', methods=["GET"])
    def get_draft_class(year_start):

        draft_class = DraftClassModel.query.filter_by(year_start=year_start).all() # Collects all players who were drafted in "year_start"

        if draft_class:
            return jsonify([draft.to_dict() for draft in draft_class])
        return jsonify({'message': 'Draft year not found'}), 404 # Prompts if draft year isn't found on MySQL database


if __name__ == "__main__":

    # Run the API
    app.run(debug=True)