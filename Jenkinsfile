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
                sh "docker build -t $IMAGE_NAME ."
            }
        }

        stage('Run Containers') {
            steps {
                sh '''
                docker run -d \
                    --name $CONTAINER_NAME \
                    --network $NETWORK_NAME \
                    $IMAGE_NAME
                '''
            }
        }

        stage('Security Scan') {
            steps {
                sh 'trivy fs .'
            }
        }
    }
}



