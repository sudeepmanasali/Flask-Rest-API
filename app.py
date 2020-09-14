from flask import Flask, request, redirect, render_template, url_for, json,jsonify
from flask_restful import Api, Resource, reqparse
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)
api = Api(app)


parser = reqparse.RequestParser()
parser.add_argument("data")



class HelloWorld(Resource):
    def get(self):

        connection = mysql.connector.connect(host="localhost",user="root",password="",database="chameleonquiz")
        query = "select question,opt1,opt2,opt3,opt4,correctopt from questions"
        cursor = connection.cursor()
        cursor.execute(query)
        global result
        result = cursor.fetchall()
        return result
  
    def post(self):
        args=parser.parse_args()
        global res
        res = json.dumps(args)
        
        print(args)
        return(res)
        


@app.route("/home")
def home():
    
    return (res) 
api.add_resource(HelloWorld, "/helloworld")


