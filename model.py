import uuid
from pydantic import BaseModel, Field
from typing import List, Union, Optional


class Game(BaseModel):
    id: str
    chart_type: str
    sea: int
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
    Plyr_fields: List[Union[str, int]]

