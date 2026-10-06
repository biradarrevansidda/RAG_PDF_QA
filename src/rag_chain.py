from src.llm import get_llm


def answer_question(question, retriever):
    source_docs = retriever.invoke(question)

    # Remove duplicate sources based on page number
    unique_docs = []
    seen_pages = set()

    for doc in source_docs:
        page = doc.metadata.get("page")

        if page not in seen_pages:
            seen_pages.add(page)
            unique_docs.append(doc)

    context_parts = []

    for doc in unique_docs:
        page = doc.metadata.get("page")

        page_text = (
            f"Page {page + 1}: "
            if isinstance(page, int)
            else ""
        )

        context_parts.append(
            page_text + doc.page_content
        )

    context = "\n\n".join(context_parts)

    prompt = f"""
You are a PDF question-answering assistant.

Answer using ONLY the information in the provided context.

If the answer is not present in the context, say:
"I could not find that information in the uploaded PDF."

Context:
{context}

Question:
{question}

Give a clear and concise answer.
"""

    response = get_llm().invoke(prompt)

    return response.content, unique_docs