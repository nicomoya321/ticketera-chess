from app.routes import auth # pyright: ignore[reportMissingImports]
def app():
    from fastapi import FastAPI
    from app.routes import tickets # pyright: ignore[reportMissingImports]
    from app.database import engine, Base ,get_db # pyright: ignore[reportMissingImports]

    Base.metadata.create_all(bind=engine)

    app = FastAPI()

    app.include_router(tickets.router)

app.include_router(auth.router) 