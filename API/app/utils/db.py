import psycopg2
from app.extensions import db
from app.models import UserEntity

def get_author(author_id: int)->str:
    """
    Retrieve the author username from the database based on its id
    
    Args:
        author_id (int): The user_id of the author to retrieve
    
    Returns:
        str: The username of the author
    """
    return db.session.query(UserEntity).filter_by(id=author_id).first().username


def init_db(db_uri: str, tables: list[dict]):
    """
        Creates the db with the specified tables
        
        Args: 
            - db_uri (str): The database URI
            - tables (list[dict]): A list of objects that represent the tables:
                {
                    "name": str,
                    "columns": [
                        {
                            "name": str,
                            "type": str
                            "constraints": str
                        }
                    ]
                }
    """
    conn = psycopg2.connect(db_uri)
    cursor = conn.cursor()
    
    for table in tables:
        columns = [
            f"{column['name']} {column['type']} {column['constraints']}"
                for column in table['columns']
        ]
        
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {table['name']} ({', '.join(columns)});")
        
    conn.commit()
    conn.close()