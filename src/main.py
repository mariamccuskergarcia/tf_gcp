import functions_framework
import sys
from degrees_of_kb import KevinBacon6Degrees 

@functions_framework.http
def hello_http(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """
    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and 'wiki_page_id' in request_json:
        wiki_page_id = request_json['wiki_page_id']
        sixdegrees = KevinBacon6Degrees(wiki_page_id)
        sixdegrees.generate_6_degrees()
    elif request_args and 'wiki_page_id' in request_args:
        wiki_page_id = request_args['wiki_page_id']
        sixdegrees = KevinBacon6Degrees(wiki_page_id)
        sixdegrees.generate_6_degrees()
    return sixdegrees.get_summary_as_json()
