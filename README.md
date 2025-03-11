# automation-api
Testing framework using Python and Pytest for testing services from themoviedb.org

#### Run without using Docker
python -m pytest tests/ --html=report.html

#### Generated report after running without using Docker container
automation-api/report.html

#### (if needed) build the container after any change
docker build -t my-python-api-tests . 

#### To run inside of a Docker container without removing it:
docker run --env-file .env --name my_test_container my-python-api-tests 

#### Get the report generated from the Docker container run into the project directory
check for the active containers:
docker ps -a

run to get the report: (using the container_id)
docker cp <container_id>:/automation-api/tests/test_report.html ./test_report.html
