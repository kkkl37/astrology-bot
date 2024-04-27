from transformers import LlamaForCausalLM, LlamaTokenizer
import torch
import re
import os

class LlaMA2:
    """
    A class for generating results given questions using a LLaMA-2 model.
    """
    def __init__(self, checkpoint, max_seq_len = 512, device='cuda:0',API_KEY=None):
        self.device = torch.device(device if torch.cuda.is_available() else 'cpu')
        self.tokenizer = LlamaTokenizer.from_pretrained(checkpoint)
        self.tokenizer.add_special_tokens({'pad_token': '[PAD]'})
        if API_KEY is not None:
            self.model = LlamaForCausalLM.from_pretrained(checkpoint,torch_dtype=torch.float16, token = API_KEY).to(self.device)  
        else:
            self.model = LlamaForCausalLM.from_pretrained(checkpoint,torch_dtype=torch.float16).to(self.device)
        self.max_seq_len = max_seq_len

    def predict(self, text):
        inputs = self.tokenizer.encode(text, return_tensors='pt', max_length=self.max_seq_len, truncation=True)
        inputs = inputs.to(self.device)
        
        # Calculate the maximum length for the model generation
        output_max_length = len(inputs[0]) + self.max_seq_len
        
        outputs = self.model.generate(inputs, max_length=output_max_length)
        full_output =  self.tokenizer.decode(outputs[0], skip_special_tokens=True)

        # post-process the model outputs to find a proper answer
        answer = full_output.split('Context:')[1]
        answer_prefix = "Response to the Question:"
        start = answer.find(answer_prefix)

        # Extract the answer
        if start != -1:
            start += len(answer_prefix)
            answer = answer[start:].strip()
        else:
            answer = "Please try again."
        
        return answer, full_output, text