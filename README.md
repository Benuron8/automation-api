# automation-api
Testing framework using Python and Pytest for testing services from themoviedb.org

#### To run inside of a Docker container:
docker run --rm --env-file .env api-tests

#### Run without using Docker
python -m pytest tests/ --html=report.html

#### Generated report after running
automation-api/report.html