# 📚 Chat with Your PDFs

A local **PDF question-answering application** built with **Streamlit,
LangChain, Hugging Face Transformers, Sentence Transformers, and
FAISS**.

The application allows users to upload one or more PDF documents,
process their contents, and ask questions about the uploaded documents
through a conversational chat interface.

## ✨ Features

-   📄 Upload multiple PDF documents
-   🔎 Extract text from PDF files
-   ✂️ Split extracted text into smaller overlapping chunks
-   🧠 Generate semantic embeddings using
    `sentence-transformers/all-MiniLM-L6-v2`
-   🗂️ Store and retrieve document vectors using FAISS
-   🤖 Generate answers using Google's `flan-t5-base` model through
    Hugging Face Transformers
-   💬 Maintain conversational context using LangChain's
    `ConversationBufferMemory`
-   🔗 Use LangChain's `ConversationalRetrievalChain` to combine
    retrieval with question answering
-   🎨 Streamlit-based chat interface with custom user and bot message
    styling

## 🏗️ How It Works

The application follows a Retrieval-Augmented Generation (RAG)-style
workflow:

``` text
                 ┌─────────────────┐
                 │   Upload PDFs   │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │ Extract PDF     │
                 │ Text (PyPDF2)   │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │ Split Text into │
                 │ Chunks           │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │ Generate        │
                 │ Embeddings      │
                 │ MiniLM-L6-v2    │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │ FAISS Vector    │
                 │ Store            │
                 └────────┬────────┘
                          │
             User Question
                          │
                          ▼
                 ┌─────────────────┐
                 │ Retrieve        │
                 │ Relevant Chunks │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │ FLAN-T5 Base    │
                 │ Question Answer │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │ Conversational  │
                 │ Response        │
                 └─────────────────┘
```

## 🧩 Project Structure

``` text
.
├── app.py
├── htmlTemplates.py
├── requirements.txt
├── .python-version
├── .gitignore
└── README.md
```

### `app.py`

The main Streamlit application.

It contains functions for:

-   Extracting text from PDFs
-   Splitting text into chunks
-   Creating the FAISS vector store
-   Initializing the Hugging Face language model
-   Creating the conversational retrieval chain
-   Handling user questions
-   Building the Streamlit interface

The application uses a chunk size of `1000` characters with an overlap
of `200` characters.

### `htmlTemplates.py`

Contains the CSS and HTML templates used to display user and bot
messages in the chat interface.

### `requirements.txt`

Contains the Python dependencies required to run the application.

### `.python-version`

Specifies Python `3.13` for the project environment.

### `.gitignore`

Contains common Python, virtual-environment, build, cache, and IDE files
that should not be committed to the repository.

## 🛠️ Tech Stack

  Technology                  Purpose
  --------------------------- ---------------------------------------
  Python                      Application development
  Streamlit                   Web interface
  PyPDF2                      PDF text extraction
  LangChain                   Retrieval and conversational pipeline
  Hugging Face Transformers   Text generation
  FLAN-T5 Base                Language model
  Sentence Transformers       Text embeddings
  FAISS                       Vector similarity search
  python-dotenv               Environment-variable loading

## 🚀 Installation

### 1. Clone the repository

``` bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd <PROJECT_DIRECTORY>
```

### 2. Create a virtual environment

``` bash
python -m venv .venv
```

Activate it on Windows:

``` bash
.venv\Scripts\activate
```

On macOS/Linux:

``` bash
source .venv/bin/activate
```

### 3. Install dependencies

``` bash
pip install -r requirements.txt
```

## ▶️ Run the Application

Start the Streamlit application with:

``` bash
streamlit run "app.py"
```

Streamlit will provide a local URL where the application can be opened
in your browser.

## 📖 Usage

1.  Launch the application.
2.  Open the **Your documents** section in the sidebar.
3.  Upload one or more PDF files.
4.  Click **Process**.
5.  Wait for the documents to be processed.
6.  Enter a question in the chat input.
7.  The application retrieves relevant information from the processed
    documents and generates a response.
8.  Continue asking follow-up questions while the conversational memory
    is active.

## 🔍 Retrieval Pipeline

### 1. PDF Text Extraction

`PyPDF2` reads each uploaded PDF and extracts text from its pages.

### 2. Text Chunking

The extracted text is divided into chunks using LangChain's
`CharacterTextSplitter`.

Current configuration:

``` text
Chunk size:    1000 characters
Chunk overlap: 200 characters
Separator:     newline
```

The overlap helps preserve context between neighboring chunks.

### 3. Embeddings

Each text chunk is converted into a numerical vector using:

``` text
sentence-transformers/all-MiniLM-L6-v2
```

These embeddings represent the semantic meaning of the text and allow
relevant document sections to be retrieved for a question.

### 4. FAISS Vector Store

The generated embeddings are stored in a FAISS vector index.

When a user asks a question, the vector store is used as the retriever
to find relevant document chunks.

### 5. Language Model

The project uses:

``` text
google/flan-t5-base
```

through the Hugging Face Transformers pipeline for
`text2text-generation`.

### 6. Conversational Retrieval

LangChain's `ConversationalRetrievalChain` connects:

``` text
User Question
      ↓
Retriever
      ↓
Relevant Document Chunks
      ↓
FLAN-T5
      ↓
Answer
```

Conversation history is maintained using `ConversationBufferMemory`.

## 📦 Main Dependencies

The project uses the following major packages:

``` text
streamlit
PyPDF2
faiss-cpu
langchain
langchain-community
langchain-text-splitters
langchain-huggingface
transformers
sentence-transformers
huggingface-hub
python-dotenv
```

Exact versions for several packages are specified in `requirements.txt`.

## ⚠️ Limitations

-   The application relies on PDF text extraction, so scanned/image-only
    PDFs may not produce useful text without OCR.
-   Processing and generation are performed locally and can require
    significant CPU/RAM resources.
-   The application currently creates the FAISS vector store during the
    document-processing step rather than persisting it for future
    sessions.
-   The language model is `flan-t5-base`, so response quality depends on
    the capabilities of that model.
-   The current implementation does not expose document/page citations
    in the generated answers.
-   The application processes the uploaded documents for the current
    Streamlit session.


## 📁 Environment Variables

The application calls `load_dotenv()` and can therefore load environment
variables from a `.env` file.

At present, the core PDF-processing and language-model pipeline shown in
the project does not require an API key because the embedding model and
FLAN-T5 model are loaded through the local Hugging Face/Transformers
stack.

Do **not** commit secrets or `.env` files to Git. The project's
`.gitignore` already includes `.env`.

------------------------------------------------------------------------

### Built With

**Python • Streamlit • LangChain • Hugging Face • Sentence Transformers
• FAISS**
#   d o c u m i n d - a i  
 