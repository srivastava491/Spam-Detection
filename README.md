# Spam Detection Software

This Spam Detection Software allows users to easily classify text as either spam or ham (not spam). The application is containerized using Docker for effortless deployment and distribution.

## Features

- **Text Classification:** Classify text to determine if it's spam or ham.
- **Containerized Deployment:** Deploy and run the application easily using Docker.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- Docker ([https://www.docker.com/](https://www.docker.com/))

## Getting Started

Follow these steps to get the Spam Detection Software up and running:

### 1. Pull the Docker Image

Pull the Docker image from Docker Hub using the following command:

```sh
docker pull aaravsrivastava491/spam_detection:tag
```
### 2. Run the Docker Container

Run the Docker container using the following command:

```bash
docker run -p 8501:8501 aaravsrivastava491/spam_detection:tag
```
### 3. Access the Application

Open your web browser and navigate to [http://localhost:8501](http://localhost:8501). You will see the input form where you can enter the text you want to classify.

**Usage:**
- Open your web browser and go to [http://localhost:8501](http://localhost:8501).
- Enter the text you want to classify in the input form.
- Click the "Classify" button.
- The application will display whether the text is classified as "Spam" or "Ham".

**Example:**
Here's an example of how to use the application:
- Navigate to [http://localhost:8501](http://localhost:8501) in your web browser.
- Enter the following text: "Congratulations! You've won a free lottery. Claim your prize now!"
- Click "Classify".
- The application will display: Spam.

## Contributing

If you'd like to contribute to this project, please fork the repository and submit a pull request. We welcome all contributions!

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For any questions or inquiries, please contact Aarav Srivastava at aaravsrivastava491.com.
