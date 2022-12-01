
# The code starts by importing the FastAPI library.
from fastapi import FastAPI
#The app variable is then set to point to the FastAPI object that was imported.
app=FastAPI()
#The code then calls a function called first_api which returns an object with a message property and no other properties.
@app.get("/")
async def first_api():
    return{'msg':'hellow saror'}


