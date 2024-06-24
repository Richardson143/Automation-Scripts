from typing import List
from langchain.agents import Tool
from langchain.docstore import InMemoryDocstore
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.tools.base import BaseTool
from langchain.vectorstores import FAISS
from typing import Optional
from richard.tools.selenium import (
    ClickButtonInput,
    DescribeWebsiteInput,
    FillOutFormInput,
    FindFormInput,
    GoogleSearchInput,
    ScrollInput,
    SeleniumWrapper,
)


def get_agent_tools() -> List[BaseTool]:
    """Get the tools that will be used by the AI agent."""
    selenium = SeleniumWrapper()
    
    class GotoTool(BaseTool):
        name = "goto"
        description = "useful for when you need visit a link or a website"
        args_schema = DescribeWebsiteInput

        def _run(self, url: str):
            return selenium.describe_website(url)

    class ClickTool(BaseTool):
        name = "click"
        description = "useful for when you need to click a button/link"
        args_schema = ClickButtonInput

        def _run(self, button_text: str):
            return selenium.click_button_by_text(button_text)

    class FindFormTool(BaseTool):
        name = "find_form"
        description = "useful for when you need to find out input forms given a url. Returns the input fields to fill out"
        args_schema = FindFormInput

        def _run(self, url: Optional[str] = None):
            return selenium.find_form_inputs(url)

    class FillFormTool(BaseTool):
        name = "fill_form"
        description = "useful for when you need to fill out a form on the current website. Input should be a json formatted string"
        args_schema = FillOutFormInput

        def _run(self, form_input: Optional[str] = None):
            return selenium.fill_out_form(form_input)

    class ScrollTool(BaseTool):
        name = "scroll"
        description = "useful for when you need to scroll up or down on the current website"
        args_schema = ScrollInput

        def _run(self, direction: str):
            return selenium.scroll(direction)

    class GoogleSearchTool(BaseTool):
        name = "google_search"
        description = "perform a google search"
        args_schema = GoogleSearchInput

        def _run(self, query: str):
            return selenium.google_search(query)

    tools: List[BaseTool] = [
        GotoTool(),
        ClickTool(),
        FindFormTool(),
        FillFormTool(),
        ScrollTool(),
        GoogleSearchTool(),
    ]

    return tools


def get_vectorstore() -> FAISS:
    # Define your embedding model
    embeddings_model = GoogleGenerativeAIEmbeddings(model="models/embedding-001")  # type: ignore
    # Initialize the vectorstore as empty
    import faiss

    embedding_size = 1536
    index = faiss.IndexFlatL2(embedding_size)
    vectorstore = FAISS(embeddings_model.embed_query, index, InMemoryDocstore({}), {})
    return vectorstore
