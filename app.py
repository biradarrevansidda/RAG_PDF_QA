import streamlit as st
from src.pdf_processor import save_uploaded_file, load_and_split_pdf
from src.vector_store import create_vector_store, get_retriever
from src.rag_chain import answer_question

st.set_page_config(page_title="RAG PDF Q&A", page_icon="📚", layout="wide")

st.title("📚 RAG-Based PDF Question Answering")
st.write("Upload a PDF, process it, and ask questions about its contents.")

uploaded_file = st.file_uploader("Upload your PDF", type=["pdf"])

if uploaded_file:
    if st.button("Process PDF", type="primary"):
        with st.spinner("Processing PDF..."):
            try:
                pdf_path = save_uploaded_file(uploaded_file)
                documents, chunks = load_and_split_pdf(pdf_path)
                vector_store = create_vector_store(chunks)
                st.session_state.vector_store = vector_store
                st.session_state.retriever = get_retriever(vector_store)

                st.success(
                    f"PDF processed successfully! "
                    f"{len(documents)} pages and {len(chunks)} chunks created."
                )
            except Exception as e:
                st.error(f"Processing error: {e}")

if "retriever" in st.session_state:
    st.divider()
    st.subheader("Ask a question")

    question = st.text_input(
        "Enter your question:",
        placeholder="Example: What is Machine Learning?"
    )

    if st.button("Ask"):
        if not question.strip():
            st.warning("Please enter a question.")
        else:
            with st.spinner("Searching the PDF and generating answer..."):
                try:
                    answer, source_docs = answer_question(
                        question,
                        st.session_state.retriever
                    )

                    st.subheader("Answer")
                    st.write(answer)

                    st.subheader("Sources")
                    for i, doc in enumerate(source_docs, 1):
                        page = doc.metadata.get("page")
                        page_display = (
                            page + 1 if isinstance(page, int) else "Unknown"
                        )

                        with st.expander(
                            f"Source {i} — Page {page_display}"
                        ):
                            st.write(doc.page_content)

                except Exception as e:
                    st.error(f"Answer error: {e}")
