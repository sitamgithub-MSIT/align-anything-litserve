# Import necessary libraries
import torch
from PIL import Image
from transformers import AutoProcessor, LlavaForConditionalGeneration
import litserve as ls


class AlignDSVAPI(ls.LitAPI):
    """
    AlignDSVAPI is a subclass of ls.LitAPI that provides an interface to the Align-DS-V vision-language model.

    Methods:
        - setup(device): Called once at startup for the task-specific setup.
        - decode_request(request): Convert the request payload to model input.
        - predict(inputs): Uses the model to generate response from the input image and question.
        - encode_response(output): Convert the model output to a response payload.
    """

    def setup(self, device):
        """
        Set up the vision-language model for the task.
        """
        # Set up model and specify the device
        self.device = device
        model_id = "PKU-Alignment/Align-DS-V"
        self.model = LlavaForConditionalGeneration.from_pretrained(
            model_id, torch_dtype=torch.float16, low_cpu_mem_usage=True
        ).to(self.device)
        self.processor = AutoProcessor.from_pretrained(model_id)

    def decode_request(self, request):
        """
        Convert the request payload to model input.
        """
        # Extract the image path and question from the request
        image_path = request.get("image_path")
        question = request.get("question")

        # Load the image from the path
        image = Image.open(image_path)

        # Apply the chat template to the question and image
        conversation = [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": question},
                    {"type": "image"},
                ],
            },
        ]
        prompt = self.processor.apply_chat_template(
            conversation, add_generation_prompt=True
        )

        # Return the model input for inference
        return (
            self.processor(images=image, text=prompt, return_tensors="pt")
            .to(torch.float16)
            .to(self.model.device)
        )

    def predict(self, inputs):
        """
        Run inference and get the model output.
        """
        # Run inference to generate the output
        with torch.inference_mode():
            generate_ids = self.model.generate(
                **inputs, do_sample=False, max_new_tokens=4096
            )
            return self.processor.decode(
                generate_ids[0],
                skip_special_tokens=True,
            )

    def encode_response(self, output):
        """
        Convert the model output to a response payload.
        """
        # Return the text output in the response
        think = output.split("<think>")[1].split("</think>")[0].strip()
        answer = output.split("</think>")[1].strip()
        return {"think": think, "answer": answer}


if __name__ == "__main__":
    # Create an instance of the AlignDSVAPI and run the server
    api = AlignDSVAPI()
    server = ls.LitServer(api, track_requests=True)
    server.run(port=8000)
