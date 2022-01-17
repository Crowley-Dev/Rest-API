#!/usr/bin/env python3

import requests, json


url = "http://0.0.0.0:5000/api?cpf={}"

resp = requests.request(
    method = "GET",
    url = url.format("00000000272"),
    headers = {
        "Content-Type": "application/json",
        # "token": "6m8x4x0b-8d3z1o3j-7n8c3z4l-0b7m7r5h",
    }

); print(resp.text)
