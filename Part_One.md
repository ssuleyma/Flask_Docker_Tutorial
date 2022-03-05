## Part 1: Experimenting and developing with Docker
File assets:
- Dockerfile
- Sample_Notebook.ipynb
- Predict_Notebook.ipynb

1. Download all assets & save to desktop
2. Open Docker dashboard app
3. Open command line (terminal)
4. Sign up and log in to [Docker Hub](https://hub.docker.com/repositories): <i>docker login</i>
5. Pull docker image: <i>docker pull jupyter/minimal-notebook</i>
6. Start a container with the command below. <b>--name</b> is parameter for container name. <b>-p</b> is parameter for port. <b>-v</b> is parameter for volume. We share notebooks between local host and container using volume. Note file folder for the container is /home/jovyan from documentation.
	- <i>docker run --name jdevenv -p 8888:8888 -v ~/Desktop/Flask_Docker/Tutorial_Assets/Part_One:/home/jovyan jupyter/minimal-notebook</i>

7. Copy and paste the link in terminal into your browser & open the Sample_Notebook.ipynb:
	- http://127.0.0.1:8888/?token=449dcbea7507f431c304453d21649af19
	- Run first 2 cells, and move to next step.
8. There are 2 ways to install packages in Docker:
	- <b>Approach 1:</b> Install packages while running the container. Docker exec command needs id of running container. Remember if container is stopped or removed, the Flask package will not be available.
		- Open a new terminal window and list all running containers: docker container ls
		- Install flask: docker exec container_id pip install flask
		- Go back to Notebook and run cell 3. Flask should be available.


