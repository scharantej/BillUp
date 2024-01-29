
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for
import csv
import sqlite3

# Initialize the Flask application
app = Flask(__name__)

# Database configuration
conn = sqlite3.connect('billers.db')
c = conn.cursor()

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for handling the biller ingestion process
@app.route('/ingest', methods=['POST'])
def ingest():
    # Get the uploaded CSV file
    file = request.files['csv_file']

    try:
        # Parse the CSV file
        csv_reader = csv.reader(file)
        
        # Extract biller data and insert into the database
        for row in csv_reader:
            biller_id, biller_name, biller_address = row
            c.execute("INSERT INTO billers VALUES (?, ?, ?)", (biller_id, biller_name, biller_address))
        
        # Commit the changes to the database
        conn.commit()

        # Redirect to the success page
        return redirect(url_for('success'))
    
    except Exception as e:
        # Handle errors during biller ingestion
        return redirect(url_for('error', error=str(e)))

# Route for displaying the success page
@app.route('/success')
def success():
    # Get the number of billers ingested
    c.execute("SELECT COUNT(*) FROM billers")
    num_billers = c.fetchone()[0]
    
    return render_template('success.html', num_billers=num_billers)

# Route for displaying the error page
@app.route('/error')
def error():
    # Get the error message from the query string
    error = request.args.get('error')
    
    return render_template('error.html', error=error)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)


This code includes the necessary Python libraries, configures the database, defines routes for the home page, biller ingestion, success, and error pages, and handles the biller ingestion process. The code is structured, commented, and follows proper Python conventions. It should generate the main Python code for the Flask application as per the given design and problem specifications. No additional files or outputs are included, and the generated code adheres to the provided constraints.