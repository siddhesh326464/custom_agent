import os,uuid
from datetime import datetime
from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct


class LongTermMemory:
    COLLECTION_NAME = "long_term_memory"
    VECTOR_DIM = 384

    def __init__(self,url:str, api_key:str):
        self.client = QdrantClient(
            url=url,
            api_key=api_key
        )
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        existing_clusters = [c.name for c in self.client.get_collections().collections]
        if self.COLLECTION_NAME not in existing_clusters:
            self.client.create_collection(
                collection_name=self.COLLECTION_NAME,
                vectors_config=VectorParams(
                    size = self.VECTOR_DIM,
                    distance = Distance.COSINE
                )
            )

    def add_long_term_memory(self,key:str,value:str):
        text_to_embade = f"{key} : {value}"
        vector = self.model.encode(text_to_embade).tolist()
        point_id = str(uuid.uuid5(uuid.NAMESPACE_DNS,key))
        self.client.upsert(
            collection_name=self.COLLECTION_NAME,
            points=[
                PointStruct(
                    id=point_id,
                    vector = vector,
                    payload={
                        "key" : key,
                        "value" : value,
                        "updated_at":datetime.now().isoformat()
                    }
                )
            ]
        )

    def get_relevant_memories(self,query:str,top_k:int=5):
        """Semantic search — finds facts relevant to the query."""
        try:
            query_encoder = self.model.encode(query).tolist()
            results = self.client.query_points(

                collection_name=self.COLLECTION_NAME,
                query=query_encoder,
                limit=top_k,
                with_payload=True,

            ).points
            return [
                {
                    "key": r.payload["key"],
                    "value": r.payload["value"],
                    "score": round(r.score, 4)
                }
                for r in results
            ]
        except Exception as e:
            return []

    def get_all_formatted(self, query: str = None, top_k: int = 5) -> str:
        """Returns facts as a string ready to inject into the LLM prompt."""
        facts = self.get_relevant_memories(query, top_k=top_k) if query else []
        if not facts:
            results, _ = self.client.scroll(
                collection_name=self.COLLECTION_NAME,
                limit=top_k,
                with_payload=True
            )
            facts = [{"key": r.payload["key"], "value": r.payload["value"]} for r in results]
        if not facts:
            return "No long-term facts stored."
        lines = ["--- LONG TERM MEMORY ---"]
        for f in facts:
            lines.append(f"- {f['key']}: {f['value']}")
        return "\n".join(lines)

        
    
