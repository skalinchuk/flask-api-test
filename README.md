## "Simple API proxy" test assignment
This application creates a simple API proxy, that takes initial data from 
https://hokodo-frontend-interview.netlify.com/data.json and returns authors with books and sorted lists of books.  

The project is written on top of Flask microframework.

To run this project, you need to have docker installed in your system 
(see https://docs.docker.com/install/) 

Installing and starting this project is as simple as cloning it from this repository
and running the command: ```docker-compose up``` from its main folder.

The web interface of the system will be available at http://localhost:5000/

The following queries shall demonstrate the functionality of the project:
- unsorted list of books: http://localhost:5000/books
- list of books sorted by title in ascending order: http://localhost:5000/books?order_by=title
- list of books sorted by title in descending order: http://localhost:5000/books?order_by=title&order_dir=desc
- list of books sorted by published date in ascending order: http://localhost:5000/books?order_by=published
- list of books sorted by published date in descending order: http://localhost:5000/books?order_by=published&order_dir=desc
- list of authors with their books: http://localhost:5000/authors

The project contains some simple tests to cover basic functionality. To execute the test suite, please use the provided script ```bash test.sh``` 