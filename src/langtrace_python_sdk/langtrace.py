
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    ConsoleSpanExporter,
    SimpleSpanProcessor,
)

from langtrace_python_sdk.extensions.langtrace_exporter import LangTraceExporter
from langtrace_python_sdk.instrumentation.anthropic.instrumentation import (
    AnthropicInstrumentation,
)
from langtrace_python_sdk.instrumentation.chroma.instrumentation import (
    ChromaInstrumentation,
)
from langtrace_python_sdk.instrumentation.langchain.instrumentation import (
    LangchainInstrumentation,
)
from langtrace_python_sdk.instrumentation.langchain_community.instrumentation import (
    LangchainCommunityInstrumentation,
)
from langtrace_python_sdk.instrumentation.langchain_core.instrumentation import (
    LangchainCoreInstrumentation,
)
from langtrace_python_sdk.instrumentation.llamaindex.instrumentation import (
    LlamaindexInstrumentation,
)
from langtrace_python_sdk.instrumentation.openai.instrumentation import (
    OpenAIInstrumentation,
)
from langtrace_python_sdk.instrumentation.pinecone.instrumentation import (
    PineconeInstrumentation,
)


def init(
    api_key: str = None,
    batch: bool = True,
    write_to_langtrace_cloud: bool = True,
    debug_log_to_console: bool = False,
    custom_remote_exporter=None,
):

    provider = TracerProvider()

    remote_write_exporter = (
        LangTraceExporter(api_key, write_to_langtrace_cloud)
        if custom_remote_exporter is None
        else custom_remote_exporter
    )
    console_exporter = ConsoleSpanExporter()
    batch_processor_remote = BatchSpanProcessor(remote_write_exporter)
    batch_processor_console = BatchSpanProcessor(console_exporter)
    simple_processor_console = SimpleSpanProcessor(console_exporter)

    if debug_log_to_console:
        if batch:
            provider.add_span_processor(batch_processor_console)
        else:
            provider.add_span_processor(simple_processor_console)

    if write_to_langtrace_cloud:
        if batch:
            provider.add_span_processor(batch_processor_remote)
        else:
            raise ValueError("Batching is required for remote write")

    # Initialize tracer
    trace.set_tracer_provider(provider)

    openai_instrumentation = OpenAIInstrumentation()
    pinecone_instrumentation = PineconeInstrumentation()
    llamaindex_instrumentation = LlamaindexInstrumentation()
    chroma_instrumentation = ChromaInstrumentation()
    langchain_instrumentation = LangchainInstrumentation()
    langchain_core_instrumentation = LangchainCoreInstrumentation()
    langchain_community_instrumentation = LangchainCommunityInstrumentation()
    anthropic_instrumentation = AnthropicInstrumentation()

    # Call the instrument method with some arguments
    openai_instrumentation.instrument()
    pinecone_instrumentation.instrument()
    llamaindex_instrumentation.instrument()
    chroma_instrumentation.instrument()
    langchain_instrumentation.instrument()
    langchain_core_instrumentation.instrument()
    langchain_community_instrumentation.instrument()
    anthropic_instrumentation.instrument()
