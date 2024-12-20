import requests
import json
import logging

# Configure logging
logging.basicConfig(filename='network.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Backend API URL
API_URL = 'http://127.0.0.1:5000/add-app'

def send_mock_data():
    # Mock data
    data = {
        'app_name': 'VirtualAndroidApp',
        'version': '1.0',
        'description': 'Mock data from virtual Android system'
    }

    try:
        response = requests.post(API_URL, json=data)
        if response.status_code == 201:
            logging.info(f'Successfully sent data: {data}')
            logging.info(f'Server Response: {response.json()}')
        else:
            logging.error(f'Failed to send data. Status Code: {response.status_code}, Response: {response.text}')
    except Exception as e:
        logging.error(f'Error connecting to the server: {e}')

def main():
    send_mock_data()

if __name__ == '__main__':
    main()
