from datetime import datetime, timedelta
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Boolean, Integer, String, DateTime,Float

from ..database import db
from ..mixins import CRUDModel

class Rychlost(CRUDModel):
    __tablename__ = 'rychlost'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True )
    SPZ = Column(Integer, nullable=False, index=False)#1=hovezi,2=vepr,3=kure
    rychlost = Column(Integer, nullable=False, index=True)#1=predni,2=zadni
    # Use custom constructor
    # pylint: disable=W0231
    def __init__(self, **kwargs):
        for k, v in kwargs.iteritems():
            setattr(self, k, v)
