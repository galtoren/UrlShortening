from sqlalchemy import create_engine, MetaData, Table, Column, String

DATABASE_URL = "sqlite:///./test.db"
mysql_db = create_engine(DATABASE_URL)
metadata = MetaData()

url_mappings = Table(
    "url_mappings",
    metadata,
    Column("shorter_url", String(8), primary_key=True),
    Column("origin_url", String(500)),
)

metadata.create_all(mysql_db)
