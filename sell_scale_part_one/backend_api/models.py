from .extensions import db

# Values to Hold: “Buy” specific stock tickers (i.e. enter ticker, quantity, and save the amount somewhere in a database)
class Stock(db.Model):
    stock_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ticker_name = db.Column(db.String(50), nullable=False)
    ticker_quantity = db.Column(db.Integer, nullable=False)
    ticker_price = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"), nullable=False)

# models, we will have one for the user, and one for the stocks they hold 
class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(60))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(60))
    stock = db.relationship('Stock')