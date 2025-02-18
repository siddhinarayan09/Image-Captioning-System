from flask import Flask, jsonify
from app.controllers.api_Handler import api_handler


def create_app():
    # Create Flask app
    app = Flask(__name__)

    # Register blueprints
    app.register_blueprint(api_handler, url_prefix='/api_handler')

    # health check endpoint
    @app.route('/', methods=['GET'])
    def health_check():
        return jsonify(message="Welcome to the Image Caption Generating System")
    
    @app.route('/health', methods=['GET'])
    def health():
        return jsonify(message="Health is OK")
    return app
