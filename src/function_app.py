import azure.functions as func
import logging
import os
import pyodbc
import product as p
import json
import logging
from azure.functions.decorators.core import DataType
import uuid

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)
@app.route(route="InsertName")
@app.generic_output_binding(arg_name="toDoItems", type="sql", CommandText="dbo.ToDo", ConnectionStringSetting="SqlConnectionString",data_type=DataType.STRING)
def test_function(req: func.HttpRequest, toDoItems: func.Out[func.SqlRow]) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")
    name = req.get_json().get("name")
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get("name")
    if name:
        toDoItems.set(func.SqlRow({"Id": str(uuid.uuid4()), "title": name, "completed": False, "url": ""}))
        return func.HttpResponse(f"Hello {name}!")
    else:
        return func.HttpResponse(
                    "Please pass a name on the query string or in the request body",
                    status_code=400
                )


# やつ
# @app.route(route="GetProduct")
# def GetProduct(req: func.HttpRequest) -> func.HttpResponse:
#     logging.info('Python HTTP trigger function processed a request.')

#     name = req.params.get('name')
#     if not name:
#         try:
#             req_body = req.get_json()
#         except ValueError:
#             pass
#         else:
#             name = req_body.get('name')

#     if name:
#         return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
#     else:
#         return func.HttpResponse(
#              "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
#              status_code=200
#         )


# vscodeから動いたやつ
# @app.route(route="hello", auth_level=func.AuthLevel.ANONYMOUS)
# @app.generic_output_binding(arg_name="toDoItems", type="sql", CommandText="dbo.ToDo", ConnectionStringSetting="SqlConnectionString",data_type=DataType.STRING)
# def test_function(req: func.HttpRequest, toDoItems: func.Out[func.SqlRow]) -> func.HttpResponse:
#     logging.info('Python HTTP trigger function processed a request.')
#     name = req.get_json().get('name')
#     if not name:
#         try:
#             req_body = req.get_json()
#         except ValueError:
#             pass
#         else:
#             name = req_body.get('name')
#     if name:
#         toDoItems.set(func.SqlRow({"Id": str(uuid.uuid4()), "title": name, "completed": False, "url": ""}))
#         return func.HttpResponse(f"Hello {name}!")
#     else:
#         return func.HttpResponse(
#                     "Please pass a name on the query string or in the request body",
#                     status_code=400
#                 )

# とってくる========================================
    # id = req.params.get('id')
    # if id:
    #     connectionString = os.environ['SqlConnectionString']
    #     query = "select" \
    #                 " p.ProductID," \
    #                 " pc.Name as CategoryName," \
    #                 " p.Name as ProductName," \
    #                 " p.Color," \
    #                 " p.StandardCost," \
    #                 " p.SellStartDate " \
    #                 "from [SalesLT].[Product] p" \
    #                 " inner join [SalesLT].[ProductCategory] pc on p.ProductCategoryID = pc.ProductCategoryID" \
    #                 f" where pc.ProductCategoryId = {id}"
    #     with pyodbc.connect(connectionString) as conn:
    #         with conn.cursor() as cursor:
    #             cursor.execute(query)
    #             rows = cursor.fetchall()
    #             products = []
    #             for row in rows:
    #                 products.append(json.dumps(vars(p.Product(row.ProductID, row.CategoryName, row.ProductName, row.Color, row.StandardCost, row.SellStartDate))))
    #             return func.HttpResponse(str(products), status_code=200, headers={"Content-Type": "application/json; charset=utf-8"})
    # else:
    #     return func.HttpResponse("Please pass a valid id on the query string", status_code=400, headers={"Content-Type": "application/json; charset=utf-8"})


# とってくる========================================
# import azure.functions as func
# import logging
# from azure.functions.decorators.core import DataType
# import uuid

# app = func.FunctionApp()

# @app.function_name(name="HttpTrigger1")
# @app.route(route="hello", auth_level=func.AuthLevel.ANONYMOUS)
# @app.generic_output_binding(arg_name="toDoItems", type="sql", CommandText="dbo.ToDo", ConnectionStringSetting="SqlConnectionString",data_type=DataType.STRING)
# def test_function(req: func.HttpRequest, toDoItems: func.Out[func.SqlRow]) -> func.HttpResponse:
#      logging.info('Python HTTP trigger function processed a request.')
#      name = req.get_json().get('name')
#      if not name:
#         try:
#             req_body = req.get_json()
#         except ValueError:
#             pass
#         else:
#             name = req_body.get('name')

#      if name:
#         toDoItems.set(func.SqlRow({"Id": str(uuid.uuid4()), "title": name, "completed": False, "url": ""}))
#         return func.HttpResponse(f"Hello {name}!")
#      else:
#         return func.HttpResponse(
#                     "Please pass a name on the query string or in the request body",
#                     status_code=400
#                 )