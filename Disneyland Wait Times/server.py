import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/location', methods=['GET', 'POST'])
def location():
    try:
        if request.method == 'POST':
            data = request.get_json()
            if not data:
                return jsonify({'error': 'No JSON data received'}), 400

            latitude = data.get('latitude')
            longitude = data.get('longitude')

            if latitude is None or longitude is None:
                return jsonify({'error': 'Missing latitude or longitude'}), 400

            try:
                latitude = float(latitude)
                longitude = float(longitude)
            except ValueError:
                return jsonify({'error': 'Invalid latitude or longitude (must be numbers)'}), 400

            print(f"Received Location (POST) - Latitude: {latitude}, Longitude: {longitude}")

            if 33.80 <= latitude <= 33.82 and -117.92 <= longitude <= -117.90:
                return jsonify({"status": "inside Disneyland"})
            else:
                return jsonify({"status": "outside Disneyland"})

        elif request.method == 'GET':
            return jsonify({'message': 'Send a POST request with latitude and longitude'}), 200

    except Exception as e:
        print(f"Error checking location: {e}")
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
