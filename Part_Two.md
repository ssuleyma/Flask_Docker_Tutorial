## Part 2: Deploying model as Docker container
#### Part 2 assets
- requirements.txt
- Dockerfile
- model.py
- server.py
- sales.csv
- sales_model.pkl
#### Steps
1. Install anaconda and create a virtual environment
  - Set current directory to the Dockerfile folder: 
  - > cd ~/Desktop/Flask_Docker_Tutorial/Tutorial_Assets/Part_Two
  - Create new environment: 
  - > conda create -n flaskappdocker python=3.8
2. Check environment has been created: 
> conda env list
3. Create all required files for flask app. 
  - requirements.txt: pandas, numpy, flask, scikit-learn , gunicorn (sample provided)
  - model.py file and save model (sample provided)
  - app.py file and save it (sample provided)
4. Activate environment and install dependencies from requirements.txt. 
> conda activate flaskappdocker
> conda install --yes --file requirements.txt 
> conda deactivate
5. Create Dockerfile (sample provided)
6. Build the image:
> docker build -t flaskappimage:0.1 .
7. List all images: 
> docker image ls
8. Start the container: 
> docker run --name flaskappcontainer -p 5000:5000 flaskappimage:0.1
9. Open a new shell window and stop then delete container (optional)
> docker container stop flaskappcontainer
> docker container rm flaskappcontainer
