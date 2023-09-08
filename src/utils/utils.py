import orjson
from fastapi import Response
from typing import Any

from pydantic import BaseModel
class CustomORJSONResponse(Response):
    media_type = "application/json"

    def render(self, content: Any) -> bytes:
        assert orjson is not None, "orjson must be installed"
        return orjson.dumps(content, option=orjson.OPT_INDENT_2)
    

# cach khac
def orjson_dumps(v: Any)-> str:
    return orjson.dumps(v,option=orjson.OPT_INDENT_2)
class ORJSONModel(BaseModel):
    class Config:
        json_loads = orjson.loads
        json_dumps = orjson_dumps
        allow_population_by_field_name = True
    
        