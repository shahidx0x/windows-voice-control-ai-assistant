# Windows Voice Control AI Assistant

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An intelligent voice assistant that controls Windows applications and generates content through speech commands.

## Features

- Voice Control - Control Windows apps using natural speech
- AI Integration - Generate content using voice commands
- Modern UI - Material Design inspired interface
- Command Logging - Track all voice commands and actions
- Extensible - Easy to add new commands and features

## Quick Start

### Prerequisites

- Python 3.9 or higher
- Windows 10/11
- Working microphone

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/windows-voice-ai.git

# Navigate to project directory
cd windows-voice-ai

# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

## Project Structure

```
ai-ass/
├── src/
│   ├── gui/              # GUI components
│   ├── services/         # Core services
│   └── utils/           # Utility functions
├── logs/                # Log files
└── main.py             # Entry point
```

## Usage

1. Select your microphone from the dropdown
2. Click "Give Command" button
3. Speak your command clearly
4. Watch the log area for results

## Voice Commands

| Command | Action |
|---------|--------|
| "open [app]" | Opens specified application |
| "close [app]" | Closes specified application |
| "generate [type]" | Generates content |
| "minimize all" | Minimizes all windows |

## Development

### Setting up dev environment

```bash
# Install dev dependencies
pip install -r requirements.txt

# Run tests
python -m pytest tests/
```

## Future Work & Progress

### GPT Model Integration
- Online GPT Integration
  - OpenAI GPT API integration for advanced language processing
  - Real-time content generation and complex queries
  - Adaptive response handling based on context

- Offline GPT Implementation
  - Local GPT model deployment for offline functionality
  - Optimized smaller models for basic commands
  - Reduced latency and increased privacy
  - No internet dependency for core features

### Planned Improvements
- Hybrid mode switching between online/offline models
- Model compression techniques for better performance
- Custom training for Windows-specific commands
- Automatic model updates and versioning

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

