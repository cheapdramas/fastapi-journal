from fastapi import FastAPI
import uvicorn
from routes.gets.get_routes import router as router_get
from routes.posts.post_routes import router as router_post
from api.api import router as router_api






app = FastAPI()

app.include_router(router_get)
app.include_router(router_post)
app.include_router(router_api)




if __name__ == '__main__':

    uvicorn.run('app:app',reload=True,port=30000)