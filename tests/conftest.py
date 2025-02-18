import pytest
import helpers
import test_urls
import requests

@pytest.fixture()
def delete_courier(request):
    courier_data = helpers.generate_courier()

    requests.post(test_urls.main_url + test_urls.create_courier_url, data=courier_data)

    marker = request.node.get_closest_marker('f_data')
    data_to_change = None if marker is None else marker.args[0]
    if data_to_change in courier_data:
        courier_data[data_to_change] = "text_to_change"
    elif data_to_change == 'delete login':
        del courier_data['login']
    else:
        pass

    response = requests.post(test_urls.main_url + test_urls.login_courier_url, data=courier_data)
    request.cls.response = response

    yield

    if response.status_code == 200:
        del_req = requests.delete(test_urls.main_url + test_urls.create_courier_url + '/' + response.text[6:12])



