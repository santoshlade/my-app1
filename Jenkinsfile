pipeline {
    agent any

    // Parameters for versioning & rollback
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
                bat """
                echo Building Docker image ${params.APP_VERSION}
                docker build -t myapp1:${params.APP_VERSION} .
                docker tag myapp1:${params.APP_VERSION} myapp1:latest
                """
            }
        }

        stage('Deploy / Rollback') {
            steps {
                script {
                    def versionToRun = params.ROLLBACK ? params.APP_VERSION : 'latest'
                    echo "Deploying container version: ${versionToRun}"

                    // Windows-safe stop & remove
                    bat """
                    REM Check if container exists
                    docker ps -a --format "{{.Names}}" | findstr /I myapp1 >nul
                    if %ERRORLEVEL%==0 (
                        docker stop myapp1
                        docker rm myapp1
                    ) else (
                        echo No container to stop/remove
                    )

                    REM Run new container
                    docker run -d -p 5000:5000 --name myapp1 myapp1:${versionToRun}
                    """
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
        failure {
            echo "Pipeline failed! Check logs."
        }
    }
}
