from flask import Flask, request, jsonify
import base64
from PIL import Image
from io import BytesIO
from flask_cors import CORS
import zxing  # Import zxing for barcode scanning

app = Flask(__name__)
CORS(app)  # Enable CORS for the entire app

@app.route('/send-image', methods=['POST'])
def send_image():
    try:
        # Get the base64 encoded image string from the POST request
        data = request.json
        base64_image_string = data.get('base64')

        # Check for base64 image string
        if not base64_image_string:
            raise ValueError("No image data provided")

        # Decode base64 image string
        image_data = base64.b64decode(base64_image_string)

        # Open the image using PIL (Pillow)
        image = Image.open(BytesIO(image_data))

        # Save the image to the server
        image_path = "decoded_image.jpg"
        image.save(image_path)

        # Scan the image for barcode data
        reader = zxing.BarCodeReader()
        barcode = reader.decode(image_path)
        if barcode:
            decoded_text = barcode.parsed
            # Process the decoded text to change the format
            processed_text = process_decoded_text(decoded_text)
        else:
            processed_text = "No barcode found."

        return jsonify({'message': 'Image successfully saved.', 'decodedText': processed_text}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

def process_decoded_text(decoded_text):
    # Assuming the format of the input is consistent
    parts = decoded_text.split()
    # Example format: [ID, Name1&Name2, Nationality, DOB, Gender, ID Number, Issue Date, Expiry Date, Authority]
    # Adjust indices according to your specific format
    formatted_parts = [
        parts[0],                  # ID
        parts[1],
        parts[2], # Name (concatenated words are separated)
        parts[3],                  # Nationality
        '.'.join(parts[4:7]),      # Date of Birth (combining multiple parts)
        parts[7],                  # Gender
        parts[8],                  # ID Number
        '.'.join(parts[9:12]),     # Issue Date
        '.'.join(parts[12:15]),    # Expiry Date
        parts[15]                  # Authority
    ]
    return ','.join(formatted_parts)

@app.route('/message', methods=['GET'])
def get_message():
    return jsonify({'message': "Hello, this is a test message!"})

if __name__ == '__main__':
    d = {'PARTIDUL DEMOCRAT DIN MOLDOVA':501, 'BLOCUL ELECTORAL”ACUM PLATFORMA DA SI PAS”': 40}
    app.run(debug=True)
