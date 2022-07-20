from fastapi import FastAPI

app = FastAPI(debug=True) # represents our api application

from orders.api import api
