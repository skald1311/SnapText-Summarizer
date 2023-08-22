from transformers import PegasusForConditionalGeneration, PegasusTokenizer
# from transformers import BartForConditionalGeneration, BartTokenizer
import torch

def main(text):
    # # Get input from text file
    # with open("input.txt", "r") as file:
    #     text = file.read()
    
    # Google's Pegasus: summarization
    model_name = "google/pegasus-cnn_dailymail"  # Model: Pegasus
    device = "cuda" if torch.cuda.is_available() else "cpu"
    tokenizer = PegasusTokenizer.from_pretrained(model_name)  # Load pretrained tokenizer
    model = PegasusForConditionalGeneration.from_pretrained(model_name).to(device)  # Define model

    tokens = tokenizer(text, truncation=True, padding="longest", return_tensors="pt").to(device)  # Tokenize input
    
    encoded_summary = model.generate(**tokens, max_new_tokens=150) # Summarize encoded
    summary = tokenizer.decode(encoded_summary[0], skip_special_tokens= True)  # Decode
    summary = summary.replace("<n>", " ")
    summary = summary.replace("  ", " ")
    return summary

    # # Google's Bart: fine-tuned to paraphrase #
    # bart = BartForConditionalGeneration.from_pretrained('eugenesiow/bart-paraphrase')
    # device1 = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    # bart = bart.to(device1)
    # bart_tokenizer = BartTokenizer.from_pretrained('eugenesiow/bart-paraphrase')
    # batch = bart_tokenizer(summary, return_tensors='pt')
    # generated_ids = bart.generate(batch['input_ids'], max_new_tokens=150)
    # generated_sentence = bart_tokenizer.batch_decode(generated_ids, skip_special_tokens=True)
    # print(f"Abstractive Summary: {generated_sentence[0]}")
    
