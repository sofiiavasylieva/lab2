import databases
import sqlalchemy
from sqlalchemy import Table, Column, String, Integer, create_engine, MetaData

DATABASE_URL = "mysql+pymysql://root:user1@localhost:3306/dbtest"

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

users = Table(
    "py_users",
    metadata,
    Column("id", String(255), primary_key=True),
    Column("username", String(255)),
    Column("password", String(255)),
    Column("first_name", String(255)),
    Column("last_name", String(255)),
    Column("gender", String(10)),
    Column("create_at", String(255)),
    Column("status", String(10)),
)


engine = sqlalchemy.create_engine(
    DATABASE_URL
)
metadata.create_all(engine)
