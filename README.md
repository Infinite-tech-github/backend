# Infinite.Tech Backend

Welcome to Infinite.Tech, an all-in-one multimodal AI platform designed to harness infinite tools for generating dynamic, intelligent applications. This backend repository powers Infinite.Tech, offering APIs for integration and creative prompt engineering across diverse data forms.

## Features

- **Multimodal AI Integration**: Connect with various AI services including Ollama, OpenAI, Anyscale, and Mistral to leverage cutting-edge AI technologies.
- **Dynamic Content Generation**: Utilize AI-driven engines to generate text, images, tables, maps, and more based on user inputs.
- **Extensive API Coverage**: Integrate with APIs for documents, images, tables, code, maps, graphs & charts, calendars, and more.
- **Scalable and Secure**: Built on FastAPI, known for its high performance, scalability, and support for asynchronous tasks.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- FastAPI
- Uvicorn (as ASGI server)

### Running the Server
**For Mac Users:**

You can easily start the server using the provided `start.sh` script. Simply run it from the terminal:

```bash
sh start_server.sh
```

**For Windows Users:**

You can easily start the server using the provided `start.bat` script. Simply double-click the file or run it from the command prompt:

```bash
start.bat
```

**For Unix-based Systems:**
```bash
uvicorn app:app --reload
```

This script executes the following commands to start the FastAPI server using Uvicorn with auto-reload enabled for development:

```batch
@echo off
python -m uvicorn app:app --reload
pause
```


This will serve the backend at `http://localhost:8000/`. The `--reload` flag allows for automatic reloads during development for immediate updates.

## Usage

Explore the following endpoints:

- `GET /`: Verify server operation.
- `GET /modes`: Retrieve a list of available modes.
- `POST /generate_section`: Submit custom content generation requests.

## Examples

### Get Modes

```bash
curl -X GET "http://localhost:8000/modes" -H  "accept: application/json"
```

### Generate Section
```bash
curl -X POST "http://localhost:8000/generate_section" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"mode\":post,\"prompt\":\"Write a paragraph about the benefits of exercise.\",\"provider\":ollama,\"model\":\"llama3.1:latest\"}"
```

## Adding New Modes

To add a new mode, create a new file in the `modes/instructions` directory with the following structure:

```markdown
# Mode Name

## Overview
Description of the mode and its functionality.

## Example
Provide an example of how to use the mode.

## Response
Provide a sample response format.
```



## Development

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a new Pull Request.

## License

- **Backend**: AGPL-3.0
- **Frontend**: Proprietary

Ensure compliance with licensing terms when using or distributing this software.

## Support

For issues, questions, or requests, please open an issue on this repository.

## About

Infinite.Tech is developed by Infinite Tech with the mission to democratize AI technology and make powerful tools accessible to a broad audience.
