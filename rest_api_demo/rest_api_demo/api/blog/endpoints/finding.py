import logging

from flask import request
from flask_restplus import Resource
from rest_api_demo.api.blog.business import create_category, delete_category, update_category
from rest_api_demo.api.blog.serializers import finding, finding_with_person_and_source, category, category_with_posts
from rest_api_demo.api.restplus import api
from rest_api_demo.database.models import Category

log = logging.getLogger(__name__)

ns = api.namespace('finding', description='Operations related to finding objects')


@ns.route('/')
class FindingCollection(Resource):

    @api.response(201, 'finding successfully created.')
    @api.expect(finding)
    def post(self):
        """
        Creates a new finding object.
        """
        data = request.json
        create_category(data)
        return None, 201


@ns.route('/<int:id>')
@api.response(404, 'Finding not found.')
class FindingItem(Resource):

    @api.marshal_with(finding_with_person_and_source)
    def get(self, id):
        """
        Returns a Finding with its corresponding person and source.
        """
        return Category.query.filter(Category.id == id).one()

    @api.response(204, 'Finding successfully deleted.')
    def delete(self, id):
        """
        Deletes finding object.
        """
        delete_category(id)
        return None, 204
