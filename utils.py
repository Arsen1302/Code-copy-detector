import os
import re
import pickle
import numpy as np
from tqdm import tqdm
from typing import List, Tuple, Set
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

def tokenize_code(code: str) -> List[str]:
    code = re.sub(r'#.*', '', code)
    code = re.sub(r'(\'\'\'[\s\S]*?\'\'\'|\"\"\"[\s\S]*?\"\"\"|\'.*?\'|\".*?\")', '', code)
    return re.findall(r'\w+|[^\w\s]', code)

def load_python_files(folder_path: str, max_files=None) -> List[Tuple[str, str]]:
    files = sorted([f for f in os.listdir(folder_path) if f.endswith(".py")],
                   key=lambda s: [int(t) if t.isdigit() else t.lower() for t in re.split(r'(\d+)', s)])
    dataset = []
    for fname in tqdm(files[:max_files], desc="Loading Python files"):
        with open(os.path.join(folder_path, fname), 'r', encoding='utf-8') as f:
            dataset.append((fname, f.read()))
    return dataset

def build_embeddings(dataset: List[Tuple[str, str]], encoder, cache_path="embeddings.pkl") -> List[Tuple[str, np.ndarray]]:
    if os.path.exists(cache_path):
        with open(cache_path, 'rb') as f:
            return pickle.load(f)
    embeddings = []
    for fname, code in tqdm(dataset, desc="Generating embeddings"):
        vec = encoder.encode(code)
        embeddings.append((fname, vec))
    with open(cache_path, 'wb') as f:
        pickle.dump(embeddings, f)
    return embeddings

def cosine_score(v1: np.ndarray, v2: np.ndarray) -> float:
    v1 = np.squeeze(v1)
    v2 = np.squeeze(v2)
    return cosine_similarity([v1], [v2])[0][0]

def jaccard_similarity(code1: str, code2: str) -> float:
    tokens1 = set(tokenize_code(code1))
    tokens2 = set(tokenize_code(code2))
    union = tokens1 | tokens2
    if not union:
        return 0.0
    return len(tokens1 & tokens2) / len(union)

def euclidean_score(v1: np.ndarray, v2: np.ndarray) -> float:
    v1 = np.squeeze(v1)
    v2 = np.squeeze(v2)
    return 1 / (1 + np.linalg.norm(v1 - v2))

def tfidf_similarity(input_code: str, candidate_code: str, vectorizer: TfidfVectorizer) -> float:
    vecs = vectorizer.transform([input_code, candidate_code])
    return cosine_similarity(vecs[0], vecs[1])[0][0]

def evaluate_metrics(predicted: List[str], relevant: Set[str], k: int = 5):
    top_k = predicted[:k]
    tp = sum(1 for f in top_k if f in relevant)
    fp = sum(1 for f in top_k if f not in relevant)
    fn = len(relevant) - tp

    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0
    accuracy = tp / len(top_k) if len(top_k) > 0 else 0

    return {
        "precision@k": precision,
        "recall@k": recall,
        "f1@k": f1,
        "accuracy@k": accuracy
    }

def combine_similarity(input_code: str,
                       candidate_code: str,
                       input_vec: np.ndarray,
                       candidate_vec: np.ndarray,
                       vectorizer: TfidfVectorizer,
                       weights=(0.5, 0.3, 0.2)) -> float:
    input_vec = np.squeeze(input_vec)
    candidate_vec = np.squeeze(candidate_vec)

    bert_score = cosine_score(input_vec, candidate_vec)
    tfidf_score = tfidf_similarity(input_code, candidate_code, vectorizer)
    euc_score = euclidean_score(input_vec, candidate_vec)
    jaccard_score = jaccard_similarity(input_code, candidate_code)

    alpha = np.clip(1 / (1 + np.exp(-bert_score)), 0.1, 0.9)

    sim = weights[0] * (alpha * bert_score + (1 - alpha) * tfidf_score) \
        + weights[1] * euc_score \
        + weights[2] * jaccard_score

    return sim
