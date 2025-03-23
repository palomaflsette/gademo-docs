*************************
General System Structure
*************************


The GADemo platform adopts a modular architecture based on the principles of microservices. This design choice ensures scalability, flexibility, and ease of maintenance, enabling independent development, deployment, and updating of its components.

The **backend** is implemented in **Python**, making use of robust scientific and computational libraries such as **DEAP (Distributed Evolutionary Algorithms in Python)** for evolutionary computation, and **FastAPI** for the construction of a lightweight and high-performance API. This API serves as the computational core of the application, responsible for the execution of genetic algorithms and the orchestration of experiments.

The **frontend** was developed using **vanilla JavaScript**, **HTML5**, and **CSS3**, prioritizing clarity and performance. The interface is designed to be intuitive and responsive, providing users with dynamic visualizations and seamless interaction with the evolutionary processes.

In terms of deployment, the platform is currently hosted in two distinct environments:

- A **cloud-based instance** via `Render <https://gademo-zxig.onrender.com>`_, allowing for public and free access.
- A **local institutional server** within the **Maxwell system** at the **Pontifical Catholic University of Rio de Janeiro (PUC-Rio)**, ensuring long-term academic availability and preservation.

This structural configuration reinforces GADemo's dual objective: to serve as a practical educational tool while maintaining the robustness and professionalism expected of a research-supporting system.
