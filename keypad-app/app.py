#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright (c) 2021 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at
               https://developer.cisco.com/docs/licenses
All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""


__author__ = "Josh Ingeniero <jingenie@cisco.com>"
__copyright__ = "Copyright (c) 2021 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"


from flask import Flask, jsonify, render_template, request

PIN = '1234'

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def intro():
    if request.method == 'GET':
        return render_template('index.html', title='Hello!')
    elif request.method == 'POST':
        data = request.form.to_dict()
        code = data['code']
        if PIN == code:
            return render_template('result.html', title='Success!', data='success')
        else:
            return render_template('result.html', title='Fail!', data='fail')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5001', debug=True)
