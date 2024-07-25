# ETHCC 7 Workshop

This agent uses the [Hive Agent Kit](htps://github.com/hivenetwork-ai/hive-agent-py) along with various tools to answer questions.

Join our Discord community for support and discussion.

[![](https://dcbadge.limes.pink/api/server/vnJvW4wZp9)](https://discord.gg/vnJvW4wZp9)

## Project Requirements
- Python >= 3.11
- Node >= 20.10.0

## Setup
### Hive Agent Server
- Create a new file called .env
- Copy the contents of [.env.example](.env.example) into your new .env file
- API keys for third party tools are not provided.
  - `OPENAI_API_KEY` from OpenAI
  
  You can use other LLMs, in which case you can add a corresponding API key
  - `ANTHROPIC_API_KEY` from Anthropic
  - `MISTRAL_API_KEY` from Mistral 
  - [Most open source LLMs](https://ollama.com/library)
- Create a virtual Python environment
```
$ python -m venv ./venv
```
- Activate the Python virtual env.
  - Windows:
    - In cmd.exe: `venv\Scripts\activate.bat`
    - In PowerShell: `venv\Scripts\Activate.ps1`
  - Unix: `source venv/bin/activate`
- Install dependencies.
```
$ pip install -r requirements.txt
```

### Hive Agent UI
- Clone the [hive-agent-ui](https://github.com/hivenetwork-ai/hive-agent-ui) (Node.js) repo.
- Follow the [setup instructions](https://github.com/hivenetwork-ai/hive-agent-ui?tab=readme-ov-file#hive-agent-ui).

## Usage
- Run it
```
(venv) $ python main.py
```
- Test your agent by calling it Chat API endpoint, `/api/chat`, to see the result:

```
curl --location 'localhost:8000/api/v1/chat' \
--header 'Content-Type: application/json' \
--data '{
    "user_id": "user123",
    "session_id": "session123",
    "chat_data": {
        "messages": [
            { "role": "user", "content": "What's going on in Canada right now?" }
        ]
    }
}'
```

## Learn More
Powered by [HiveNetwork.ai](https://hivenetwork.ai).
