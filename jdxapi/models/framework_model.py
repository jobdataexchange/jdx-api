from jdxapi.app import DB
# import re
from flask_sqlalchemy import SQLAlchemy
from jdxapi.models.lookup_single_decorator import lookup_single_error_handler
from sqlalchemy import Integer, String, DateTime, Numeric, Column, func, Text, ForeignKey
from sqlalchemy.orm import validates, relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import text as sa_text
from uuid import uuid4, uuid5, NAMESPACE_DNS

def frame_id_default(context):
    framework_name = context.get_current_parameters()['framework_name']
    lol = uuid4()
    lol2 = uuid5(NAMESPACE_DNS, framework_name)
    print(lol, lol2)
    return lol2

class Framework(DB.Model):
    __tablename__ = 'framework'

    framework_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=frame_id_default
    )

    framework_type_id = Column(Integer, ForeignKey('framework_type.framework_type_id'))
    framework_type = relationship("FrameworkType")

    framework_name = Column(String, unique=True)
    framework_description = Column(String)
    framework_uri = Column(String)
    
    @classmethod
    @lookup_single_error_handler('framework_id')
    def get_framework_from_id(self, framework_id):
        framework_query = DB.session.query(Framework).filter_by(framework_id=framework_id)
        framework = framework_query.one()
        return framework

class FrameworkType(DB.Model):
    __tablename__ = 'framework_type'

    framework_type_id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    framework_type = Column(String)


