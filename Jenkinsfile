pipeline {

    agent any

    environment {
        DOCKER_IMAGE = 'monuser/microapp'
    }

    stages {

        stage('Charger .env') {

            steps {

                script {

                    def envFile = readFile('.env')

                    envFile.split('\n').each { line ->

                        line = line.trim()

                        if (line && !line.startsWith('#')) {

                            def parts = line.split('=', 2)

                            if (parts.size() == 2) {

                                def key = parts[0].trim()
                                def value = parts[1].trim()

                                env[key] = value
                            }
                        }
                    }

                    echo "Application : ${env.APP_NAME}"
                    echo "Port        : ${env.APP_PORT}"
                    echo "Version     : ${env.APP_VERSION}"
                }
            }
        }

        stage('Build Docker') {

            steps {

                script {

                    def image = "${env.DOCKER_IMAGE}:${env.APP_VERSION}"

                    echo "🐳 Construction de l'image : ${image}"

                    docker.build(image)
                }
            }
        }

        stage('Push Docker') {

            steps {

                withCredentials([
                    usernamePassword(
                        credentialsId: 'docker_hub',
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_PASSWORD'
                    )
                ]) {

                    sh '''
                        echo "$DOCKER_PASSWORD" | \
                        docker login \
                        -u "$DOCKER_USER" \
                        --password-stdin

                        docker push \
                        "$DOCKER_IMAGE:$APP_VERSION"
                    '''
                }
            }
        }

        stage('Deploy') {

            when {
                branch 'main'
            }

            steps {

                echo """
                🚀 Déploiement en production

                Application : ${env.APP_NAME}
                Version     : ${env.APP_VERSION}
                Port        : ${env.APP_PORT}
                Image       : ${env.DOCKER_IMAGE}:${env.APP_VERSION}
                """
            }
        }
    }

    post {

        success {
            echo "✅ Pipeline terminé avec succès"
        }

        failure {
            echo "❌ Pipeline en échec"
        }
    }
}