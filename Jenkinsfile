pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Jenkins pulls repo automatically, so nothing required here
                echo 'Checked out source code'
            }
        }

        stage('Build') {
            steps {
                sh '''
                mkdir -p build
                zip -r build/myapp.zip .
                '''
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -m unittest discover tests'
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                mkdir -p /tmp/deploy
                cp build/myapp.zip /tmp/deploy/
                echo "Deployed at $(date)" > /tmp/deploy/deploy.log
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'build/**', fingerprint: true
        }
    }
}
