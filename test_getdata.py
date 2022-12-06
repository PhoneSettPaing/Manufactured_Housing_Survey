from getdata import data_source


def test_data_source():
    assert len(data_source()) == 8
    file_list = [
        "PUF2021final_v1.xls",
        "PUF2020final_v1coll.xlsx",
        "PUF2019.xlsx",
        "PUF2018.xlsx",
        "PUF2017.xlsx",
        "puf2016.xlsx",
        "PUF2015.xlsx",
        "PUF2014.xlsx",
    ]
    assert all(ele in str(data_source()) for ele in file_list) == True
