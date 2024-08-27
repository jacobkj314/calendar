from flask import Flask, request, redirect, render_template, render_template_string, url_for, flash, get_flashed_messages, jsonify, send_from_directory
from flask_socketio import SocketIO, join_room, leave_room

from sys import argv

app = Flask(__name__)
socketio = SocketIO (
                        app, 
                        **(
                            {} 
                            if ("debug" in argv) else 
                            {"async_mode":"gevent"}
                        )
                    )





if __name__ == '__main__':
    if "debug" in argv:
        socketio.run(app, host='0.0.0.0', port=7074, debug=True)
    else:
        from gevent.pywsgi import WSGIServer
        WSGIServer(("0.0.0.0", 7074), app).serve_forever()