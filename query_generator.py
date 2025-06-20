
def generate_queries(model, question):
    prompt = (
        f"Could you generate 10 relevant and concise search queries for the following research question: {question}? "
        "Please answer only with the search queries, and separate it by commas without any additional text."
    )
    response = model.invoke(prompt)
    return [q.strip() for q in response.content.split(",")]
