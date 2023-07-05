# -*- coding: utf-8 -*-
import falcon
from bson import ObjectId

from Product.Model.product import Product


class ProductManager:

    def on_post(self, request, response, *args, **kwargs):
        data = request.media
        Product(name=data.get('name'),
                description=data.get('description'),
                category=ObjectId(data.get('category')),
                stock=data.get('stock'),
                weight=data.get('weight'),
                price=data.get('price'),
                image=data.get('image', 'https://random.imagecdn.app/500/150')).save()
        response.status = falcon.HTTP_200
        response.media = {'msg': 'product saved successfully'}
        return response

    def on_get(self, request, response):
        response_list = []
        category_list = Product.objects
        for item in category_list:
            response_list.append(item.to_dict)
        response.media = {'items': response_list}
        return response

    def on_put(self, request, response, *args, **kwargs):
        try:
            data = request.media
            product = None
            if data.get('name'):
                product = Product.objects.filter(name=data.get('name')).first()
            else:
                product = Product.objects.filter(id=kwargs['id']).first()
            if not product:
                response.status = falcon.HTTP_200
                response.media = {'msg': 'Product not found'}
                return response
            product.update(name=data.get('name'),
                           description=data.get('description'),
                           category=data.get('category'),
                           stock=data.get('stock'),
                           weight=data.get('weight'),
                           price=data.get('price'),
                           image=data.get('image'))
            response.status = falcon.HTTP_200
            response.media = {'msg': 'Product Updated Successfully'}
            return response
        except ValueError:
            raise ValueError('Error occured')
