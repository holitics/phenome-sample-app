# sample_app.py, Copyright (c) 2019, Phenome Project - Nicholas Saparoff <nick.saparoff@gmail.com>

import time

from sqlalchemy.exc import IntegrityError
from phenome_core.core.base.logger import root_logger as logger
from phenome_core.core.database.db import db_session
from phenome_core.core import ui
from phenome_core.core.database.model.object import Object
from phenome_core.core.constants import  _API_ERROR_CODES_, _API_ERROR_MESSAGES_

from phenome_core.core.database.model.api import get_object_by_id, get_object_by_ip, delete_object

from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    jsonify
)

# define the blueprint for the sample_app phenome
sample_app = Blueprint('sample_app', __name__, template_folder='./templates')


@sample_app.route('/')
def home():
    return hello_world()


@sample_app.route('/helloworld')
def hello_world():

    logger.debug("/helloworld:" + request.remote_addr)

    # render a simple helloworld template in ./templates folder
    return render_template('helloworld.html', version='0.0')


@sample_app.route('/info')
def info():
    # return the internal "info" screen (uses ./templates/info.html )
    return ui.info()


@sample_app.route('/status')
def status():
    # return the internal "status" screen (uses ./templates/status.html )
    return ui.status()


@sample_app.route('/messages')
def messages():
    # return the internal "messages" screen (uses ./templates/messages.html )
    return ui.messages()


@sample_app.route('/object_dialog/<id>/<header_only>/<show_details>')
def object_dialog(id, header_only, show_details):
    # allows object dialog display (called from the status screen)
    return ui.object_dialog(None, id, header_only, show_details)


@sample_app.route('/update_object_properties', methods=['POST'])
def update_object_properties():
    # allows object properties to be updated (called from the object dialog template)
    return ui.update_object_properties(request)


