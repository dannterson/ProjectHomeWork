def filter_by_state(data_state: list[dict], state: str = "EXECUTED") -> list[dict]:
    return list(filter(lambda i: i["state"] == state, data_state))


def sort_by_date(data_list: list[dict], reverse=True) -> list[dict]:
    return sorted(data_list, key=lambda x: x["date"], reverse=reverse)


test_data_filtered = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                      {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                      {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                      {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

test_data_sort = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                  {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                  {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                  {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

print(filter_by_state(test_data_filtered))
print(sort_by_date(test_data_sort))
