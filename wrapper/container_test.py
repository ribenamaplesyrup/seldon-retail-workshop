from seldon_core.seldon_client import SeldonClient

endpoint = "0.0.0.0:9001"

data = [[-0.43831067,  0.23457404, -0.17366155,  0.26935668,  0.13463672, -0.55234561]]

sc = SeldonClient(microservice_endpoint=endpoint)
response = sc.microservice(
   json_data = data,
   method='predict'
)

print(response.request)
print(response.response)
