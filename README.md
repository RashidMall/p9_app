# Article Recommendation Web App

This is a simple Flask-based web application for receiving article recommendations for users. The application interacts with a remote API server that provides personalized article recommendations based on user IDs.
https://openclassrooms-p9-app-6b76a5f33f7a.herokuapp.com/
## Usage
1. Make sure you have Python and Flask installed on your system.

2. Clone the repository to your local machine.

3. Open the terminal and navigate to the project directory.

4. Run the Flask application using the following command:
```bash
python app.py
```
5. Access the application in your web browser by navigating to `http://127.0.0.1:5050/`.

## Functionality  
The web application has the following main features:  
1. __Homepage__: The homepage provides a simple form where users can enter their user ID.  
2. __Recommendations Page__: After submitting the user ID, the application sends a request to a remote API server that calculates and returns a list of recommended articles for the user.  
3. __Display Recommendations__: The recommendations are displayed to the user, and they can explore the recommended articles.  

## Configuration
To use this application in a production environment, you may need to configure the `SERVER_URL` variable in the `app.py` file to point to your remote recommendation server.  
```python
# URL of the remote API server for article recommendations.
SERVER_URL = "https://your-remote-server-url-here.com/api/rec_articles?user_id="
```

Ensure that the server provides recommendations in the expected format.
