from kedro.pipeline import Pipeline, node
from .nodes import create_faiss_index


def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=create_faiss_index,
                inputs="chunks",
                outputs="vectorstore",
                name="create_faiss_index_node",
            )
        ]
    )