#!/bin/bash
SERVICE_NAME=classattendance
export PYTHONPATH=`pwd`
api() {
    echo "Starting API..."
    API_PORT=${API_PORT:-8000}
    API_HOST=${API_HOST:-0.0.0.0}
    uvicorn demoservice.api.app:app --host ${API_HOST} --port ${API_PORT}
}

ui() {
    echo "Starting UI..."
    UI_PORT=${UI_PORT:-8088}
    streamlit run webapp/index.py --server.port ${UI_PORT} --client.showSidebarNavigation=False
}

# Check the command-line argument to determine action
case "$1" in
    api)
        api
        ;;
    webapp)
        ui
        ;;
    all)
        api
        ui
        ;;
    *)
        echo "Usage: $0 {api|ui|all}"
        exit 1
        ;;
esac

exit 0
