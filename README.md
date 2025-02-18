# Build your own AI Agent with Backblaze B2 + LangChain

The notebooks in this repository shows you how to build an AI Agent that accepts natural language questions concerning the Backblaze [Drive Stats](https://www.backblaze.com/drivestats) data set, generates SQL queries, and responds with natural language answers.

There are currently two notebooks:

* [agent_demo.ipynb](agent_demo.ipynb) uses OpenAI GPT-4o mini as the underlying LLM
* [agent_demo_deepseek.ipynb](agent_demo_deepseek.ipynb) explores the use of DeepSeek R1 and DeepSeek V3 as alternatives to OpenAI.

## Configuration

### OpenAI

To use the OpenAI API, you must [sign up for an OpenAI account](https://platform.openai.com/signup) and [create an OpenAI API key](https://platform.openai.com/api-keys).

Copy `.env.template` to `.env`, then edit it to include your Open AI API key:

``` dotenv
OPENAI_API_KEY=<your-openai-api-key>
```

### DeepSeek

To use the DeepSeek API, you must [sign up for a DeepSeek account](https://platform.deepseek.com/sign_up) and [create a DeepSeek API key](https://platform.deepseek.com/api_keys).

Copy `.env.template` to `.env`, then edit it to include your DeepSeek API key:

``` dotenv
DEEPSEEK_API_KEY=<your-deepseek-api-key>
```

# Running the Notebooks

Both notebooks should run on any Jupyter-compatible platform:

* The "classic" Jupyter Notebook interface is lightweight and easy to install and use: https://docs.jupyter.org/en/latest/install/notebook-classic.html
* JupyterLab is more versatile, with more features: https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html
* There are Jupyter plugins for many integrated development environments (IDEs), for example, [IntelliJ](https://plugins.jetbrains.com/plugin/22814-jupyter) and [VS Code](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter).

## JupyterLab Settings

If you are deploying JupyterLab on a virtual machine at a cloud provider, you will need to configure it to accept connections from the internet. Here is the configuration we set in `~/.jupyter/jupyter_server_config.py` for this purpose:

```python
# Allow requests where the Host header doesn't point to a local server
c.ServerApp.allow_remote_access = True

# The IP address the Jupyter server will listen on.
# 0.0.0.0 = all addresses
c.ServerApp.ip = '0.0.0.0'

# Allow access to hidden files
# Set to True to allow access to .venv
c.ContentsManager.allow_hidden = True
```
