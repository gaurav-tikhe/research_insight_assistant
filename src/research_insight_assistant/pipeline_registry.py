"""Project pipelines."""
from __future__ import annotations

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline
from research_insight_assistant.pipelines.data_ingestion.pipeline import create_pipeline as ingestion_pipeline
from research_insight_assistant.pipelines.chunking.pipeline import create_pipeline as chunking_pipeline
from research_insight_assistant.pipelines.embedding.pipeline import create_pipeline as embedding_pipeline 
from research_insight_assistant.pipelines.retrieval.pipeline import create_pipeline as retrieval_pipeline
from research_insight_assistant.pipelines.generation.pipeline import create_pipeline as generation_pipeline


def register_pipelines() -> dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    return {
        "__default__": ingestion_pipeline() 
                       + chunking_pipeline() 
                       + embedding_pipeline() 
                       + retrieval_pipeline()
                       + generation_pipeline(),
    }
