# -*- coding: utf-8 -*-
class ResponseHandler:
    def __init__(self, parameters, data=None):
        self.parameters = parameters
        self.data = data

    def success_response(self):
        if not self.data:
            return {'msg': f'{self.parameters} created successfully'}
        else:
            return {'msg': f'{self.parameters} created successfully', 'data': self.data}
