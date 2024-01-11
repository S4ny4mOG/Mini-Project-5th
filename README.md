# EmailGPT
EmailGPT is a powerful web application designed to streamline your email management by efficiently classifying emails into spam and ham. But that's not all – for legitimate emails (ham), EmailGPT goes the extra mile by providing concise and helpful summaries.

## Access EmailGPT

Experience the power of EmailGPT by accessing it through your web browser. Follow these steps:

1. Ensure that you have cloned the repository and started the server as mentioned in the [Getting Started](#getting-started) section.

2. Open your web browser and navigate to the following URL:

   [EmailGPT](https://spamemailgpt.streamlit.app/)

3. Begin exploring EmailGPT's features, from accurate email classification to automatic summarization for legitimate emails (ham).

Feel free to customize EmailGPT according to your needs and manage your emails more efficiently!

## Features
Email Classification: EmailGPT employs advanced machine learning algorithms to accurately classify incoming emails as either spam or ham.
Summarization for Ham: For legitimate emails (ham), EmailGPT generates automatic summaries, saving you time and allowing for quick insights into the content.
User-Friendly Interface: The intuitive web interface makes it easy for users to interact with EmailGPT, providing a seamless experience.

## Table of Contents
- [Installation](#GettingStarted)
- [Usage](#usage)
- [Tech Stack](#TechnologiesUsed)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Getting Started
To get started with EmailGPT, follow these simple steps:

1.Clone the repository to your local machine:
```bash
  git clone https://github.com/s4ny4mOG/EmailGPT.git
```
2.Navigate to the project directory:
 ```bash
  cd EmailGPT
```
3.Install the necessary dependencies:
  ```
  pip install requirments.txt
  ```
4.Start the server:
  ```
  streamlit run main.py
  ```
5.Access EmailGPT through your web browser at 
```
http://localhost:8501/
```


## Usage
1.Upload your email dataset or enter the body of email into EmailGPT  .

2.Let EmailGPT work its magic! The application will classify emails and provide summaries for legitimate ones.

3.Manage your emails more efficiently, saving time and ensuring important information is easily accessible.

## Technologies Used
Frontend: streamlit
Machine Learning Model: Scikit-learn , Huggingface api for summarization.
Summarization: GPT-3.5

## Contributing
We welcome contributions from the community to enhance EmailGPT. If you have ideas, bug reports, or feature requests, feel free to open an issue or submit a pull request.

## License

EmailGPT is licensed under the [MIT License](LICENSE).

## Contact

If you have any questions or need assistance, feel free to reach out to us:
- Email: off.sanyam@gmail.com
