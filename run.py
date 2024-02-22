from flask import Flask, jsonify
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:1234567890@localhost:3306/db1'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Define your database connection string
DB_CONNECTION_STRING = "mysql+mysqlconnector://root:1234567890@localhost:3306/db1"

# Create engine and session
engine = create_engine(DB_CONNECTION_STRING)
Session = sessionmaker(bind=engine)
session = Session()

# Define a base class for declarative class definitions
Base = declarative_base()
 
# Define your table structure as a class
class YourTable(Base):
    __tablename__ = 'app_master'
 
    # id = Column(Integer, primary_key=True)
    file_id = Column(Integer, primary_key=True)
    app_code = Column(String)
    file_name = Column(String)
    # Add more columns as needed

@app.route('/', methods=['GET'])
def read_and_write():
    return '{"status": "up"}'

# Route to fetch data from the database
@app.route('/data', methods=['GET'])
def get_data():
    try:
        # Execute your query
        session = Session()
        query = session.query(YourTable).all()
        session.close()

        # Convert query result to a list of dictionaries
        data = []
        for row in query:
            data.append({
                'file_id': row.file_id,
                'app_code': row.app_code,
                'file_name': row.file_name,
                # Add more columns as needed
            })

        # Return JSON response
        return jsonify({'data': data}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)