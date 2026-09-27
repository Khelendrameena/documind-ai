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
# CONFIG
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

    return text_splitter.split_text(text)


# ============================================================
# EMBEDDINGS
# ============================================================

@st.cache_resource
def create_embeddings():

    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )


# ============================================================
# VECTOR STORE
# ============================================================

def get_vectorstore(text_chunks):

    embeddings = create_embeddings()

    vectorstore = FAISS.from_texts(
        text_chunks,
        embedding=embeddings
    )

    return vectorstore


# ============================================================
# LLM
# ============================================================

@st.cache_resource
def create_llm():

    hf_pipeline = pipeline(
        "text2text-generation",
        model="google/flan-t5-base",
        max_new_tokens=256,
        temperature=0.2
    )

    return HuggingFacePipeline(
        pipeline=hf_pipeline
    )


# ============================================================
# CONVERSATION CHAIN
# ============================================================

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
            search_kwargs={"k": 3}
        ),
        memory=memory,
        return_source_documents=False
    )

    return conversation_chain


# ============================================================
# CHAT RESPONSE
# ============================================================

def handle_userinput(user_question):

    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_question
    })

    try:

        with st.spinner("Thinking..."):

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
            "Sorry, something went wrong while "
            "processing your question.\n\n"
            f"Error: `{str(e)}`"
        )

    # Save assistant response
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })


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
                avatar="📄"
            ):
                st.markdown(
                    message["content"]
                )


# ============================================================
# MAIN
# ============================================================

def main():

    load_dotenv()

    # --------------------------------------------------------
    # CSS
    # --------------------------------------------------------

    st.markdown(
        css,
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # SESSION STATE
    # --------------------------------------------------------

    if "conversation" not in st.session_state:
        st.session_state.conversation = None

    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "documents_processed" not in st.session_state:
        st.session_state.documents_processed = False

    # --------------------------------------------------------
    # HEADER
    # --------------------------------------------------------

    # IMPORTANT:
    # No custom HTML here.
    # This avoids raw HTML rendering problems.

    col1, col2 = st.columns(
        [0.12, 0.88],
        vertical_alignment="center"
    )

    with col1:

        st.markdown(
            """
            <div class="logo-box">
                D
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            '<div class="app-title">DocuMind</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="app-subtitle">AI Document Assistant</div>',
            unsafe_allow_html=True
        )

    st.divider()

    # --------------------------------------------------------
    # SIDEBAR
    # --------------------------------------------------------

    with st.sidebar:

        st.title("📂 Documents")

        st.caption(
            "Upload PDF files and ask questions "
            "about their content."
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

                # --------------------------------------------
                # Extract
                # --------------------------------------------

                with st.spinner(
                    "Reading documents..."
                ):

                    raw_text = get_pdf_text(
                        pdf_docs
                    )

                if not raw_text.strip():

                    st.error(
                        "No readable text was found "
                        "in the uploaded PDF."
                    )

                else:

                    # ----------------------------------------
                    # Chunks
                    # ----------------------------------------

                    with st.spinner(
                        "Splitting document..."
                    ):

                        text_chunks = get_text_chunks(
                            raw_text
                        )

                    if not text_chunks:

                        st.error(
                            "Could not create text chunks."
                        )

                    else:

                        # ------------------------------------
                        # Vector database
                        # ------------------------------------

                        with st.spinner(
                            "Creating embeddings..."
                        ):

                            vectorstore = get_vectorstore(
                                text_chunks
                            )

                        # ------------------------------------
                        # Conversation chain
                        # ------------------------------------

                        with st.spinner(
                            "Loading AI model..."
                        ):

                            st.session_state.conversation = (
                                get_conversation_chain(
                                    vectorstore
                                )
                            )

                        # Clear old conversation
                        st.session_state.messages = []

                        st.session_state.documents_processed = True

                        st.success(
                            "✅ Documents processed!"
                        )

                        st.caption(
                            f"{len(text_chunks)} text chunks created."
                        )

        st.divider()

        if st.session_state.documents_processed:

            st.success(
                "🟢 DocuMind is ready"
            )

        else:

            st.info(
                "Upload and process a PDF first."
            )

    # --------------------------------------------------------
    # WELCOME
    # --------------------------------------------------------

    if not st.session_state.messages:

        st.markdown(
            """
            <div class="welcome-box">

                <div class="welcome-icon">
                    📄
                </div>

                <h2>
                    Chat with your documents
                </h2>

                <p>
                    Upload a PDF and ask questions
                    about its content.
                </p>

            </div>
            """,
            unsafe_allow_html=True
        )

    # --------------------------------------------------------
    # CHAT HISTORY
    # --------------------------------------------------------

    render_chat()

    # --------------------------------------------------------
    # CHAT INPUT
    # --------------------------------------------------------

    user_question = st.chat_input(
        "Ask something about your document..."
    )

    if user_question:

        if st.session_state.conversation is None:

            st.warning(
                "⚠️ Please upload and process "
                "a PDF first."
            )

        else:

            handle_userinput(
                user_question
            )

            st.rerun()


# ============================================================
# RUN
# ============================================================

if __name__ == "__main__":
    main()
