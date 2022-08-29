from fastapi import FastAPI
from pydantic import BaseModel

import load_env as _envs

app = FastAPI()

class UserInterest(BaseModel):
    views : dict[int, int]


@app.get('/test')
async def testRoute():
    return {'test': 'Hello World From Content-Filter-Services'}


@app.post('/')
async def getRoomRecommend(datas: UserInterest):
    '''
    This function is : f(a) = b 
    where [a] is Dict of [topic_ID : views_count]
    and [b] is Dict of [topic_ID : recommend_amount]
    '''
    _datas = datas.views
    _sum = sum(_datas.values())
    for k, v in _datas.items():
        _datas[k] = round((v/_sum) * 10)
    return _datas


if __name__ == '__main__':
    import uvicorn

    PORT = int(_envs.PORT)
    uvicorn.run("main:app", port=PORT, host='0.0.0.0', reload=True)