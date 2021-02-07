from flask_swagger import swagger
from flask import jsonify, Blueprint, current_app

docs = Blueprint('docs', __name__, url_prefix='/docs')

# @docs.route('/')
# def doc():
#     return docs.send_static_file('index.html')

# Route to access API Swagger specifications => needs to access `app`
@docs.route('/swagger')
def swagger_spec():
    swag = swagger(current_app)
    # See http://swagger.io/specification/ for more information
    swag['basePath'] = current_app.config['SWAGGER_BASE_PATH']
    swag['info']['title'] = "Digiez Assessment API"
    return jsonify(swag)
