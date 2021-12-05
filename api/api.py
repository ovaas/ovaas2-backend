from ninja_extra import NinjaExtraAPI
from ninja_jwt.controller import NinjaJWTDefaultController
from ovaas.api import router as ovaas_router

api = NinjaExtraAPI(title='OVAAS Backend API', version='0.1', description='OVAAS 2 backend api docs')

api.register_controllers(NinjaJWTDefaultController)

api.add_router("api/v1", ovaas_router)
