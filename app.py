import streamlit as st
from dotenv import load_dotenv

from PyPDF2 import PdfReader
from PyPDF2.errors import PdfReadError

from langchain_text_splitters import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings, HuggingFacePipeline
from langchain_community.vectorstores import FAISS

from transformers import pipeline

from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

from htmlTemplates import css


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="DocuMind",
    page_icon="📄",
    layout="centered"
)


# ============================================================
# PDF TEXT EXTRACTION
# ============================================================

def get_pdf_text(pdf_docs):

    text = ""

    for pdf in pdf_docs:

        try:
            pdf_reader = PdfReader(pdf)

            for page in pdf_reader.pages:

                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

        except PdfReadError:
            st.error(
                f"❌ Could not read '{pdf.name}'. "
                "The PDF may be corrupted or incomplete."
            )

        except Exception as e:
            st.error(
                f"❌ Error reading '{pdf.name}': {str(e)}"
            )

    return text


# ============================================================
# TEXT CHUNKS
# ============================================================

def get_text_chunks(text):

    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=400,
        chunk_overlap=50,
        length_function=len
    )

    chunks = text_splitter.split_text(text)

    return chunks


# ============================================================
# VECTOR DATABASE
# ============================================================

@st.cache_resource(show_spinner=False)
def create_embeddings():

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    return embeddings


def get_vectorstore(text_chunks):

    embeddings = create_embeddings()

    vectorstore = FAISS.from_texts(
        texts=text_chunks,
        embedding=embeddings
    )

    return vectorstore


# ============================================================
# LLM + CONVERSATION CHAIN
# ============================================================

@st.cache_resource(show_spinner=False)
def create_llm():

    hf_pipeline = pipeline(
        "text2text-generation",
        model="google/flan-t5-base",
        max_new_tokens=256,
        temperature=0.2
    )

    llm = HuggingFacePipeline(
        pipeline=hf_pipeline
    )

    return llm


def get_conversation_chain(vectorstore):

    llm = create_llm()

    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True,
        output_key="answer"
    )

    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(
            search_kwargs={
                "k": 3
            }
        ),
        memory=memory,
        return_source_documents=False
    )

    return conversation_chain


# ============================================================
# ASK QUESTION
# ============================================================

def handle_userinput(user_question):

    # --------------------------------
    # User message
    # --------------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_question
        }
    )

    # --------------------------------
    # Get AI response
    # --------------------------------

    with st.spinner("Thinking..."):

        try:

            response = st.session_state.conversation.invoke(
                {
                    "question": user_question
                }
            )

            answer = response.get(
                "answer",
                "I couldn't find an answer in the document."
            )

        except Exception as e:

            answer = (
                "Sorry, I encountered an error while "
                f"processing your question.\n\n`{str(e)}`"
            )

    # --------------------------------
    # Save AI response
    # --------------------------------

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )


# ============================================================
# RENDER CHAT
# ============================================================

def render_chat():

    for message in st.session_state.messages:

        if message["role"] == "user":

            with st.chat_message(
                "user",
                avatar="👤"
            ):
                st.markdown(
                    message["content"]
                )

        else:

            with st.chat_message(
                "assistant",
                avatar="D"
            ):
                st.markdown(
                    message["content"]
                )


# ============================================================
# MAIN
# ============================================================

def main():

    load_dotenv()

    # --------------------------------
    # Load CSS
    # --------------------------------

    st.markdown(
        css,
        unsafe_allow_html=True
    )

    # --------------------------------
    # Session State
    # --------------------------------

    if "conversation" not in st.session_state:
        st.session_state.conversation = None

    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "documents_processed" not in st.session_state:
        st.session_state.documents_processed = False

    # --------------------------------
    # Header
    # --------------------------------

    st.markdown(
        """
        <div class="documind-header">

            <div class="documind-logo">
                D
            </div>

            <div>
                <div class="documind-title">
                    DocuMind
                </div>

                <div class="documind-subtitle">
                    AI Document Assistant
                </div>
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    # --------------------------------
    # Sidebar
    # --------------------------------

    with st.sidebar:

        st.markdown(
            "## 📂 Documents"
        )

        st.markdown(
            "Upload one or more PDF documents "
            "to start chatting with them."
        )

        pdf_docs = st.file_uploader(
            "Upload PDF files",
            type=["pdf"],
            accept_multiple_files=True
        )

        st.divider()

        process_button = st.button(
            "🚀 Process Documents",
            use_container_width=True
        )

        if process_button:

            if not pdf_docs:

                st.warning(
                    "Please upload at least one PDF."
                )

            else:

                with st.spinner(
                    "Reading your documents..."
                ):

                    raw_text = get_pdf_text(
                        pdf_docs
                    )

                if not raw_text.strip():

                    st.error(
                        "❌ No readable text was found "
                        "in the uploaded PDF."
                    )

                else:

                    with st.spinner(
                        "Creating document embeddings..."
                    ):

                        text_chunks = get_text_chunks(
                            raw_text
                        )

                        if not text_chunks:

                            st.error(
                                "Could not create text chunks."
                            )

                        else:

                            vectorstore = get_vectorstore(
                                text_chunks
                            )

                    with st.spinner(
                        "Loading AI model..."
                    ):

                        st.session_state.conversation = (
                            get_conversation_chain(
                                vectorstore
                            )
                        )

                    st.session_state.messages = []

                    st.session_state.documents_processed = True

                    st.success(
                        "✅ Documents processed successfully!"
                    )

                    st.info(
                        f"Created {len(text_chunks)} "
                        "text chunks."
                    )

        # --------------------------------
        # Status
        # --------------------------------

        st.divider()

        if st.session_state.documents_processed:

            st.success(
                "🟢 Document assistant ready"
            )

        else:

            st.info(
                "⚪ Upload and process a PDF to begin."
            )

    # --------------------------------
    # Welcome screen
    # --------------------------------

    if not st.session_state.messages:

        st.markdown(
            """
            <div class="welcome">

                <div class="welcome-icon">
                    D
                </div>

                <h1>
                    How can I help with your document?
                </h1>

                <p>
                    Upload a PDF and ask questions
                    about its content.
                </p>

            </div>
            """,
            unsafe_allow_html=True
        )

    # --------------------------------
    # Existing Chat
    # --------------------------------

    render_chat()

    # --------------------------------
    # Chat Input
    # --------------------------------

    user_question = st.chat_input(
        "Ask something about your document..."
    )

    if user_question:

        if st.session_state.conversation is None:

            st.warning(
                "⚠️ Please upload and process "
                "your PDF first."
            )

        else:

            handle_userinput(
                user_question
            )

            # Rerun so the new messages
            # are rendered immediately
            st.rerun()


# ============================================================
# RUN
# ============================================================

if __name__ == "__main__":
    main()
