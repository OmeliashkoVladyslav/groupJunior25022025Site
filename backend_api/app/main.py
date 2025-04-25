from app_factory import get_application

app = get_application()

@app.get('/')
async def index():
    return {'status2332': 200}
