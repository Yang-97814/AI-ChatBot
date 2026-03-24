"""
AI ChatBot - 智谱 AI GLM-4 智能对话助手
基于 Streamlit 和智谱 AI 大模型构建
"""

import streamlit as st
import requests
from dotenv import load_dotenv
import os
import uuid


load_dotenv()


class ChatBot:
    """智谱 AI 智能对话助手"""

    def __init__(self):
        self.api_key = None
        self.model = "glm-4-flash"  # 免费模型，有一定额度
        self.api_url = "https://open.bigmodel.cn/api/paas/v4/chat/completions"

    def init_client(self, api_key: str):
        """初始化客户端"""
        self.api_key = api_key

    def generate_response(self, messages: list) -> str:
        """生成回复"""
        if not self.api_key:
            return "请先输入 API Key"

        try:
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }

            data = {
                "model": self.model,
                "messages": messages
            }

            response = requests.post(
                self.api_url,
                headers=headers,
                json=data,
                timeout=60
            )

            if response.status_code == 200:
                result = response.json()
                return result["choices"][0]["message"]["content"]
            else:
                error_msg = response.json().get("error", {}).get("message", "未知错误")
                return f"API 错误: {error_msg}"

        except requests.exceptions.Timeout:
            return "请求超时，请重试"
        except Exception as e:
            return f"发生错误: {str(e)}"


def initialize_session_state():
    """初始化会话状态"""
    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "api_key_configured" not in st.session_state:
        st.session_state.api_key_configured = False

    if "chatbot" not in st.session_state:
        st.session_state.chatbot = ChatBot()

    if "session_id" not in st.session_state:
        st.session_state.session_id = str(uuid.uuid4())


def render_sidebar():
    """渲染侧边栏"""
    with st.sidebar:
        st.title("⚙️ 设置")

        api_key = st.text_input(
            "API Key",
            type="password",
            value="",
            help="输入你的智谱 AI API Key"
        )

        if api_key:
            st.session_state.chatbot.init_client(api_key)
            st.session_state.api_key_configured = True
            st.success("✅ API Key 已配置")

        st.divider()

        st.subheader("💡 使用提示")
        st.markdown("""
        1. 首先获取智谱 AI API Key
        2. 输入 API Key 并确认
        3. 在下方输入问题开始对话
        """)

        st.divider()

        st.subheader("📝 如何获取 API Key")
        st.markdown("""
        1. 访问 [智谱 AI 开放平台](https://open.bigmodel.cn/)
        2. 注册并登录账号
        3. 进入控制台 -> API Key 管理
        4. 创建新 Key 并复制
        """)
        st.caption("新用户有免费额度赠送")

        st.divider()

        if st.button("🗑️ 清除对话", use_container_width=True):
            st.session_state.messages = []
            st.rerun()

        st.divider()

        st.caption("Powered by 智谱 AI GLM-4")


def render_chat_history():
    """渲染聊天历史"""
    for message in st.session_state.messages:
        role = message["role"]
        content = message["content"]

        with st.chat_message(role):
            st.markdown(content)


def handle_user_input():
    """处理用户输入"""
    if prompt := st.chat_input("输入你的问题..."):
        user_message = {"role": "user", "content": prompt}
        st.session_state.messages.append(user_message)

        with st.chat_message("user"):
            st.markdown(prompt)

        if not st.session_state.api_key_configured:
            with st.chat_message("assistant"):
                st.error("请先在侧边栏输入 API Key")
            return

        with st.chat_message("assistant"):
            with st.spinner("思考中..."):
                response = st.session_state.chatbot.generate_response(
                    st.session_state.messages[:-1] + [{"role": "user", "content": prompt}]
                )

            st.markdown(response)

        assistant_message = {"role": "assistant", "content": response}
        st.session_state.messages.append(assistant_message)


def main():
    """主函数"""
    st.set_page_config(
        page_title="智谱 AI 助手",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    st.title("🤖 智谱 AI 助手")
    st.markdown("基于 GLM-4 的智能对话机器人，支持中文问答")

    initialize_session_state()
    render_sidebar()
    render_chat_history()
    handle_user_input()


if __name__ == "__main__":
    main()
