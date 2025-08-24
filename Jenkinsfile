pipeline {
    agent any

    // Define parameters for versioning & rollback
    parameters {
        string(name: 'APP_VERSION', defaultValue: 'v1.0.0', description: 'Version tag for this build')
        booleanParam(name: 'ROLLBACK', defaultValue: false, description: 'Check to rollback to previous version')
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checked out source code'
            }
        }

        stage('Build Docker Image') {
            when { expression { return !params.ROLLBACK } }  // Skip build if rolling back
            steps {
                // Build Docker image with a version tag
                bat "docker build -t myapp1:${params.APP_VERSION} ."
                // Optionally tag latest for convenience
                bat "docker tag myapp1:${params.APP_VERSION} myapp1:latest"
            }
        }

        stage('Deploy / Rollback') {
            steps {
                script {
                    def versionToRun = params.ROLLBACK ? params.APP_VERSION : 'latest'
                    echo "Deploying container version: ${versionToRun}"

                    // Stop & remove old container
                    bat '''
                    docker stop myapp1 || echo "No container to stop"
                    docker rm myapp1   || echo "No container to remove"
                    '''

                    // Run container
                    bat "docker run -d -p 5000:5000 --name myapp1 myapp1:${versionToRun}"
                }
            }
        }

        stage('Verify') {
            steps {
                echo "App should be running at http://localhost:5000"
                bat "docker ps"
            }
        }
    }

    post {
        success {
            echo "Pipeline finished successfully!"
        }
    }
}
