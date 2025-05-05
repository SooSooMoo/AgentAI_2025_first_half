!pip install langchain_community

# APIキー（OpenAIのみ）
import os
from google.colab import userdata

os.environ["OPENAI_API_KEY"] = "あなたのOpenAI APIキー"
#google.colab利用の場合
#os.environ["OPENAI_API_KEY"] = userdata.get("OPENAI_API_KEY")

# モデル読み込み
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from langchain.utilities import DuckDuckGoSearchAPIWrapper

# モデル定義
llm = ChatOpenAI(
    model="gpt-4",  # または "gpt-3.5-turbo"
    temperature=0.7,
    max_tokens=1500,
)

# DuckDuckGo検索ツールの設定
search = DuckDuckGoSearchAPIWrapper()

search_tool = Tool(
    name="Search",
    func=search.run,
    description="サッカーなどの試合スケジュールを調べるためのWeb検索ツールです。"
)

# エージェント初期化
tools = [search_tool]

agent = initialize_agent(
    tools,
    llm,
    agent="chat-zero-shot-react-description",
    verbose=True,
)

# エージェントへの指示
sport = "サッカー"
country = "スペイン"

task_prompt = f"""
あなたはプロの旅行プランナーです。

【タスク】
・{sport}観戦と{country}への海外旅行プランを作成してください。
・DuckDuckGo検索ツールを使って現地の試合スケジュールを調べてください。
・試合日を中心に5日間の旅行プランを立ててください。
・観戦、観光、移動、食事、宿泊など、具体的な日程を含めてください。
"""

# 実行
response = agent.run(task_prompt)

print(response)
