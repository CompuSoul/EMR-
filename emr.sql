-- The @searchTerm variable represents what the user typed in the search bar
-- Example: SET @searchTerm = 'Smith';

SELECT 
    patient_id, 
    first_name, 
    last_name, 
    dob, 
    ssn_last_4, 
    payor_source
FROM 
    patients
WHERE 
    first_name LIKE CONCAT('%', @searchTerm, '%') 
    OR last_name LIKE CONCAT('%', @searchTerm, '%') 
    OR CONCAT(first_name, ' ', last_name) LIKE CONCAT('%', @searchTerm, '%') -- Checks full name
    OR dob LIKE CONCAT('%', @searchTerm, '%') 
    OR ssn_last_4 = @searchTerm -- Exact match only for SSN to avoid partial hits
ORDER BY 
    last_name ASC, first_name ASC
LIMIT 20; -- Always limit results to prevent crashing the browser with too many rows