from kedro.pipeline import Pipeline, node
from .nodes import retrieve_chunks


def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=retrieve_chunks,
                inputs=["params:query", "vectorstore"],
                outputs="retrieved_chunks",
                name="retrieve_chunks_node",
            )
        ]
    )