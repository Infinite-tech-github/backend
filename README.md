# Infinite.Tech Backend

Welcome to the **Infinite.Tech Backend**, a robust API platform enabling the generation of dynamic, multimodal AI-driven applications. This backend integrates multiple AI tools to create intelligent, interactive experiences and supports advanced content generation across diverse data modalities.

## Key Features

- **Multimodal AI Integration**: Seamlessly connect with leading AI providers like Ollama, OpenAI, Anyscale, and Mistral to unlock diverse AI capabilities.
- **Dynamic Content Creation**: Generate text, images, tables, maps, and other content using customized prompts and modes.
- **Customizable Modes**: Add new modes and tailor prompt handling with minimal setup.
- **Scalable Architecture**: Built on FastAPI for high performance and support for asynchronous operations.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- FastAPI
- Uvicorn (ASGI server)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/infinite-tech-backend.git
   cd infinite-tech-backend
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Server

#### Mac/Linux Users:
Run the provided `start.sh` script:

```bash
sh start.sh
```

#### Windows Users:
Execute the `start.bat` script by double-clicking it or running in the terminal:

```bash
start.bat
```

#### General Command:
Alternatively, you can run the server manually:

```bash
uvicorn app:app --reload
```

The backend will be available at `http://localhost:8000/`. Use the `--reload` flag during development for auto-reloading upon changes.

## API Endpoints

### Health Check
- **`GET /`**: Confirms the server is running.

### List Available Modes
- **`GET /modes`**: Retrieves all available modes from the configuration directory.

### Generate Content Section
- **`POST /generate_section`**: Generates content based on the input prompt, selected mode, and AI model.

#### Example Request:
```bash
curl -X POST "http://localhost:8000/generate_section" \
-H "accept: application/json" \
-H "Content-Type: application/json" \
-d '{
  "prompt": "Describe the benefits of regular exercise.",
  "model": "llama3.1:latest",
  "mode": "general_generation"
}'
```

### Adding New Modes
To create a new mode, add a markdown file in the `modes/instructions` directory. Use the following structure:

```markdown
# Mode Name

## Overview
Detailed description of the mode.

## Example
Usage examples for the mode.

## Response
Sample response format.
```

## Development

Contributions are welcome! Follow these steps to contribute:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-branch
   ```
3. Implement your changes and commit:
   ```bash
   git commit -am 'Add some feature'
   ```
4. Push the branch:
   ```bash
   git push origin feature-branch
   ```
5. Open a Pull Request for review.

## License

- **Backend**: AGPL-3.0
- **Frontend**: Proprietary

Please adhere to licensing terms for usage and distribution.

## Support

For questions, issues, or feature requests, please open an issue on this repository.

## About

Infinite.Tech is committed to democratizing AI technology by creating accessible, powerful tools that enable innovation across industries. This backend is a cornerstone of that mission, supporting seamless integration and content generation for developers, businesses, and creative professionals alike.
