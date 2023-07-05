# -*- coding: utf-8 -*-
from Product.Model.product_type import Category


class CategoryManager:

    def on_post(self, request, response):
        data = request.media
        Category(name=data.get('name')).save()
        response.media = {'msg': 'Category saved successfully'}
        return response

    def on_get(self, request, response):
        response_list = []
        category_list = Category.objects.all()
        print(category_list)
        for item in category_list:
            response_list.append(item.to_dict)
        print(response_list)
        response.media = {'items': response_list}
        return response
