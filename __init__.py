from fastapi import APIRouter, Body, Depends
from sqlalchemy.orm import Session

from app.core.module_class import TableModule, ApiModule
from app.core.table_class.db_core import get_db
from app.modules.sample.table import SampleTable


class Sample(ApiModule, TableModule):
    def _register_api_bp(self, bp: APIRouter):
        @bp.get('/description')
        def description():
            return 'this is a sample module_manager description,' \
                   ' this sample will tell you how to' \
                   ' create a module_manager for Figbox'

        @bp.post('/show_body')
        def show_body(body: str = Body(..., embed=True)):
            return f'your body is: {body}'

        @bp.post('/create', description='create data to table')
        def create(db: Session = Depends(get_db), data: str = Body(..., embed=True)):
            """create data into the table"""
            data = SampleTable(data=data)
            data.create_stamp()
            db.add(data)
            db.commit()
            return data

        @bp.get('/read', description='read data from table')
        def read(db: Session = Depends(get_db)):
            """read data from table"""
            return db.query(SampleTable).all()

        @bp.put('/update', description='update')
        def update(id: int, db: Session = Depends(get_db), data: str = Body(..., embed=True)):
            sample_data: SampleTable = db.query(SampleTable).filter(SampleTable.id == id).first()
            sample_data.data = data
            sample_data.update_stamp()
            db.commit()
            return sample_data

        @bp.delete('/delete', description='delete a data')
        def delete(id: int, db: Session = Depends(get_db)):
            db.query(SampleTable).filter(SampleTable.id == id).delete()
            db.commit()
            return {}

        # 任意なプレフィックスを作成する為
        abc_bp = self._register_free_prefix('/abc', 'abc')

        @abc_bp.get('/sample', description='you used a free prefix')
        def abc_sample():
            return 'you used a free prefix'

    def get_table(self) -> list:
        return [SampleTable]

    def _get_tag(self) -> str:
        return 'サンプルモジュール'

    def get_module_name(self) -> str:
        return 'sample'


sample = Sample()
