from flask import Flask, request, jsonify, send_from_directory
import util

app = Flask(__name__, static_folder='.')

@app.route('/')
def serve_app():
    return send_from_directory('.', 'app.html')

@app.route('/classify_image', methods=['POST'])
def classify_image():
    try:
        image_data = request.form['image_data']
        if not image_data:
            return jsonify({"error": "No image data provided"}), 400

        response_data = util.classify_image(image_data)
        response = jsonify(response_data)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    print("Starting Python Flask Server For Sports Celebrity Image Classification")
    util.load_saved_artifacts()
    app.run(port=5000)
