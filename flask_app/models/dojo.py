from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models import ninja

# Model file, Model class
class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []


    # CREATE
    @classmethod
    def create(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
        result = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)
        return result




    # READ
    # Read Many
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query)
        dojos = []

        for row in results:
            dojos.append(cls(row))
            
        return dojos


    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"

        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)

        return cls(results[0])
    

    @classmethod
    def get_dojos_with_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"

        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)

        this_dojo = cls(results[0])

        print(results)
        if results[0]["ninjas.id"] != None:
            for row_data in results:
                ninja_data = {
                    "id": row_data["ninjas.id"],
                    "first_name": row_data["first_name"],
                    "last_name": row_data["last_name"],
                    "dojo_id": row_data["dojo_id"],
                    "created_at": row_data["ninjas.created_at"],
                    "updated_at": row_data["ninjas.updated_at"]
                }
                this_dojo.ninjas.append(ninja.Ninja(ninja_data))

        return this_dojo

