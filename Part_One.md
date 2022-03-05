## Part 1: Experimenting and developing with Docker
Part 1 assets:
- Dockerfile
- Sample_Notebook.ipynb
- Predict_Notebook.ipynb

1. Clone this repository & save to desktop
2. Open Docker dashboard app
3. Open command line (terminal)
4. Sign up and log in to [Docker Hub](https://hub.docker.com/repositories): 
> docker login
5. Pull docker image:
> docker pull jupyter/minimal-notebook
6. Start a container with the command below. <b>--name</b> is parameter for container name. <b>-p</b> is parameter for port. <b>-v</b> is parameter for volume. We share notebooks between local host and container using volume. Note file folder for the container is /home/jovyan from documentation.
> docker run --name jdevenv -p 8888:8888 -v ~/Desktop/Flask_Docker_Tutorial/Tutorial_Assets/Part_One:/home/jovyan jupyter/minimal-notebook

7. Copy and paste the link in terminal into your browser & open the Sample_Notebook.ipynb:
	- http://127.0.0.1:8888/?token=449dcbea7507f431c304453d21649af19
	- Run first 2 cells, and move to next step.
8. There are 2 ways to install packages in Docker:
	- <b>Approach 1:</b> Install packages while running the container. [Docker exec](https://docs.docker.com/engine/reference/commandline/exec/) command needs id of running container. Remember if container is stopped or removed, the Flask package will not be available.
		- Open a new terminal window and list all running containers: 
		- > docker container ls
		- Install flask: 
		- > docker exec container_id pip install flask
		- Go back to Notebook and run cell 3. Flask should be available.
	- <b>Approach 2:</b> Extend Docker image to include Flask. The package will always be available, but one need to build a new image and then run it.
		- Extend Docker image to include Flask by creating a [Dockerfile](https://github.com/jupyter/docker-stacks/blob/master/scipy-notebook/Dockerfile) (there is one already in folder Part_One, but you can create one yourself):
		- > FROM jupyter/minimal-notebook
		- > RUN pip install --quiet --no-cache-dir \ 'flask==1.1.2'
		- Set current directory to the Dockerfile folder:
		- > cd ~/Desktop/Flask_Docker/Tutorial_Assets/Part_One
		- Build image: 
		- > docker build -t extended-jupyter:flask .
		- Start container: 
		- > docker run --name extended-jupyter-container -p 8888:8888 -v ~/Desktop/Flask_Docker_Tutorial/Tutorial_Assets/Part_One:/home/jovyan extended-jupyter:flask

9. Push your extended image to Docker Hub to make it available to others. 
	- Create a repo in DockerHub by going to https://hub.docker.com and clicking <b>Create Repository</b>. Give a name and click <b>Create</b>. I named mine <b>my-dev-env</b>.
	- In your command line run the code to tag the local image: 
	- > docker tag image_name user_name/repo_name:tag_name (i.e. docker tag extended-jupyter:flask ssuleyma/my-dev-env:latest)
	- Push local image to Docker Hub: 
	- > docker push user_name/repo_name:tag_name (i.e. docker push ssuleyma/my-dev-env:latest)
	- Start your development container: 
	- > docker run --name mydevenv -p 8888:8888 -v ~/Desktop/Flask_Docker/Tutorial_Assets/Part_One:/home/jovyan image_name:tag (i.e. ssuleyma/my-dev-env:latest)

