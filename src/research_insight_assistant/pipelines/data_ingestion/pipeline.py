from kedro.pipeline import Pipeline, node
from .nodes import load_pdfs

def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=load_pdfs,
                inputs="params:pdf_data_path",
                outputs="raw_pdfs",
                name="load_pdfs_node"
            )
        ]
    )