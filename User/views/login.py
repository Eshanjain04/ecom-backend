# -*- coding: utf-8 -*-
import falcon
import jwt

from settings.config import JWT_ALGORITHM
from settings.config import JWT_KEY
from User.Model.user import User
from utilities.password_hashing import Encrypt


class Login:

    def on_post(self, req, resp):
        user_name = req.media.get('user_name')
        email = req.media.get('email')
        password = req.media.get('password')
        user_obj = None
        if user_name:
            user_obj = User.objects.filter(user_name=user_name).first()
        if email:
            user_obj = User.objects.filter(email=email).first()
        print(user_obj)
        if not user_obj:
            resp.status = falcon.HTTP_422
            resp.media = {'msg': 'User not found'}
            return resp
        decrypted_password = Encrypt.decrypt(password, user_obj.password)
        if not decrypted_password:
            resp.status = falcon.HTTP_422
            resp.media = {'msg': 'Invalid Password'}
            return resp
        else:
            resp.status = falcon.HTTP_200
            payload = {'user_id': str(user_obj.pk)}
            token = jwt.encode(payload, JWT_KEY, algorithm=JWT_ALGORITHM)
            resp.media = {'msg': 'Login Successful', 'token': token, 'data': user_obj.to_dict}
            return resp
