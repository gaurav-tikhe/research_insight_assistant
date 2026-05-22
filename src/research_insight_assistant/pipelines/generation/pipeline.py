from kedro.pipeline import Pipeline, node
from .nodes import generate_answer

def create_pipeline(**kwargs):
    return Pipeline(
        [
        node(
            func=generate_answer,
            inputs=["params:query", "retrieved_chunks"],
            outputs="final_answer",
            name="generate_answer_node"
            )
        ]
    )