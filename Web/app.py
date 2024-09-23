from flask import Flask
from flask_socketio import SocketIO
from routes import register_routes

app = Flask(__name__)
socketio = SocketIO(app)

# Register Blueprints
register_routes(app)

if __name__ == '__main__':
    socketio.run(app, debug=True)
