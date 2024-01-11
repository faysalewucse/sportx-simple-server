#  @bekbrace
#  FARMSTACK Tutorial - Sunday 13.06.2021

# Pydantic allows auto creation of JSON Schemas from models
import uuid
from pydantic import BaseModel, Field
from typing import List, Union, Optional


class Game(BaseModel):
    id: str
    chart_type: str
    gid: str
    game_time: str
    game_date: str
    team: str
    sp_name: str
    sp_id: Union[int, str]
    sp_id2: str
    League: str
    Handed: str
    age: str
    height: str
    weight: str
    career_inn: str
    wx_record: str
    A_1: str
    A_2: str
    Blurb: str
    GS: Union[int, str]
    y_arr: str
    bar_color: str
    awx: Union[float, str]
    twx: Union[int, str]
    cy_p: float
    x_arr: str
    awx_arr: str
    mov_ave_arr: str
    homepage_x: str
    Cy_rank_league: Optional[Union[int, str]] = None
    Cy_rank_overall: Optional[int] = None
    Trade_data: Union[list[Union[str, int]], str]
    sctr_arr: List[Union[str, int]]

