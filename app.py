"""
AI ChatBot - Claude API 智能对话助手
基于 Streamlit 和 Anthropic Claude API 构建
"""

import streamlit as st
import anthropic
from dotenv import load_dotenv
import os
import uuid


load_dotenv()


class ChatBot:
    """Claude 智能对话助手"""

    def __init__(self):
        self.client = None
        self.model = "claude-sonnet-4-20250514"
        self.max_tokens = 4096

    def init_client(self, api_key: str):
        """初始化 Anthropic 客户端"""
        self.client = anthropic.Anthropic(api_key=api_key)

    def generate_response(self, messages: list) -> str:
        """生成回复"""
        if not self.client:
            return "请先输入 API Key"

        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=self.max_tokens,
                messages=messages
            )
            return response.content[0].text
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
            help="输入你的 Anthropic API Key"
        )

        if api_key:
            st.session_state.chatbot.init_client(api_key)
            st.session_state.api_key_configured = True
            st.success("✅ API Key 已配置")

        st.divider()

        st.subheader("💡 使用提示")
        st.markdown("""
        1. 首先输入你的 API Key
        2. 在下方输入问题
        3. 按 Enter 或点击发送
        """)

        st.divider()

        if st.button("🗑️ 清除对话", use_container_width=True):
            st.session_state.messages = []
            st.rerun()

        st.divider()

        st.caption("Powered by Claude 3.5 Sonnet")


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

            col1, col2 = st.columns([1, 5])
            with col1:
                if st.button("📋 复制", key=f"copy_{len(st.session_state.messages)}"):
                    import pyperclip
                    pyperclip.copy(response)
                    st.toast("已复制到剪贴板")

        assistant_message = {"role": "assistant", "content": response}
        st.session_state.messages.append(assistant_message)


def main():
    """主函数"""
    st.set_page_config(
        page_title="Claude AI 助手",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    st.title("🤖 Claude AI 助手")
    st.markdown("基于 Claude 3.5 Sonnet 的智能对话机器人")

    initialize_session_state()
    render_sidebar()
    render_chat_history()
    handle_user_input()


if __name__ == "__main__":
    main()
