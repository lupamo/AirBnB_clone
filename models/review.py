#!/usr/bin/python3
"""This module creates a review class"""

from models.base_model import BaseModel

class Review(BaseModel):
    """Class for managing review projects"""
    
    place_id = ""
    user_id = ""
    text = ""
