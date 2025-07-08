[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/BDrNFAy8)
# **Code Copy Detector**

## **Task Description:**

You are provided with a dataset consisting of various programming solutions sourced from LeetCode. Each programming problem in the dataset has multiple independent implementations, showcasing different approaches and coding styles.

#### **Dataset Description**

The dataset consists of multiple programming problems, each accompanied by five independent solution implementations.

**Dataset Structure:**

*   **Column 1 – problem\_description:** A text field containing the full description of the problem along with examples.
    
*   **Columns 2–6 – solution\_1\_path to solution\_5\_path:** Each column contains the file path to a distinct solution implemented in Python that correctly solves the described problem.
    

#### **Objective**

Your goal is to develop a retrieval system capable of identifying and returning alternative solutions to a specific LeetCode problem when given a single solution as input.

*   **Input:** A single programming solution (code snippet).
    
*   **Output:** All other distinct solutions for the same problem from the dataset.
    

#### **Submission Guidelines**

*   A working retrieval system (source code and documented usage instructions). Clearly structure your repository for easy reproduction. Include scripts or notebooks for data preprocessing, training, retrieval, and evaluation.
    
*   A detailed technical report describing your methodology, evaluation strategy, comparative results, and analysis.

## Evaluation Metrics
1. Precision@K
   
2. Recall@K

3. F1-score@K
   
4. Accuracy

## What to try

You can start with the methods below or suggest your own method:

* Vector-based Token Similarity

* Keyword-based Retrieval

* Textual Retrieval with BM25 or TF-IDF

* Graph-based Approaches (Control Flow Graphs, Graph Meural Network)


# GitHub Classroom Guideline

**Step 1:** Accept the Assignment

* Click on the GitHub Classroom assignment [link](https://classroom.github.com/a/BDrNFAy8).

* Log in to your GitHub account (create an account if needed).

* Click Accept assignment. GitHub Classroom will create a private repository for you to work on the assignment.

**Step 2:** Clone the Repository

* Go to your newly created assignment repository.

* Click on the green Code button and copy the repository link.

* Open your terminal or Git Bash and type:
```bash
git clone [repository_link]
```
Navigate to the cloned folder:
```bash
cd [repository_name]
```
**Step 3:** Work on the Assignment

* Create, modify, and complete your assignment files directly in the cloned folder on your computer.

* Regularly commit your changes:

```bash
    git add .
    git commit -m "Descriptive message about your changes"
```
**Step 4:** Push Your Work to GitHub

* Once you've committed your changes, push them to GitHub:
```bash
git push origin main
```
**Step 5:** Verify Submission

* Visit your repository on GitHub to confirm your latest commits appear.

* Ensure that all required files are properly uploaded and displayed.
