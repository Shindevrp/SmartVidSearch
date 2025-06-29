import pinecone
from credentials.api_keys import (
    PINECONE_API_KEY, PINECONE_INDEX_NAME, PINECONE_DIMENSIONS, PINECONE_HOST,
    PINECONE_REGION, PINECONE_METRIC, PINECONE_TYPE, PINECONE_CAPACITY_MODE
)

pinecone.init(
    api_key=PINECONE_API_KEY,
    environment=PINECONE_REGION,  # Pinecone uses region as environment
    host=PINECONE_HOST
)

def get_or_create_index():
    if PINECONE_INDEX_NAME not in pinecone.list_indexes():
        pinecone.create_index(
            name=PINECONE_INDEX_NAME,
            dimension=PINECONE_DIMENSIONS,
            metric=PINECONE_METRIC,
            pod_type=PINECONE_TYPE,
            capacity_mode=PINECONE_CAPACITY_MODE
        )
    return pinecone.Index(PINECONE_INDEX_NAME)

def upsert_embeddings(embeddings, ids):
    index = get_or_create_index()
    index.upsert(vectors=list(zip(ids, embeddings)))

def query_embedding(embedding, top_k=5):
    index = get_or_create_index()
    return index.query(embedding, top_k=top_k)
