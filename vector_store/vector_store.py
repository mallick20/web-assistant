from llama_index import VectorStoreIndex,SimpleDirectoryReader

if __name__ == '__main__':

    documents=SimpleDirectoryReader("data").load_data()