import logging

from flask import request
from flask_restplus import Resource
from rest_api_demo.api.blog.business import create_category, delete_category, update_category
from rest_api_demo.api.blog.serializers import finding, finding_with_person_and_source, category, category_with_posts
from rest_api_demo.api.restplus import api
from rest_api_demo.database.models import Category

log = logging.getLogger(__name__)

ns = api.namespace('findings', description='Operations related to findings')


@ns.route('/')
class FindingCollection(Resource):

    @api.marshal_list_with(finding)
    def get(self):
        """
        Returns list of findings.
        """
        categories = Category.query.all()
        return categories

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
        Returns a list of related Findings.
        """
        data = request.json
        create_category(data)
        return None, 201


@ns.route('/<string:text>')
@api.response(404, 'Finding not found.')
class FindingItem(Resource):

    @api.marshal_with(finding_with_person_and_source)
    def get(self, id):
        """
        Returns a list of related Findings.
        """
        data = request.json
        create_category(data)
        return None, 201
