import requests
import json

class IceAndFireAPI:
    url_endpoint = "https://www.anapioficeandfire.com/api/books"

    def update_endpoint_with_query_params(self, query_params):
        name = query_params.get('name', None)
        if name is not None:
            self.url_endpoint += "?name={}".format(name)

    def get_books(self, query_params):
        self.update_endpoint_with_query_params(query_params)
        api_response = requests.get(self.url_endpoint)
        json_data = json.loads(api_response.text)
        for element in json_data:
            del element['url']
            del element['characters']
            del element['mediaType']
            del element['povCharacters']
        return json_data
