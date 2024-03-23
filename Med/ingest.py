from langchain.document_loaders import PyPDFLoader, DirectoryLoader, PDFMinerLoader 
from langchain.text_splitter import RecursiveCharacterTextSplitter 
from langchain.embeddings import SentenceTransformerEmbeddings 
import torch
import os
import numpy as np
from pinecone import Pinecone

pc = Pinecone(api_key="0f3718e3-1756-4a37-9583-839c535e296c")
index_name = "vectorindex"

persist_directory = "db"

def main():
    loader = PDFMinerLoader('Model/data.pdf')
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=500)
    texts = text_splitter.split_documents(documents)
    print(texts)
    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

    embedded_texts = [ embeddings.encode(text) for text in texts]
    tensor = torch.tensor(embedded_texts)
    storage = tensor.untyped_storage()
    print(embedded_texts)

    return


if __name__ == "__main__":
    main()