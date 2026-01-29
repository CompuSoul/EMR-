@app.route('/api/search_patients', methods=['GET'])
def search_patients():
    search_term = request.args.get('q', '') # Get text from search bar
    
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True) # Return results as JSON objects
    
    # The SQL Query (Safe Version)
    sql = """
        SELECT patient_id, first_name, last_name, dob, ssn_last_4, payor_source
        FROM patients
        WHERE first_name LIKE %s 
           OR last_name LIKE %s 
           OR CONCAT(first_name, ' ', last_name) LIKE %s
           OR ssn_last_4 = %s
        LIMIT 20
    """
    
    # Add wildcards (%) to the search term for the 'LIKE' clauses
    wildcard_search = f"%{search_term}%"
    exact_search = search_term 
    
    # We pass the variables separately from the SQL string for security
    params = (wildcard_search, wildcard_search, wildcard_search, exact_search)
    
    cursor.execute(sql, params)
    results = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return jsonify(results)