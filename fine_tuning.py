from transformers import LlamaForCausalLM, LlamaTokenizer, Trainer, TrainingArguments
import torch
from preprocess_data import load_and_preprocess_data

def fine_tune_llama(model_name, dataset_path):
    # Load and preprocess the dataset
    scaled_features, df = load_and_preprocess_data(dataset_path)

    # Initialize Llama 3.1 model and tokenizer
    tokenizer = LlamaTokenizer.from_pretrained(model_name)
    model = LlamaForCausalLM.from_pretrained(model_name)
    
    # Prepare the dataset for fine-tuning (create input-output pairs)
    # For simplicity, assume the dataset is formatted appropriately
    
    # Define training arguments
    training_args = TrainingArguments(
        output_dir='./results',
        num_train_epochs=3,
        per_device_train_batch_size=4,
        save_steps=10_000,
        save_total_limit=2,
    )

    # Fine-tune model using Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=scaled_features  # Adjust this to your dataset structure
    )

    trainer.train()

    # Save the fine-tuned model
    model.save_pretrained('./fine_tuned_llama')
    tokenizer.save_pretrained('./fine_tuned_llama')

if __name__ == "__main__":
    fine_tune_llama('llama-3.1', 'path_to_spotify_dataset.csv')
