from encoder import CodeEncoder
from utils import load_python_files, build_embeddings, evaluate_metrics,combine_similarity
from retrieval import RetrievalSystem

def multiline_input(prompt="Paste your solution code below. When done, type 'END' on a new line:\n"):
    print(prompt)
    lines = []
    while True:
        line = input()
        if line.strip() == "END":
            break
        lines.append(line)
    return "\n".join(lines)

def main():
    top_k = 5
    dataset_dir = "TestData/solutions"
    csv_file = "TestData/test.csv"

    dataset = load_python_files(dataset_dir)
    encoder = CodeEncoder()
    embeddings = build_embeddings(dataset, encoder)

    input_code = multiline_input()

    if not input_code.strip():
        print("Empty input detected. Exiting.")
        return

    retrieval_system = RetrievalSystem(csv_file, dataset_dir)
    retrieval_system.load_dataset()
    retrieval_system.preprocess()

    matched = retrieval_system.retrieve(input_code)
    input_emb = encoder.encode(matched["matched_code"])
    code_lookup = dict(dataset)

    similar = [
        (fname, combine_similarity(matched["matched_code"], code_lookup.get(fname, ""), input_emb, emb, retrieval_system.vectorizer))
        for fname, emb in embeddings
    ]
    similar.sort(key=lambda x: x[1], reverse=True)

    top_k_files = [fname for fname, _ in similar[:5]]
    relevant_files = set(matched["other_paths"] + [matched["matched_path"]])
    metrics = evaluate_metrics(top_k_files, relevant_files, k=top_k)

    print(f"\n📊 Evaluation Metrics 5:")
    for metric, value in metrics.items():
        print(f"{metric}: {value:.4f}")

    print("\n🔍 Top similar files to the matched solution:")
    for i, (fname,score) in enumerate(similar[:top_k]):
        mark = "✅" if fname in relevant_files else "📄"
        print(f"{i+1:2d}. {mark} {fname:<30}")

if __name__ == "__main__":
    main()