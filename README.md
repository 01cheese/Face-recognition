# Celebrity Image Classification Service

![image](https://github.com/01cheese/Face-recognition/assets/115219323/dff8335b-584a-4238-81ee-508e84c54fb6)

This project implements a web service for celebrity image classification. The web application is built using Flask on the backend and HTML/JavaScript on the frontend.

## Project Structure

- `artifacts/` - Contains model artifacts such as `class_dictionary.json` and `saved_model.pkl`.
- `opencv/` - Contains Haar cascade files for face and eye detection.
- `UI/` - Contains frontend files.
  - `images/` - Folder for storing celebrity images.
  - `test_images/` - Folder for test images.
  - `app.css` - Styles for the web application.
  - `app.html` - HTML file for the frontend.
  - `app.js` - JavaScript file for the frontend.
  - `dropzone.min.css` and `dropzone.min.js` - Dropzone library for image upload.
- `b64.txt` - File containing an image in base64 format.
- `main.py` - Main Flask application file.
- `requirements.txt` - List of project dependencies.
- `util.py` - Utility functions for image processing and classification.
- `wavelet.py` - Functions for image transformation using wavelets.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/AI_FOTO.git
    cd AI_FOTO
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # For Windows: .venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:
    ```bash
    python main.py
    ```

The application will be accessible at `http://127.0.0.1:5000/`.

## Usage

1. Open your browser and go to `http://127.0.0.1:5000/`.
2. Upload a celebrity image through the Dropzone interface.
3. Click the "Classify" button to classify the image.
4. The result will be displayed on the page.

## Code Structure

### `main.py`
Main Flask application file. Contains routes for loading the main page and handling image classification requests.

### `util.py`
Contains utility functions for loading the model, processing images, and performing classification.

### `wavelet.py`
Contains a function for transforming images using wavelets.

## Notes

- Ensure that the `opencv/haarcascades/` folder contains `haarcascade_frontalface_default.xml` and `haarcascade_eye.xml` files necessary for face and eye detection.
