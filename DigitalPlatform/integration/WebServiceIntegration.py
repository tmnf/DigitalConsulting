# This class will handle requests to a webservice

def send_data_to_webservice(request, data, webservice):
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    post = request.post(webservice, data=data, headers=headers)

    return post.content
