from fastapi_admin.app import FastAPIAdmin as admin_app
from fastapi_admin.app  import ModelResource
from fastapi_admin.resources import Field


from app.models.curator import Curator




 # Ресурс для Curator
@admin_app.register
class CuratorResource(ModelResource):
    label = "Curator"
    page_pre_title = "Curator list"
    page_title = "Curator Model"
    model=Curator,
    fields = [
        "id",
        "station"
        "user"
    ] 
    
    # Ресурс для PlayerTeam
    admin_app.add_resource(Model(
        model=PlayerTeam,
        fields=[
            "id",
            Field(name="name", label="Name", input_=inputs.Text()),
            Field(name="score", label="Score", input_=inputs.Number()),
            # Добавьте другие поля
        ],
    ))
    
    # Ресурс для Station
    admin_app.add_resource(Model(
        model=Station,
        fields=[
            "id",
            Field(name="name", label="Name", input_=inputs.Text()),
            # Добавьте другие поля
        ],
    ))
    
    # Ресурс для StationOrder
    admin_app.add_resource(Model(
        model=StationOrder,
        fields=[
            "id",
            Field(name="order", label="Order", input_=inputs.Number()),
            # Добавьте другие поля
        ],
    ))
    
    # Ресурс для Task
    admin_app.add_resource(Model(
        model=Task,
        fields=[
            "id",
            Field(name="title", label="Title", input_=inputs.Text()),
            Field(name="description", label="Description", input_=inputs.Textarea()),
            # Добавьте другие поля
        ],
    ))