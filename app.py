from flask import Flask, request, render_template, jsonify
import torch
from transformers import GPT2Tokenizer
from model import SimpleGPT2SequenceClassifier 

app = Flask(__name__)


model_new = SimpleGPT2SequenceClassifier(hidden_size=768, num_classes=2, max_seq_len=128, gpt_model_name="gpt2")
model_new.load_state_dict(torch.load("predict.pt"))
model_new.eval()

tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
tokenizer.padding_side = "left"
tokenizer.pad_token = tokenizer.eos_token

labels_map = {
    0: "non-suicidal",
    1: "suicidal",
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')  

    if request.method == 'POST':
        text_from_request = request.form['text']  
        fixed_text = " ".join(text_from_request.lower().split())
        model_input = tokenizer(fixed_text, padding='max_length', max_length=128, truncation=True, return_tensors="pt")
        mask = model_input['attention_mask'].cpu()
        input_id = model_input["input_ids"].squeeze(1).cpu()
        output = model_new(input_id, mask)
        pred_label = labels_map[output.argmax(dim=1).item()]
        return jsonify({"prediction": pred_label})

if __name__ == '__main__':
    app.run(debug=True)
