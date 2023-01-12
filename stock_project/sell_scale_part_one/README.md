# Intructions for Getting the Website Running

### Step 1: Get the virtual environment running
    $ source virtualenv/bin/activate
    > **Troubleshooting**: If this virtual environment is acting weird, you may need to run the following steps:

    $ pip3 install virtualenv
    $ ~/.pyenv/versions/3.6.5/bin/python3 -m venv virtualenv

### Install axios, the library that will allow connections between Flask and React
    $ npm i axios
    > Make sure this is done in the myapp directory, ~/sell_scale_part_one/react_frontend/myapp

### Install react-router-dom, the library to redirect between pages 
    $ npm install react-router-dom
    > Make sure this is done in the myapp directory, ~/sell_scale_part_one/react_frontend/myapp

### Run pip requirements to get all dependencies 
    $ pip3 install requirements.txt
    > In the home directory, ~/sell_scale_part_one

### There will be two environment variables to set:
    $ export FLASK_APP=backend_api
    $ export FLASK_ENV=development

### To run the backend (must go before the frontend), run the following in ./sell_scale_part_one directory:
    $ flask run 
    > After running `flask run`, the database should be created. If you want to manually play with the database, run the following in the home directory. 
    $ sqlite3 instance/db.stockdatabase

### Now to start the frontend, run the following in ./sell_scale_part_one/react_frontend/my-app
    $ npm start 

### Once in the website, it's important to note that I have created a user, use the following information:
    > **username**: aakash_adesara, **password**: sellscale_for_life$
    > Important Note: username = email for the purposes of this application.

# Weird Error with Axios
    > Although I will mention this to Aakash upon turning in, it's important to note that I had problems with axios. Although I thought it was weird since I had used axios the day before for another project I've been working on, it was completely blocked on all of my projects. My guess is that it isn't related to how I am implementing axios, but an external issue with a browser blocking my use through CORS. This unfortunately means that I wasn't able to test any of the connection between the flask backend and the react frontend, although I did my best to simulate how I would do it. If there are any questions at all, please feel free to reach out. I sincerely apologize for this weird error. Thank you and I hope you enjoy the project. 

# Another Note Regarding App.js and App2.js
    > Because I wasn't able to test with axios, I couldn't test the login functionality of the application. Because of this, I couldn't render the StockPage component in my project, so I decided to put everything onto the App.js to show the work I did, however, App2.js shows how I would have implemented it had I had the chance to work with axios and get the login working. Again, I sincerely apologize for this occurence. Nonetheless, I hope you enjoy reading through my thought process for the project!