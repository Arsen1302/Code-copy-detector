from typing import List, Dict
import os, csv, numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from utils import tokenize_code, cosine_score, euclidean_score, jaccard_similarity, tfidf_similarity


class RetrievalSystem:
    def __init__(self, csv_path: str, code_base_dir: str):
        self.csv_path = csv_path
        self.code_base_dir = code_base_dir
        self.solution_paths: List[str] = []
        self.solution_contents: List[str] = []
        self.solution_index_to_problem: List[int] = []
        self.problem_to_solution_paths: Dict[int, List[str]] = {}
        self.path_to_problem: Dict[str, int] = {}
        self.problems: List[str] = []
        self.vectorizer: TfidfVectorizer = None
        self.tfidf_matrix = None

    def load_dataset(self):
        with open(self.csv_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)
            for problem_id, row in enumerate(reader):
                problem_name = row[0]
                self.problems.append(problem_name)
                paths = [p.strip() for p in row[1:] if p.strip()]
                self.problem_to_solution_paths[problem_id] = [os.path.basename(p) for p in paths]

                for p in paths:
                    fname = os.path.basename(p)
                    full_path = os.path.join(self.code_base_dir, fname)
                    code = ""
                    if os.path.exists(full_path):
                        with open(full_path, 'r', encoding='utf-8') as code_file:
                            code = code_file.read()
                    self.solution_paths.append(fname)
                    self.solution_contents.append(code)
                    self.solution_index_to_problem.append(problem_id)
                    self.path_to_problem[fname] = problem_id

    def preprocess(self):
        self.vectorizer = TfidfVectorizer(
            tokenizer=tokenize_code,
            token_pattern=None,
            lowercase=False,
            ngram_range=(1, 4),
            sublinear_tf=True,
            max_df=0.95,
            min_df=2
        )
        self.tfidf_matrix = self.vectorizer.fit_transform(self.solution_contents)

    def retrieve(self, input_code: str):
        vec = self.vectorizer.transform([input_code])
        scores = cosine_similarity(vec, self.tfidf_matrix)[0]
        top_idx = np.argmax(scores)
        problem_id = self.solution_index_to_problem[top_idx]

        return {
            "description": self.problems[problem_id],
            "matched_path": self.solution_paths[top_idx],
            "matched_code": self.solution_contents[top_idx],
            "other_paths": [p for p in self.problem_to_solution_paths[problem_id] if p != self.solution_paths[top_idx]]
        }

