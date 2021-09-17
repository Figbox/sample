from fastapi import APIRouter, Body

from app.core.module_class import TableModule, ApiModule


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

        # 任意なプレフィックスを作成する為
        abc_bp = self._register_free_prefix('/abc', 'abc')

        @abc_bp.get('/sample', description='you used a free prefix')
        def abc_sample():
            return 'you used a free prefix'

    def get_table(self) -> list:
        return []

    def _get_tag(self) -> str:
        return 'サンプルモジュール'

    def get_module_name(self) -> str:
        return 'sample'


sample = Sample()
