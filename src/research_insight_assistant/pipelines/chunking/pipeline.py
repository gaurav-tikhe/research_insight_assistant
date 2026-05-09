from kedro.pipeline import Pipeline, node
from .nodes import chunk_texts

def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=chunk_texts,
                inputs="raw_pdfs",
                outputs="chunks",
                name="chunk_texts_node"
            )

        ]
    )