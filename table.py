from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime

from app.core.table_class import DateCreateUpdateTable


# see https://fastapi.tiangolo.com/tutorial/sql-databases/
class SampleTable(DateCreateUpdateTable):
    __tablename__ = 'sample'
    data = Column(String(250))
