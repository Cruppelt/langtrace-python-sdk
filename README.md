# [Langtrace](https://www.langtrace.ai)

## Open Source & Open Telemetry(OTEL) Observability for LLM applications

![Static Badge](https://img.shields.io/badge/License-AGPL--3.0-blue) ![Static Badge](https://img.shields.io/badge/npm_@langtrase/typescript--sdk-1.2.9-green) ![Static Badge](https://img.shields.io/badge/pip_langtrace--python--sdk-1.2.8-green) ![Static Badge](https://img.shields.io/badge/Development_status-Active-green)

---

Langtrace is an open source observability software which lets you capture, debug and analyze traces and metrics from all your applications that leverages LLM APIs, Vector Databases and LLM based Frameworks.

## Open Telemetry Support

The traces generated by Langtrace adhere to [Open Telemetry Standards(OTEL)](https://opentelemetry.io/docs/concepts/signals/traces/). We are developing [semantic conventions](https://opentelemetry.io/docs/concepts/semantic-conventions/) for the traces generated by this project. You can checkout the current definitions in [this repository](https://github.com/Scale3-Labs/langtrace-trace-attributes/tree/main/schemas). Note: This is an ongoing development and we encourage you to get involved and welcome your feedback.

---

## Langtrace Cloud ☁️

To use the managed SaaS version of Langtrace, follow the steps below:

1. Sign up by going to [this link](https://langtrace.ai).
2. Create a new Project after signing up. Projects are containers for storing traces and metrics generated by your application. If you have only one application, creating 1 project will do.
3. Generate an API key by going inside the project.
4. In your application, install the Langtrace SDK and initialize it with the API key you generated in the step 3.
5. The code for installing and setting up the SDK is shown below

## Getting Started

Get started by adding simply three lines to your code!

``` python
pip install langtrace-python-sdk
```

``` python
from langtrace_python_sdk import langtrace # Must precede any llm module imports
langtrace.init(api_key=<your_api_key>)
```

OR

``` python
from langtrace_python_sdk import langtrace # Must precede any llm module imports
langtrace.init() # LANGTRACE_API_KEY as an ENVIRONMENT variable
```

## Langtrace Self Hosted

Get started by adding simply two lines to your code and see traces being logged to the console!

``` python
pip install langtrace-python-sdk
```

``` python
from langtrace_python_sdk import langtrace # Must precede any llm module imports
langtrace.init(write_to_langtrace_cloud=False, batch=False)
```

## Langtrace self hosted custom exporter

Get started by adding simply three lines to your code and see traces being exported to your remote location!

``` python
pip install langtrace-python-sdk
```

``` python
from langtrace_python_sdk import langtrace # Must precede any llm module imports
langtrace.init(custom_remote_exporter=<your_exporter>, batch=<True or False>)
```

### Additional Customization

- `@with_langtrace_root_span` - this decorator is designed to organize and relate different spans, in a hierarchical manner. When you're performing multiple operations that you want to monitor together as a unit, this function helps by establishing a "parent" (`LangtraceRootSpan` or whatever is passed to `name`) span. Then, any calls to the LLM APIs made within the given function (fn) will be considered "children" of this parent span. This setup is especially useful for tracking the performance or behavior of a group of operations collectively, rather than individually.

```python
from langtrace_python_sdk.utils.with_root_span import with_langtrace_root_span

@with_langtrace_root_span()
def example():
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": "Say this is a test three times"}],
        stream=False,
    )
    return response
```


- `with_additional_attributes` - this function is designed to enhance the traces by adding custom attributes to the current context. These custom attributes provide extra details about the operations being performed, making it easier to analyze and understand their behavior.

```python
from langtrace_python_sdk.utils.with_root_span import (
    with_langtrace_root_span,
    with_additional_attributes,
)

@with_additional_attributes({"user.id": "1234", "user.feedback.rating": 1})
def api_call1():
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": "Say this is a test three times"}],
        stream=False,
    )
    return response


@with_additional_attributes({"user.id": "5678", "user.feedback.rating": -1})
def api_call2():
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": "Say this is a test three times"}],
        stream=False,
    )
    return response


@with_langtrace_root_span()
def chat_completion():
   api_call1()
   api_call2()
```

## Supported integrations

Langtrace automatically captures traces from the following vendors:

| Vendor | Type | Typescript SDK | Python SDK
| ------ | ------ | ------ | ------ |
| OpenAI | LLM | :white_check_mark: | :white_check_mark: |
| Anthropic | LLM | :white_check_mark: | :white_check_mark: |
| Azure OpenAI | LLM | :white_check_mark: | :white_check_mark: |
| Langchain | Framework | :x: | :white_check_mark: |
| LlamaIndex | Framework | :white_check_mark: | :white_check_mark: |
| Pinecone | Vector Database | :white_check_mark: | :white_check_mark: |
| ChromaDB | Vector Database | :white_check_mark: | :white_check_mark: |

---

## Feature Requests and Issues

- To request for features, head over [here to start a discussion](https://github.com/Scale3-Labs/langtrace/discussions/categories/feature-requests).
- To raise an issue, head over [here and create an issue](https://github.com/Scale3-Labs/langtrace/issues).

---

## Contributions

We welcome contributions to this project. To get started, fork this repository and start developing. To get involved, join our [Discord](https://discord.langtrace.ai) workspace.

---

## Security

To report security vulnerabilites, email us at <security@scale3labs.com>. You can read more on security [here](https://github.com/Scale3-Labs/langtrace/blob/development/SECURITY.md).

---

## License

- Langtrace application(this repository) is [licensed](https://github.com/Scale3-Labs/langtrace/blob/development/LICENSE) under the AGPL 3.0 License. You can read about this license [here](https://www.gnu.org/licenses/agpl-3.0.en.html).
- Langtrace SDKs are licensed under the Apache 2.0 License. You can read about this license [here](https://www.apache.org/licenses/LICENSE-2.0).
