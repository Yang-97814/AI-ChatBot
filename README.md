# AI ChatBot - Claude API 智能对话助手

一个基于 Streamlit 和 Claude API 的现代化智能对话应用，支持多轮对话、代码高亮、Markdown 渲染等功能。

## 功能特性

- 🤖 基于 Claude 3.5 Sonnet 的智能对话
- 💬 支持多轮上下文对话
- 📝 Markdown 渲染，代码高亮显示
- 🌙 暗色主题，护眼舒适
- 💾 对话历史记录
- 📋 一键复制回复内容
- 🗑️ 清除对话历史

## 技术栈

- **Python 3.10+**
- **Streamlit** - Web 界面框架
- **Anthropic SDK** - Claude API 调用
- **python-dotenv** - 环境变量管理

## 快速开始

### 1. 克隆项目

```bash
git clone https://github.com/Yang-97814/AI-ChatBot.git
cd AI-ChatBot
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 配置 API Key

复制 `.env.example` 为 `.env`，并填入你的 API Key：

```bash
cp .env.example .env
```

编辑 `.env` 文件：

```
ANTHROPIC_API_KEY=sk-ant-api03-your_key_here
```

> 💡 获取 API Key：访问 [Anthropic Console](https://console.anthropic.com/)

### 4. 运行应用

```bash
streamlit run app.py
```

应用将在浏览器中打开，默认地址：`http://localhost:8501`

## 使用说明

1. 首次使用需要输入 API Key（会保存在本地会话中）
2. 在输入框中输入你的问题
3. 按 Enter 或点击发送按钮
4. 等待 Claude 生成回复
5. 支持连续对话，上下文会自动传递

## 项目结构

```
AI-ChatBot/
├── app.py              # 主应用代码
├── requirements.txt    # 依赖列表
├── .env.example        # 环境变量示例
├── README.md           # 项目说明
└── .gitignore          # Git 忽略文件
```

## 环境变量

| 变量名 | 必填 | 说明 |
|--------|------|------|
| ANTHROPIC_API_KEY | 是 | Anthropic API 密钥 |

## 注意事项

- 请保管好你的 API Key，不要泄露给他人
- API 调用会产生费用，注意控制使用量
- 建议设置 API 使用限额提醒

## 许可证

MIT License

## 贡献

欢迎提交 Issue 和 Pull Request！
