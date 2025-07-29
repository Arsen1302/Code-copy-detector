# Code Duplicate Finder

This is a Python tool I built to detect duplicate or highly similar code solutions among a large set of programming problem solutions. My goal was to make it easy to find alternative solutions to the same problem, even if they're written in different styles or use different approaches.

## Features
- Uses advanced transformer-based code embeddings for semantic similarity
- Lets you retrieve alternative solutions for any code snippet you provide
- Evaluates retrieval quality with metrics like Precision@K, Recall@K, F1@K, and Accuracy
- Efficiently handles large datasets of Python files

## About `embeddings.pkl`
The `embeddings.pkl` file is an automatically generated cache that stores the vector representations (embeddings) of all code solutions in your dataset. These embeddings are created using a pre-trained transformer model the first time you run the tool. Caching them in this file makes subsequent runs much faster, since the tool can load the embeddings directly instead of recomputing them every time. If you add or change files in your dataset, you may want to delete `embeddings.pkl` so it can be rebuilt with the new data.

## How It Works
1. I embed all code solutions using a pre-trained model
2. The tool indexes the solutions for fast similarity search
3. When you paste your code, it retrieves the most similar solutions from the dataset
4. It evaluates the results using standard information retrieval metrics

## Usage
1. Put your dataset in the `TestData/solutions` directory and make sure `TestData/test.csv` is present.
2. Run the main script:
   ```bash
   python main.py
   ```
3. Paste your code when prompted. The tool will find and display the most similar solutions from the dataset.

## Requirements
- Python 3.8+
- PyTorch
- transformers
- scikit-learn
- tqdm

To install dependencies, just run:
```bash
pip install -r requirements.txt
```

## Project Structure
- `main.py` – Main entry point
- `encoder.py` – Code embedding logic
- `retrieval.py` – Retrieval and search logic
- `utils.py` – Utility functions
- `TestData/` – Dataset directory
- `embeddings.pkl` – Cached code embeddings

---

## That's It!
Thanks for reading and checking out the project!
