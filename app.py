from data_processor import load_data, clean_data
from analytics_engine import generate_sales_summary
from rag_pipeline import build_vector_store, create_qa_chain

def main():
    df = load_data("data/global_superstore.csv")
    df = clean_data(df)

    summary_text = generate_sales_summary(df)

    vectorstore = build_vector_store(summary_text)
    qa_chain = create_qa_chain(vectorstore)

    print("AI Business Analyst Ready!")
    
    while True:
        query = input("\nAsk a question: ")
        response = qa_chain.run(query)
        print("\nAnswer:", response)

if __name__ == "__main__":
    main()
