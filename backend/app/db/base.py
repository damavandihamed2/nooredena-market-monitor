from sqlalchemy.orm import declarative_base

Base = declarative_base()

from app.models.fda import *
from app.models.iee import *
from app.models.ime import *
from app.models.otp import *
from app.models.tsetmc import *
from app.models.user import *


