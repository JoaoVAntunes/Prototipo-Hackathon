#file to manipulate the creation and manipulation of the data base.
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy() #incialize the data base variable, will be used on all the db files

instance = f"mysql+pymysql://root:vV9C3y9hjS0si2E@localhost:3306/crea_db"
