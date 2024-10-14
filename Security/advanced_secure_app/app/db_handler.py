import logging
from app.models import Log
from app.extensions import db
from datetime import datetime


class DBHandler(logging.Handler):
    def emit(self, record):
        log_entry = Log(
            user_id=getattr(record, 'user_id', None),
            action=record.getMessage(),
            timestamp=datetime.utcnow()
        )
        db.session.add(log_entry)
        db.session.commit()
