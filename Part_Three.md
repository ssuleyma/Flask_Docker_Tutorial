## Part 3: Connecting multiple containers
#### Part 3 assets
- docker-compose.yml
- Part_One
- Part_Two (this folder is not required for docker compose because we build our environment from remote image)
#### Steps
1. Send request to the model container from another container. Go to Predict_Notebook and run it. You should get network error. To send request from one container to another in your local environment you have to connect them using Docker Compose:
  - Create Docker compose yaml file: docker-compose.yml (sample provided)
  - Put all your applications into one folder and set current directory to that folder: 
  - > cd ~/Desktop/Flask_Docker_Tutorial/Tutorial_Assets/Part_Three
  - Build image and start container: 
  - > docker-compose up 
  - Use Predict_Notebook to send request to compose-flask-app.
  - Delete all containers (Optional): 
  - > docker-compose down
