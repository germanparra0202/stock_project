from flask import session, request, jsonify
from .extensions import db
from .models import User, Stock
from . import create_app

# import yfinance to make api calls
import yfinance as yf

# to hash password 
import hashlib

# to allow access to the react frontend 
from flask_cors import CORS, cross_origin

app = create_app()

# Only global variable to have user 
current_user = -1

# Test path to make sure flask is working correctly
@app.route('/')
def test():
    return {
        "german Loves flask": "and react"
    }

# The first route will keep track of the user to know what to insert into the database 
@app.route('/login', methods=['POST'])
def login():
    
    if request.method == 'POST':

        # get the data from the frontend 
        data = request.get_json()

        # Handle login form submission here
        email = request.form['username']
        unhashed_password = request.form['password']

        # make sure to hash it to match database value 
        hashed_password = hashlib.sha256(unhashed_password.encode()).hexdigest()
        
        # check if the user exists in the database and if the password is correct
        user = User.query.filter_by(email=email).first()
        password = User.query_filter_by(password=hashed_password).first()
        if user and password:
            session['user_id'] = user.id
            current_user = user.id 

        else:
            # Handle invalid login
            return "Login Unsuccessful."
      
    return jsonify({
        "username": email,
        "password": password,
        "data": data
    }), 200, {'Access-Control-Allow-Origin': 'http://localhost:3000'}

@app.route('/logout')
def logout():
    # Remove the user_id from the session
    session.pop('user_id', None)
    return "Log out successful."

# this function checks to see if there is indeed a user logged in 
@app.route('/check-login', methods=['GET'])
def check_login():
    user = session.get('user_id')
    if user:
        return {'isLoggedIn': True}
    else:
        return {'isLoggedIn': False}

# this function will serve as a query for specific stocks 
@app.route("/query_stock", method=['POST'])
def get_stock():
    ''' for the purpose of this application, we will return:
        ticker_name: (Apple Inc., etc...)
        ticker_quantity (shares outstanding): (2, 34, etc...)
        ticker_price: (134.21, 0.51, etc...)
        ticker_sector: (Technology, etc...)
        ticker_summary: description
    '''
    data = request.get_json()

    # get a request from the react frontend
    stock = data['query']

    api_call = yf.Ticker(stock)

    # make request through yfinance
    name = api_call.info['shortName']
    shares_outstanding = api_call.info['sharesOutstanding']
    price = api_call.info['currentPrice']
    sector = api_call.info['sector']
    summary = api_call.info['longBusinessSummary']

    return jsonify({
        "ticker_name": name,
        "ticker_quantity": shares_outstanding,
        "ticker_price": price,
        "ticker_sector": sector,
        "ticker_summary": summary
    }), 200, {'Access-Control-Allow-Origin': 'http://localhost:3000'}

# this function will serve as buying stocks and storing in the database 
@app.route("/api/buy_stock", method=['POST'])
def store_stock():
    ''' for the purpose of this application, we will store:
        ticker_name: (Apple Inc., etc...)
        ticker_quantity (shares outstanding): (2, 34, etc...)
        ticker_price: (134.21, 0.51, etc...)
        total_purchase: (1100.12, etc...)
    '''
    # get user
    user = current_user

    # get the variables from the frontend 
    stock = request.get_json['ticker']
    amount = request.get_json['shares']

    api_call = yf.Ticker(stock)
    
    # make request through yfinance
    name = api_call.info['shortName']
    shares_outstanding = amount
    price = api_call.info['currentPrice']

    # handle the case where the stock is already in the database 
     if Stock.query.filter_by(user_id=user, ticker_name=name).scalar() is not None:
         # increment the shares to add more
         present_shares = Stock.query.filter(and_(Stock.user_id == user, Stock.ticker_name == name)).with_entities(Stock.ticker_quantity).all()
         shares_outstanding = shares_outstanding + present_shares

    # Add to the database 
    new_ticker = Stock(ticker_name = name, ticker_quantity = shares_outstanding, ticker_price = price, user_id = user)

    # add the new Stock to the database
    db.session.add(new_ticker)

    # commit the change to the database
    db.session.commit()
        
    return "Success. Ticker added."

# this function will retrieve the stocks in the portfolio 
@app.route("/api/portfolio", methods=['POST'])
def get_tickers():

    # Initialize three list to append values 
    name = []
    shares_outstanding = []
    price = []

    # get user id 
    user = 1

    # get the filtered entries based on the user
    filtered_entries = Stock.query.filter_by(user_id=user).all()
    
    for entry in filtered_entries:
        name.append(entry.ticker_name)
        shares_outstanding.append(entry.ticker_quantity)
        price.append(entry.ticker_price)

    return jsonify({
        "name": name,
        "shares": shares_outstanding,
        "prices": price
    }), 200, {'Access-Control-Allow-Origin': 'http://localhost:3000'}