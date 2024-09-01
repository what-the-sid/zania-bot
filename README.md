
# Zania Bot 🤖

API for answering questions based on a document using LangChain.\
_(**Note**: Authentication has not been added to the FastAPI app)_

## Run Locally 🚀

\
**Install Dependencies** 

The `Makefile` here automates various setup and maintenance tasks for the project:

- **local and production**: Installs all required libraries and sets up the `zania` command alias in your shell configuration.
- **create-venv**: Creates a Python virtual environment if it doesn't already exist.
- **install-libs**: Installs all dependencies using Poetry within the virtual environment.
- **clean**: Removes the virtual environment and cleans up the zania alias from your shell configuration.
To use these commands, simply run

```bash
make local #OR make production
```

**Start dev server**

```bash
  zania run-server dev # OR production
```

## Environment Variables 🎲


| ENV Name                | Description                        |
|-------------------------|------------------------------------|
| `OPEN_API_KEY`     | API Key required to interact with Open AI model           |

You can configure the same using:
```bash
  zania config
```
This will ask prompt to add your `OPEN_API_KEY` interactively

## API Reference 📂

**Default langchain playground**: `/chain/playground`

### Zania Document QA Bot

```http
  POST /api/v1/analyze-file
```

| Parameter | Type     | Description                | Syntax |
| :-------- | :------- | :------------------------- | :---------------------------|
| `document` | `file` | **Required**. Document you need to read and analyze| `JSON/PDF` files Supported |
| `questions` | `file` | **Required**. JSON File containing all questions you need to answer| The questions should be a list of `String`|

**Example** `questions.json`:

```json
[
    "What is the name of the company?",
    "Who is the CEO of the company?",
    "What is their vacation policy?",
    "What is the termination policy?"
]

```

**Example** `Response`
```json
{
    "results": [
        {
            "question": "What is the name of the company?",
            "answer": "The name of the company is Zania, Inc."
        },
        {
            "question": "Who is the CEO of the company?",
            "answer": "The CEO of the company is Shruti Gupta."
        },
        {
            "question": "What is their vacation policy?",
            "answer": "Employees must request vacation at least a specified number of days or weeks in advance, and the company generally grants requests considering business needs. Vacation must be taken in increments of at least a specified number of hours or days. Unused vacation may be required to be used during certain leaves of absence, and vacation accrual may stop during unpaid leaves."
        },
        {
            "question": "What is the termination policy?",
            "answer": "The termination policy states that employment is on an \"at-will\" basis, meaning employees can be terminated without prior warning or procedure, depending on circumstances. Management may provide verbal or written warnings before termination, but is not obligated to follow any specific disciplinary procedures. The specific terms of the employment relationship, including termination procedures, are governed by applicable state laws."
        }
    ]
}
```

## Development ✂️

The [settings.py](https://github.com/what-the-sid/zania-bot/blob/main/app/settings.py) file contains configurable parameters that define the core behavior and metadata of the Zania QA Bot API.

For Example, You can fine tune the API by changing the `model` and `system prompt` by modifying the following variables:
 ```python
 CHAIN_MODEL = "gpt-4o-mini" # model name
 QA_TEMPLATE = (
    "You are an assistant for question-answering tasks. "
    "Use the following pieces of retrieved context to answer "
    "Answer the question as precise as possible using the provided context"
    "If you don't know the answer or If the answer is not contained in the context, say Data Not Available. Use three sentences maximum and keep the "
    "answer concise."
    "\n\n"
    "{context}"
    ) # System Prompt used to read and understand the uploaded document
 ```

## Authors 😎

- [@what-the-sid](https://github.com/what-the-sid)


## Todo 📋
- Add test cases to the APIs
- Add a pre-commit to the build

## References

[Langchain PDF ingestion](https://python.langchain.com/v0.2/docs/tutorials/pdf_qa/)\
[Langchain Document Loaders (PDF)](https://python.langchain.com/v0.2/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.pdf.PyPDFParser.html)\
[Langchain Document Loaders (JSON)](https://python.langchain.com/v0.2/api_reference/community/document_loaders/langchain_community.document_loaders.json_loader.JSONLoader.html)
