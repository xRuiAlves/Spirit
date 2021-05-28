# Spirit + Django Cloud Deployer

This is a [Spirit Project](https://github.com/nitely/Spirit) fork that serves as part of the validation process of the [django-cloud-deployer](https://pypi.org/project/django-cloud-deployer/) plugin package that was developed as a Proof of Concept for a part of my Master's Degree thesis work.

Feel free to [try out the deployment](http://spirit.thesis.ruialves.me/).

## Implemented Changes

- Updated project requirements to feature the `django-cloud-deployer` package dependency
- Added a Django app called `cloud_spirit` created with the [django-spirit](https://pypi.org/project/django-spirit/) package itself
- Updated the app's `settings.py` configurations to read information (such as database configurations) from environment variables
- Updated app's `urls.py` routes with `runInPaaS` and `runInFaaS` annotations

## Cloud Deployment Annotations - System Partitioning

The system's url endpoints were seperated (between PaaS and FaaS) as following:

- Running in FaaS:
    - `admin/*` routes
    - `category/*` routes
    - `search/*` routes
    - `media/*` routes
- Running in PaaS:
    - `user/*` routes
    - `topic/*` routes
    - `comment/*` routes

## Replicate this deployment

First, please refer to the [django-cloud-deployer](https://pypi.org/project/django-cloud-deployer/) package documentation.

- Install the requirements with `pip install -r requirements.txt`
- Configure the project:
    - Create a `.env` file with the required environment variables
    - Apply any required migrations with `python manage.py migrate`
    - Create database cache tables with `python manage.py createcachetable` 
- (*Optional*) Check which urls will run in which cloud service with the package's `check_deploy` command, with `python -m django_cloud_deployer check_deploy`
- Deploy the project with `python -m django_cloud_deployer deploy heroku azure`

## Notes and other regards

- An SMTP server was not configured for this deployment (since it was out of the scope of the validation purposes), and thus account creation is disabled
- A test account under the username `Mary_Lawrance` and password `password`
- The DNS configuration was made manually (it was out of the scope of the validation purposes) and is not part of the package deployment script as of now; However, it may be tackled as future work
