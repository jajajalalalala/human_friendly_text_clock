from datetime import datetime
from flask import Flask, jsonify
from flask_restful import Resource, Api
import HumanFriendlyTextClock as clock

app = Flask(__name__)

api = Api(app)


@app.route('/', methods=['GET'])
def home():
    time = datetime.now().strftime("%H:%M")
    return jsonify({time: clock.get_human_friendly_text(time)})


class HumanClockAPI(Resource):
    def get(self, time):
        time = str(time)
        return jsonify({time: clock.get_human_friendly_text(time)})


api.add_resource(HumanClockAPI, '/<time>')

if __name__ == '__main__':
    app.run(debug=True)
