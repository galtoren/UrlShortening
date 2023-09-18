from sqlalchemy import create_engine, MetaData, Table, Column, String

DATABASE_URL = "sqlite:///./test.db"
mysql_db = create_engine(DATABASE_URL)
metadata = MetaData()

users = Table(
    "url_mappings",
    metadata,
    Column("id", String(50), primary_key=True),
    Column("origin_url", String(500)),
    Column("shorter_url", String(100)),
)

metadata.create_all(mysql_db)
