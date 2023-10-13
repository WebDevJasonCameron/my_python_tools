from keys.keys import provide_key1
from autogen import AssistantAgent, UserProxyAgent, config_list_from_json
import openai

openai.api_key = provide_key1()

config_list = config_list_from_json(env_or_file="OAI_CONFIG_LIST")
assistant = AssistantAgent("assistant", llm_config={"config_list": config_list})
user_proxy = UserProxyAgent("user_proxy", code_execution_config={"work_dir": "coding"})


user_proxy.initiate_chat(assistant, message="build a simple snake game")

