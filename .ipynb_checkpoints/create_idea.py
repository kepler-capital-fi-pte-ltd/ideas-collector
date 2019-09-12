from db.py import Idea
from flask_sqlalchemy import SQLAlchemy

def find_reuters_code(search_key : str) -> list:
    """
    Allow the user to find reuters id from a company name or ticker
    :param search_key: string of text to match / search
    :return: the matched company name and RIC
    """
    reuters_id = "empty"
    company_name = "company_name"

    #TODO create this function
    return reuters_id, company_name

def create_idea(**kwargs) -> str:
    """
    Create a new idea in the db.
    Input kwargs should be all of the tables in the Idea model (found in the db.py file)
    :kwargs: dictionary of the idea arguments
    """
    new = Idea(kwargs)
    new.save()

def load_idea(iden : String): -> dict:
    return Idea.query.filter_by(iden=iden).first()

def update_idea(idea : Idea, changes : dict) -> str:
    """
    Updates an existing idea and saves to db.
    :param idea: Existing idea to be updated (object)
    :param changes: Dictionary of the fields to be updated
    :return: Confirmation of success
    """
    for k, v in changes.items():
        eval(f"idea.{k} = v")
        db.session.commit()