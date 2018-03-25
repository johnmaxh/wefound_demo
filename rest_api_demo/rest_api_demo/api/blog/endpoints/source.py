import logging

from flask import request
from flask_restplus import Resource
from rest_api_demo.api.blog.business import create_category, delete_category, update_category
from rest_api_demo.api.blog.serializers import source, source_with_findings, category, category_with_posts
from rest_api_demo.api.restplus import api
from rest_api_demo.database.models import Category

log = logging.getLogger(__name__)

ns = api.namespace('sources', description='Operations related to source Objects')


@ns.route('/')
class SourceCollection(Resource):

    @api.marshal_list_with(source)
    def get(self):
        """
        Returns list of sources.
        """
        categories = Category.query.all()
        return categories

    @api.response(201, 'Source successfully created.')
    @api.expect(source)
    def post(self):
        """
        Creates a new source object.
        """
        data = request.json
        create_category(data)
        return None, 201


@ns.route('/')
class SourceCollection2(Resource):

    @api.marshal_list_with(source)
    def get(self):
        """
        Returns list of sources.
        """
        categories = Category.query.all()
        return categories

    @api.response(201, 'Source successfully created.')
    @api.expect(source)
    def post(self):
        """
        Creates a new source object.
        """
        data = request.json
        create_category(data)
        return None, 201


@ns.route('/<int:id>')
@api.response(404, 'Source not found.')
class SourceItem(Resource):

    @api.marshal_with(source_with_findings)
    def get(self, id):
        """
        Returns a source with a list of findings.
        """
        return Category.query.filter(Category.id == id).one()

    @api.response(204, 'Source successfully deleted.')
    def delete(self, id):
        """
        Deletes source object.
        """
        delete_category(id)
        return None, 204
