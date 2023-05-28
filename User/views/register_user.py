# -*- coding: utf-8 -*-
import falcon

from User.Model.user import User
from utilities.password_hashing import Encrypt


class RegisterUser:

    def on_post(self, request, response):
        user_input = request.media
        if not (user_input.get('user_name')):
            response.status = falcon.HTTP_422
            response.media = {'msg': 'Username is a required field'}
            return response
        elif not user_input.get('email'):
            response.status = falcon.HTTP_422
            response.media = {'msg': 'email is a required field'}
            return response
        elif not user_input.get('password'):
            response.status = falcon.HTTP_422
            response.media = {'msg': 'password is a required field'}
            return response

        user_obj = User.objects.filter(user_name=user_input['user_name']).first()
        if user_obj:
            response.media = {'msg': 'User Already Exists'}
            return response
        else:
            hash_pass = Encrypt().encrypt(user_input.get('password'))
            new_user_obj = User(user_name=user_input['user_name'],
                                email=user_input['email'],
                                password=hash_pass)
            new_user_obj.save()
            response.status = falcon.HTTP_200
            response.media = {'msg': 'New User created successfully', 'data': new_user_obj.to_dict}
            return response
