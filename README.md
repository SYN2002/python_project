# MongoDB Connection Setup

This repository contains a Python script to establish a secure connection to a MongoDB database using the `pymongo` library. The script loads the MongoDB connection string from an environment file (`.env`) to enhance security and flexibility in managing sensitive information.

## Features

- **Secure Connection**: The script securely connects to a MongoDB database using TLS encryption and allows invalid certificates.
- **Flexible Configuration**: MongoDB connection parameters, such as the connection URI and authentication details, are stored in a `.env` file, allowing for easy configuration changes.
- **Error Handling**: The script includes error handling to ensure that the MongoDB URI is properly configured and present in the environment variables.
- **Ease of Use**: By following the instructions provided in this README, users can quickly set up and run the script to establish a connection to their MongoDB database.

## Getting Started

### Prerequisites

Before running the script, ensure that you have the following installed:

- Python (version 3.6 or higher)
- `pymongo` library (`pip install pymongo`)
- `python-dotenv` library (`pip install python-dotenv`)

## Installation

1. **Clone the Repository**: Clone this repository to your local machine using the following command:

    ```bash
    git clone https://github.com/your_username/mongodb-connection-setup.git
    ```

2. **Install Dependencies**: Navigate to the project directory and install the required dependencies using pip:

    ```bash
    cd mongodb-connection-setup
    pip install -r requirements.txt
    ```

## Usage

1. **Create a `.env` File**: Create a `.env` file in the root of the project directory and add your MongoDB connection string in the following format:

    ```env
    MONGODB_URI=mongodb://username:<password>@host1:port1,host2:port2,host3:port3/?replicaSet=your_replica_set&authSource=admin&tls=true&tlsAllowInvalidCertificates=true&tlsDisableOCSPEndpointCheck=true
    ```

    Replace `username`, `password`, `host1`, `port1`, `host2`, `port2`, `host3`, `port3`, `your_replica_set` with your MongoDB credentials and connection details.

2. **Run the Script**: Execute the Python script to establish a connection to your MongoDB database:

    ```bash
    python mongodb_connection.py
    ```

3. **Verify Connection**: Check the terminal output for any errors and ensure that the connection to the MongoDB database is established successfully.

# YouTube Manager App

This is a simple YouTube manager app that allows you to perform various operations on your videos.

### Options:

1. **List all videos**: View all the videos in your collection.
2. **Add a new video**: Add a new video to your collection.
3. **Update a video**: Update the details of an existing video.
4. **Delete a video**: Delete a video from your collection.
5. **Exit the app**: Quit the YouTube manager app.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

