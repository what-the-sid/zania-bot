
# Zania Bot 🤖

API for answering questions based on a document using LangChain.

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


## Authors 😎

- [@what-the-sid](https://github.com/what-the-sid)

## Todo 📋
- Add test cases to the APIs
- Add a pre-commit to the build

