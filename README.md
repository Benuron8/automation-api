# API Testing with Pytest
This project contains API test automation using Pytest. 
The tests can be run locally or using Docker and also in Github Actions.

#### Prerequisites:
    Git: For cloning the repository.
    Python 3.13.2: For running the API tests.
    Docker: For running the tests in a containerized environment.

#### Clone the Repository
git clone https://github.com/Benuron8/automation-api.git
cd automation-api

#### Install dependencies
pip install -r requirements.txt

#### Environment variables
To run the API tests an Api token is needed. I added the API token  in a file ".env" that is on .gitignore (so it will not be found in the repository remote)
To run: 
    api token will be shared in other way
    then create a .env file in the first project level in automation-api/
    inside that file just add -> API_TOKEN={insert here the api token}

#### Running locally 
python -m pytest tests/ --html=report.html

this will generate a report.html

#### Running with Docker

build the Docker image:

docker build -t pytest-api .

run the Docker container:
choose a name for the container because the container is not being removed, for reporting porpuse

docker run --env-file .env --name {name_your_container} pytest-api

Get the report generated from the Docker container run into the project directory:
(check for the active containers):
docker ps -a

run to get the report: (using the your container_id)
docker cp <container_id>:/automation-api/tests/test_report.html ./test_report.html

ex: "docker cp 2df5a12a6236:/automation-api/tests/test_report.html ./test_report.html"

#### GitHub Actions
Open the repository and in Tab Actions click the last job runned and click "Re-run all jobs"

