***********************
Read Root Method (GET)
***********************

This is a simple utility method provided by the GADemo API, typically used to test if the API service is up and running.

**Endpoint:** ``/``  
**Method:** ``GET``

When a client sends a ``GET`` request to the root endpoint (``/``), the API responds with a simple JSON string.

**Parameters:**  
- *None* — This method does not require any query parameters or request body.

**Response:**  
- **Code:** ``200 OK``  
- **Media Type:** ``application/json``  
- **Example Output:**  
  
  .. code-block:: json

     "GADemo API is running"

This method is especially useful for:

- **Health checks** during deployment or maintenance.
- **Basic testing** of API availability through platforms like Swagger, Postman, or `curl`.

