pipeline {
    agent any

    environment {
        IMAGE_NAME = "dockerapp"
        CONTAINER_NAME = "dockercontainer"
        NETWORK_NAME = "dockerapp-network"
    }

    stages {

        stage('Clean-up Stage') {
            steps {
                sh '''
                docker rm -f $CONTAINER_NAME || true
                '''
            }
        }

        stage('Set-up Stage') {
            steps {
                sh '''
                docker network inspect $NETWORK_NAME >/dev/null 2>&1 || \
                docker network create $NETWORK_NAME
                '''
            }
        }

        stage('Build Image') {
            steps {
                sh '''
                docker build -t $IMAGE_NAME .
                '''
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                docker run -d \
                    --name $CONTAINER_NAME \
                    --network $NETWORK_NAME \
                    -p 5500:5500 \
                    $IMAGE_NAME

                sleep 5
                '''
            }
        }

        stage('Test Stage') {
            steps {
                sh '''
                docker run --rm \
                    --network $NETWORK_NAME \
                    $IMAGE_NAME \
                    python3 -m unittest test.py
                '''
            }
        }

        stage('Security Scan') {
            steps {
                sh '''
                trivy fs .
                '''
            }
        }
    }
