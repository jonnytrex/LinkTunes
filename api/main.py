
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

##CREATE DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///temp.db'
db = SQLAlchemy()
db.init_app(app)

##CREATE TABLE
# User account info
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    wallet_id = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    
    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

# Artist account
class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    #artist type can be musician, visual artist, clothing etc
    artist_type = db.Column(db.String(30), nullable=False)
    wallet_id = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    #preferred type of crypto to be paid in
    payment_favorite = db.Column(db.String(250), nullable=False)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

# Merch 
class Merch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    #merch type can be music, art, clothing etc
    merch_type = db.Column(db.String(30), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    
    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

with app.app_context():
    db.create_all()

#get all users
@app.route('/users', methods=['GET'])
def get_all_users():
    result = db.session.execute(db.select(User).order_by(User.name))
    all_users = result.scalars().all()
    return jsonify(users=[user.to_dict() for user in all_users]) 

#get user by id
@app.route('/users/<int:id>', methods=['GET'])
def get_user_by_id(id: int):
    user_selected = db.get_or_404(User,id)
    return jsonify(user_selected.to_dict()) 

#get user by wallet id
@app.route("/search")
def get_user_by_wallet():
    query_wallet = request.args.get("wallet")
    result = db.session.execute(db.select(User).where(User.wallet_id == query_wallet))
    
    all_users = result.scalars().all()
    if all_users:
        return jsonify(users=[user.to_dict() for user in all_users])
    else:
        return jsonify(error={"Not Found": "Sorry, no user with that wallet."}), 404

# Create a new user
# Test this inside Postman. Request type: Post ->  Body ->  x-www-form-urlencoded
@app.route("/add_user", methods=["POST"])
def post_new_user():
    new_user = User(
        name=request.form.get("name"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        wallet_id=request.form.get("wallet_id"),
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new user."})





if __name__ == '__main__':
    app.run(debug=True)