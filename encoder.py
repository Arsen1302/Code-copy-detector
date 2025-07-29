import re
import torch
from transformers import AutoTokenizer, T5EncoderModel

class CodeEncoder:
    def __init__(self, model_name="Salesforce/codet5p-220m"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = T5EncoderModel.from_pretrained(model_name)
        self.device = torch.device(
            "mps" if torch.backends.mps.is_available() else
            "cuda" if torch.cuda.is_available() else "cpu"
        )
        self.model.to(self.device).eval()

    def normalize_code(self, code: str) -> str:
        code = re.sub(r'#.*', '', code)
        code = re.sub(r'\s+', ' ', code)
        code = re.sub(r'".*?"|\'.*?\'', 'STR', code)
        code = re.sub(r'\d+', 'NUM', code)
        return code.strip()

    def encode(self, code: str) -> torch.Tensor:
        code = self.normalize_code(code)
        inputs = self.tokenizer(code, return_tensors="pt", padding="max_length", truncation=True, max_length=512)
        inputs = {k: v.to(self.device) for k, v in inputs.items()}
        with torch.no_grad():
            outputs = self.model(**inputs, output_hidden_states=True)
            last = outputs.hidden_states[-1][:, 0, :]
            second_last = outputs.hidden_states[-2][:, 0, :]
            pooled = (last + second_last) / 2
        return pooled.cpu()
