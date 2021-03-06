import logging

logger = logging.getLogger('flask_Roger')
logger.addHandler(logging.StreamHandler())
if logger.level == logging.NOTSET:
    logger.setLevel(logging.WARN)
    
log = logging.getLogger('flask_Roger')
log.addHandler(logging.StreamHandler())
if log.level == logging.NOTSET:
    log.setLevel(logging.WARN)


from .core import (
    Ask,
    request,
    session,
    version,
    context,
    current_stream,
    convert_errors
)

from .models import (
    question,
    statement,
    audio,
    delegate,
    elicit_slot,
    confirm_slot,
    confirm_intent
)
