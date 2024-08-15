## Docker & Docker-Compose installation commands:
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

## Usage of Docker:
1) Create a Dockerfile and docker-compose.yml files.
2) Configure and write commands into those files
3) Grant permissions: sudo usermod -aG docker $USER
4) [OPTIONAL] - Check docker status: sudo systemctl status docker
5) If not already running: sudo systemctl start docker
6) Check permissions: ls -l /var/run/docker.sock
7) sudo chown :docker /var/run/docker.sock
8) At last it would be good to restart docker: sudo systemctl restart docker

## Django REST Framework migration in docker compose container:
## Never forget this step after building image. Otherwide it gets stuck in memory issues.
sudo docker exec -it web python3 manage.py makemigrations
sudo docker exec -it web python3 manage.py migrate

## Django REST Framework collecting static files dir
sudo docker exec -it web-service python3 manage.py collectstatic --no-input

# Create default admin for admin panel
1) sudo docker exec -it web-service python3 manage.py createsuperuser --username "admin" --email "admin@gmail.com"
2) >>> default password: "admin"
3) >>> confirm by entering: y

## Inspect and get credentials from docker container
sudo docker inspect db  

## Push the Project on DockerHub
docker login

# Step 2: Build the Docker image
sudo docker build -t prowider5565/suzane-ecommerce:tag .

# Step 3: Push the Docker image to Docker Hub
sudo docker push prowider5565/suzane-ecommerce:tag
sudo docker push prowider5565/suzane-ecommerce:latest
