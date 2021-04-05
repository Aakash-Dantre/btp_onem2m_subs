import requests
import json
import time

def create_ae(uri_ae,authentication, cnt_name, cnt_labels="", data_format="json"):
    """
        Method description:
        Creates a container(CON) in the OneM2M framework/tree
        under the specified AE

        Parameters:
        uri_ae : [str] URI for the parent AE
        cnt_name : [str] name of the container (DESCRIPTOR/DATA)
        data_format : [str] body format
    """

    headers = {
        'X-M2M-Origin': authentication,
        'Content-type': 'application/{};ty=2'.format(data_format)}

    body = {
        "m2m:ae": {
            "rn": "{}".format(cnt_name),
            "api": "test_id",
            "lbl": cnt_labels,
            "rr":"false",
        }
    }

    try:    
        response = requests.post(uri_ae, json=body, headers=headers)
    except TypeError:
        response = requests.post(uri_ae, data=json.dumps(body), headers=headers)

    #print('Return code : {}'.format(response.status_code))
    #print('Return Content : {}'.format(response.text))

def create_cnt(uri_ae,authentication, cnt_name, cnt_labels="", data_format="json"):
    """
        Method description:
        Creates a container(CON) in the OneM2M framework/tree
        under the specified AE

        Parameters:
        uri_ae : [str] URI for the parent AE
        cnt_name : [str] name of the container (DESCRIPTOR/DATA)
        data_format : [str] body format
    """

    headers = {
        'X-M2M-Origin': authentication,
        'Content-type': 'application/{};ty=3'.format(data_format)}

    body = {
        "m2m:cnt": {
            "rn": "{}".format(cnt_name),
            "mni": 120,
            "lbl": cnt_labels,
        }
    }

    try:    
        response = requests.post(uri_ae, json=body, headers=headers)
    except TypeError:
        response = requests.post(uri_ae, data=json.dumps(body), headers=headers)

    #print('Return code : {}'.format(response.status_code))
    #print('Return Content : {}'.format(response.text))


def create_desc_cin(uri_desc_cnt,authentication, node_description, desc_cin_labels="", data_format="json"):
    """
        Method description:
        Creates a descriptor content instance(desc_CIN) in the OneM2M framework/tree
        under the specified DESCRIPTOR CON

        This holds the detailed description for an specific AE

        Parameters:
        uri_desc_cnt : [str] URI for the parent DESCRIPTOR CON
        data_format : [str] payload format
    """

    headers = {
        'X-M2M-Origin': authentication,
        'Content-type': 'application/{};ty=4'.format(data_format)}

    body = {
        "m2m:cin": {
            "cnf":"application/json",
            "con":node_description,
            "lbl":desc_cin_labels,
            "test":"failed",
        }
    }

    try:
        response = requests.post(uri_desc_cnt, json=body, headers=headers)
    except TypeError:
        response = requests.post(uri_desc_cnt, data=json.dumps(body), headers=headers)
    print('Return code : {}'.format(response.status_code))
    #print('Return Content : {}'.format(response.text))


def create_sub(uri_data_cnt,vert,authentication,data_format="json"):
    """
        Method description:
        Creates a subscription in the OneM2M framework/tree
        under the specified DATA CNT

        This is to send data to desired application

        Parameters:
        uri_data_cnt : [str] URI for the parent DATA CON
    """
    sub_url= "http://127.0.0.1:8000/"+vert
    headers = {
        'X-M2M-Origin': authentication,
        'Content-type': 'application/{};ty=23'.format(data_format)}

    body = {
        "m2m:sub": {
            "nu":sub_url,
            "nct":2
        }
    }
    print(body)
    try:
        response = requests.post(uri_data_cnt, json=body, headers=headers)
    except TypeError:
        response = requests.post(uri_data_cnt, data=json.dumps(body), headers=headers)

    print('Return code : {}'.format(response.status_code))
    print('Return Content : {}'.format(response.text))

    _resp=json.loads(response.text)
    ri=_resp["m2m:sub"]["ri"]
    ri=ri.split("/in-cse/")[1]
    #print(ri)
    return ri

def create_sub2(uri_data_cnt,authentication,data_format="json"):
    """
        Method description:
        Creates a subscription in the OneM2M framework/tree
        under the specified DATA CNT

        This is to send data to desired application

        Parameters:
        uri_data_cnt : [str] URI for the parent DATA CON
    """
    sub_url= "http://127.0.0.1:8000/"
    headers = {
        'X-M2M-Origin': authentication,
        'Content-type': 'application/{};ty=23'.format(data_format)}

    body = {
        "m2m:sub": {
            "nu":sub_url,
            "nct":2
        }
    }
    #print(body)
    try:
        response = requests.post(uri_data_cnt, json=body, headers=headers)
    except TypeError:
        response = requests.post(uri_data_cnt, data=json.dumps(body), headers=headers)

    #print('Return code : {}'.format(response.status_code))
    #print('Return Content : {}'.format(response.text))

    _resp=json.loads(response.text)
    ri=_resp["m2m:sub"]["ri"]
    ri=ri.split("/in-cse/")[1]
    #print(ri)
    return ri

def discovery(uri,authentication, data_format="json"):
    """
        Method description:
        Deletes/Unregisters an application entity(AE) from the OneM2M framework/tree
        under the specified CSE

        Parameters:
        uri_cse : [str] URI of parent CSE
        ae_name : [str] name of the AE
        fmt_ex : [str] payload format
    """
    headers = {
        'X-M2M-Origin': authentication,
        'Connection':'keep-alive',
        'Content-type': 'application/{}'.format(data_format)}

    response = requests.get(uri, headers=headers)
    _resp = json.loads(response.text)
    return _resp