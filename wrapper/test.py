from CustomerSegmenter import CustomerSegmenter

X = {"data": {
"names": ['mean', 'categ_0', 'categ_1', 'categ_2', 'categ_3', 'categ_4' ],
"ndarray": [[-0.43831067,  0.23457404, -0.17366155,  0.26935668,  0.13463672, -0.55234561]]}}

result = CustomerSegmenter().predict(X['data']['ndarray'], X['data']['names'])
print(result)
