## Run the api locally:


    export AWS_ACCESS_KEY_ID=abc && export AWS_SECRET_ACCESS_KEY=abc && export AWS_DEFAULT_REGION=eu-west-1 && export TABLE_NAME="local-tasks-api-table" && export DYNAMODB_URL=http://localhost:9999 && export ALLOWED_ORIGINS=*
    
    docker-compose up -d
    
    poetry run uvicorn main:app --reload