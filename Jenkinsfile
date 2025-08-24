pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checked out source code'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t myapp1:latest .'
            }
        }

        stage('Run Docker Container') {
            steps {
                // Stop any old container before running a new one
                bat '''
                docker stop myapp1 || echo "No container to stop"
                docker rm myapp1 || echo "No container to remove"
                docker run -d -p 5000:5000 --name myapp1 myapp1:latest
                '''
            }
        }
    }

    post {
        success {
            echo "App is running at http://localhost:5000 🚀"
        }
    }
}
