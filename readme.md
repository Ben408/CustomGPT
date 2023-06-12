# CustomGPT
Ask questions to your documents locally without an internet connection, no data leaves your execution environment at any point. \
No GPU is used, this is a CPU-based implementation. \
An internet connection is initially required to download the components but your data is processed locally.

Built with [LangChain](https://github.com/hwchase17/langchain), 
[GPT4All](https://github.com/nomic-ai/gpt4all), 
[LlamaCpp](https://github.com/ggerganov/llama.cpp), 
[Chroma](https://www.trychroma.com/),
[SentenceTransformers](https://www.sbert.net/),
[NLTK](http://www.nltk.org/nltk_data/),

# Environment Setup

Still need to fix requirements.txt

Download an LLM model and place it in /models
LLM: default to [ggml-gpt4all-j-v1.3-groovy.bin](https://gpt4all.io/models/ggml-gpt4all-j-v1.3-groovy.bin). 
Also testing with Vicuna non-quantized models

Rename `example.env` to `.env` and edit the variables:

```
MODEL_TYPE: supports LlamaCpp or GPT4All
PERSIST_DIRECTORY: the folder with your chroma vectorstore 
MODEL_PATH: Path to your GPT4All or other LLM
MODEL_N_CTX: Maximum token limit for the LLM model
EMBEDDINGS_MODEL_NAME: SentenceTransformers embeddings model name (see https://www.sbert.net/docs/pretrained_models.html)
TARGET_SOURCE_CHUNKS: The amount of chunks (sources) that will be used to answer a question
```

Add your source documents to /source documents.

Supported formats:
   - `.csv`: CSV,
   - `.docx`: Word XML Document,
   - `.doc`: Word Legacy Document,
   - `.enex`: EverNote,
   - `.eml`: Email,
   - `.epub`: EPub,
   - `.html`: HTML,
   - `.md`: Markdown,
   - `.msg`: Outlook Message,
   - `.odt`: Open Document Text,
   - `.pdf`: PDF (Portable Document Format),
   - `.pptx` : PowerPoint XML Document,
   - `.ppt` : PowerPoint Legacy Document,
   - `.txt`: Text file (UTF-8),****

From the shell/terminal, run
```shell
python ingest.py
```
You can ingest any number of documents, these will be accumulated in the local embeddings database. \
Ingestion will take 10-30 seconds per document, depending on the size of the document. 

You can use the hugging face embeddings or the instruct embeddings in injest.py. 
```shell
    # Create embeddings
    embeddings = HuggingFaceEmbeddings(model_name=embeddings_model_name)
    # Change the embedding type here to the instruct embeddings if you are running into issues.
```
You will want to test with a set of the content you will import and also test by adjusting the chunk_size based on the content of the documents.

Adjust the chunk size by modifying 
```shell
chunk_size = 500
chunk_overlap = 100
```
as needed in the script based on the content files being ingested.

The ingestor script creates a `db` folder containing the local chroma vectorstore, index, etc. \ 
To re-create the database, delete the `db` folder.

NOTE: There seems to be some corrpution problem with the punkt archive on http://www.nltk.org/nltk_data/, so find it elsewhere and put it somewhere locally available to the environment.
