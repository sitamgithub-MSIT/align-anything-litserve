# Align-DS-V LitServe

[![Open In Studio](https://pl-bolts-doc-images.s3.us-east-2.amazonaws.com/app-2/studio-badge.svg)](https://lightning.ai/sitammeur/studios/deploy-got-ocr2-model)

Align-DS-V, a vision-language model created by the PKU-Alignment team and HKUST, builds upon the DeepSeek-R1-Distill-Llama-8B architecture. The model demonstrates strong performance across diverse visual question-answering (VQA), chat, and reasoning tasks. This project shows how to create a self-hosted, private API that deploys [reasoning vision-language model](https://huggingface.co/PKU-Alignment/Align-DS-V) with LitServe, an easy-to-use, flexible serving engine for AI models built on FastAPI.

## Project Structure

The project is structured as follows:

- `server.py`: The file containing the main code for the web server.
- `client.py`: The file containing the code for client-side requests.
- `LICENSE`: The license file for the project.
- `README.md`: The README file that contains information about the project.
- `images`: The folder containing test images for the model.
- `assets`: The folder containing screenshots for working on the application.
- `.gitignore`: The file containing the list of files and directories to be ignored by Git.

## Tech Stack

- Python (for the programming language)
- PyTorch (for the deep learning framework)
- Hugging Face Transformers Library (for the model)
- LitServe (for the serving engine)

## Getting Started

To get started with this project, follow the steps below:

1. Run the server: `python server.py`
2. Upon running the server successfully, you will see uvicorn running on port 8000.
3. Open a new terminal window.
4. Run the client: `python client.py`

Now, you can see the model's output based on the input request. The model will generate answers based on the input image and question.

## Usage

The project can be used to serve the Align-DS-V vision-language model using LitServe. It allows you to input an image and a question and then get the model's answer. It suggests potential uses in various visual question-answering chats and reasoning tasks.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please raise an issue to discuss the changes you want to make. Once the changes are approved, you can create a pull request.

## License

This project is licensed under the [Apache-2.0 License](LICENSE).

## Contact

If you have any questions or suggestions about the project, please contact me on my GitHub profile.

Happy coding! 🚀
