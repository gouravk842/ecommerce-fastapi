import fastapi
import uvicorn

from src.ecommerce.controller.order import order_router
from src.ecommerce.controller.product import product_router
from src.app_config import AppConfig
from src.user.controller import user_router

app = fastapi.FastAPI()
app_config = AppConfig(dev_mode=True)  # Create the AppConfig instance


# main function to run the application
def main():
    configure(app_config)
    uvicorn.run(app, host='127.0.0.1', port=8000)


# do all the configuration here
def configure(app_config: AppConfig):
    configure_templates()
    configure_routes()
    configure_db(app_config)


# Initialize the templates
def configure_templates():
    pass


# Initialize the routes from different modules
def configure_routes():
    app.include_router(product_router)
    app.include_router(order_router)
    app.include_router(user_router)


# Initialize the database
def configure_db(app_config: AppConfig):
    app.db = app_config.db_manager.get_database()


# entry point of the application
if __name__ == '__main__':
    main()
