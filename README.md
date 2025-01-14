# Build your own AI Agent with Backblaze B2 + LangChain

The [notebook in this repository](agent_demo.ipynb) shows you how to build an AI Agent that accepts natural language questions concerning the Backblaze [Drive Stats](https://www.backblaze.com/drivestats) data set, generates SQL queries, and responds with natural language answers.

## Configuration

To use the OpenAI API, you must [sign up for an OpenAI account](https://platform.openai.com/signup) and [create an OpenAI API key](https://platform.openai.com/api-keys).

Copy `.env.template` to `.env`, then edit it to include your Open AI API key:

``` dotenv
OPENAI_API_KEY=<your-open-ai-api-key>
```
