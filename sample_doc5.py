Experiment 5 — Create and Run Docker Image

Aim:
Create a Docker image for a Python application stored in a local repository and run the application using Docker container.

Step 1 — Open Docker Desktop

1. Press Windows Key
2. Search "Docker Desktop"
3. Open Docker Desktop
4. Wait until Docker Engine starts and shows:
   Engine running

--------------------------------------------------

Step 2 — Create Project Folder

Create folder structure:

Desktop
└── Devops
    └── dockerimage

--------------------------------------------------

Step 3 — Open Folder in VS Code

1. Open VS Code
2. Click:
   File → Open Folder
3. Select:
   dockerimage

--------------------------------------------------

Step 4 — Create Python File

Create file:
sample.py

Paste the following code:

print("Hello World")

Save the file.

--------------------------------------------------

Step 5 — Create Dockerfile

Create file:
Dockerfile

Paste the following content:

FROM python

WORKDIR /app

COPY . /app

CMD ["python","sample.py"]

Save the file.

--------------------------------------------------

Step 6 — Open Terminal in VS Code

Click:
Terminal → New Terminal

--------------------------------------------------

Step 7 — Run Python File

Command:

py sample.py

Output:

Hello World

--------------------------------------------------

Step 8 — Build Docker Image

Command:

docker build -t test.1 .

Explanation:
- docker build → builds docker image
- -t → tag/image name
- test.1 → image name
- . → current directory

Check image:

docker images

You should see:
test.1

--------------------------------------------------

Step 9 — Run Docker Container

Command:

docker run --name cont1 test.1

Output:

Hello World

--------------------------------------------------

Step 10 — Check Container

Command:

docker ps -a

You should see:
cont1

--------------------------------------------------

Step 11 — Verify in Docker Desktop

Open Docker Desktop and check:
- Images → test.1
- Containers → cont1

--------------------------------------------------

Step 12 — Login to Docker Hub

Command:

docker login

Enter Docker Hub username and password.

If successful:
Login Succeeded

--------------------------------------------------

Step 13 — Tag Docker Image

Command:

docker image tag test.1 username/test.1

Example:

docker image tag test.1 shamanth/test.1

--------------------------------------------------

Step 14 — Push Image to Docker Hub

Command:

docker push username/test.1:latest

Example:

docker push shamanth/test.1:latest

--------------------------------------------------

Output:

Hello World
