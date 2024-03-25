import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="generateResponse2")
def generateResponse2(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP-triggered function generateResponse2() processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP-triggered function generateResponse2() executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP-triggered function generateResponse2() executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )