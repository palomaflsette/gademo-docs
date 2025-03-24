# API


This section provides a complete reference to the **GADemo backend API**, enabling users to programmatically interact with the genetic algorithm engine.

It is designed for **developers and researchers** who wish to integrate GADEMO into custom applications, automate experiment execution, or extend its functionality for advanced use cases.

The API documentation is organized into the following key components:

- **About DEAP Library**: Background on the evolutionary computation library used to build the GA engine.
- **General Documentation**: Overview of the API architecture and usage.
- **GET Method – Root Endpoint**: Basic route to verify the server status or retrieve metadata.
- **POST Method – Run Experiments**: Core endpoint that receives execution parameters and returns genetic algorithm results.
- **Parameters**: Description of the configurable fields available in each request.
- **Request Body**: Format and structure of the JSON payload expected by the POST method.
- **Endpoint**: URL specification for accessing the API services.
- **Response**: Structure and meaning of the returned data after experiment execution.


This section empowers users to go beyond the web interface and build custom workflows for experimentation, analysis, and optimization through flexible HTTP-based communication with the GADEMO engine.


```{toctree}
:caption: API

about_deap
documentation
read_root
run_experiments
```
