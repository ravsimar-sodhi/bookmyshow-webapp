from flask import Blueprint, request, session, jsonify, render_template
from app import db
from sqlalchemy import *
class Seat (db.Model):
    __tablename__ = "seat"
    id = db.Column('id', db.Integer, primary_key = True)
    row = db.Column('row', db.String)   #Row will be alphabetical A,B,C
    column = db.Column('column', db.Integer)

    def __init__(self,row,column):
        self.row = row
        self.column = column

    def to_dict_seat(self):
    	return {
    	'id' : self.id , 
    	'row' : self.row ,
    	'column' : self.column 
    	}

    def __repr__(self):
        return "Seat { row: %r column: %r}"%(self.row,self.column)