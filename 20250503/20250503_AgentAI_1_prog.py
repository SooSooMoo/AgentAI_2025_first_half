# 必要なライブラリのインストール
#!pip install --quiet langchain openai
#!pip install langchain_community

# OpenAI APIキーの設定
import os
from google.colab import userdata

#google.colabを利用しない場合
os.environ["OPENAI_API_KEY"] = "あなたのAPIキーをここに"
#google.colab利用の場合
#os.environ["OPENAI_API_KEY"] = userdata.get("OPENAI_API_KEY")

# LangChain基本セットアップ
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate
from langchain.chains import LLMChain

# モデルの準備（GPT-4またはGPT-3.5-turbo）
llm = ChatOpenAI(
    model="gpt-3.5-turbo",  # または "gpt-3.5-turbo"
    #model="gpt-4",  # または "gpt-3.5-turbo"
    temperature=0.7,
    max_tokens=1500,
)

# システムプロンプト（エージェントに与える性格・役割）
system_message = SystemMessage(
    content=(
        "あなたは海外旅行とスポーツ観戦に精通したプロフェッショナルな旅行プランナーです。"
        "ユーザーが希望する『観戦対象』と『旅行先』に合わせて、"
        "1日ごとの詳細な旅行プラン（観戦イベント情報、移動手段、観光地提案などを含む）を作成してください。"
        "計画は現実的かつ実行可能なものにしてください。"
    )
)

# 入力フォーマット
human_template = "〇〇観戦と□□□□への海外旅行プランを作成してください。\n\n【観戦対象】{sport}\n【旅行先】{country}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

# チェーンの作成
chat_prompt = ChatPromptTemplate.from_messages([system_message, human_message_prompt])
chain = LLMChain(llm=llm, prompt=chat_prompt)

# --- ここで実際に動かしてみる ---

# ユーザーインプット
sport = "サッカー"
country = "スペイン"

# エージェントに依頼
response = chain.run(sport=sport, country=country)

# 結果表示
print(response)
