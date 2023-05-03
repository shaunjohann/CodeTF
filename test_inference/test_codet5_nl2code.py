import sys
from pathlib import Path
sys.path.append(str(Path(".").absolute().parent))
# sys.path.append("../")
import torch
from codetf.models import load_model
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = load_model(model_name="codegen_nl2code", model_type="base", dataset="codexglue", task="sum", language="python", is_eval=True, device=device)


prompts = "# check if a string is in valid format"
code_snippets = model.predict([prompts])

print(code_snippets)