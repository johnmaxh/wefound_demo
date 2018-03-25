import logging

from flask import request
from flask_restplus import Resource
from rest_api_demo.api.blog.business import create_category, delete_category, update_category
from rest_api_demo.api.blog.serializers import person, person_with_findings, category, category_with_posts
from rest_api_demo.api.restplus import api
from rest_api_demo.database.models import Category

log = logging.getLogger(__name__)

ns = api.namespace('people', description='Operations related to person Objects')


@ns.route('/')
class PersonCollection(Resource):

    @api.marshal_list_with(person)
    def get(self):
        """
        Returns list of people.
        """
        categories = Category.query.all()
        return categories

    @api.response(201, 'Person successfully created.')
    @api.expect(person)
    def post(self):
        """
        Creates a new person object.
        """
        data = request.json
        create_category(data)
        return None, 201


@ns.route('/<int:id>')
@api.response(404, 'Person not found.')
class PersonItem(Resource):

    @api.marshal_with(person_with_findings)
    def get(self, id):
        """
        Returns a Person with a list of findings.
        """
        return Category.query.filter(Category.id == id).one()

    @api.expect(person)
    @api.response(204, 'Person successfully updated.')
    def put(self, id):
        """
        Updates a person object.

        Use this method to change the name or email of a person.

        * Send a JSON object with the new name and email in the request body.

        ```
        {
          "name": "New Category Name"
          "email": "New Email Address"
        }
        ```

        * Specify the ID of the person to modify in the request URL path.
        """
        data = request.json
        update_category(id, data)
        return None, 204

    @api.response(204, 'person successfully deleted.')
    def delete(self, id):
        """
        Deletes blog category.
        """
        delete_category(id)
        return None, 204
