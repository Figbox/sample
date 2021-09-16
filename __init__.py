from fastapi import APIRouter, Body

from app.models.module import ApiModule, TableModule


class Sample(ApiModule, TableModule):
    def _register_api_bp(self, bp: APIRouter):
        @bp.get('/description')
        def description():
            return 'this is a sample module description,' \
                   ' this sample will tell you how to' \
                   ' create a module for Figbox'

        @bp.post('/show_body')
        def show_body(body: str = Body(..., embed=True)):
            return f'your body is: {body}'

    def get_table(self) -> list:
        return []

    def _get_tag(self) -> str:
        return 'サンプルモジュール'

    def get_module_name(self) -> str:
        return 'sample'
