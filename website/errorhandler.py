from flask import Blueprint, flash, redirect, request
from werkzeug import exceptions

errorhandler_mold = Blueprint('errorhandler', __name__)


@errorhandler_mold.app_errorhandler(exceptions.RequestEntityTooLarge)
def request_entity_too_large(e):
    flash('File too large.', category='error')
    return redirect(request.url)


@errorhandler_mold.app_errorhandler(exceptions.NotFound)
def not_found(e):
    return redirect('/error-pages/404')
