pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checked out source code'
            }
        }

        stage('Build') {
            steps {
                bat '''
                if not exist build mkdir build
                powershell Compress-Archive -Path * -DestinationPath build\\myapp.zip -Force
                '''
            }
        }

        stage('Test') {
            steps {
                bat 'python -m unittest discover tests'
            }
        }

        stage('Deploy') {
            steps {
                bat '''
                if not exist C:\\temp\\deploy mkdir C:\\temp\\deploy
                copy build\\myapp.zip C:\\temp\\deploy\\
                echo Deployed at %date% %time% > C:\\temp\\deploy\\deploy.log
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
