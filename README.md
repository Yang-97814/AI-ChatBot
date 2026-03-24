# AI ChatBot - 智谱 AI GLM-4 智能对话助手

一个基于 Streamlit 和智谱 AI GLM-4 的现代化智能对话应用，支持多轮对话、Markdown 渲染、中文优化等功能。

## 功能特性

- 🤖 基于智谱 AI GLM-4 的智能对话
- 💬 支持多轮上下文对话
- 📝 Markdown 渲染，代码高亮显示
- 🌙 暗色主题，护眼舒适
- 💾 对话历史记录
- 🗑️ 清除对话历史
- 🇨🇳 专为中文优化

## 技术栈

- **Python 3.10+**
- **Streamlit** - Web 界面框架
- **requests** - HTTP 请求库
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

### 3. 获取 API Key

1. 访问 [智谱 AI 开放平台](https://open.bigmodel.cn/)
2. 注册并登录账号
3. 进入控制台 -> API Key 管理
4. 创建新 Key 并复制

> 💡 新用户有免费额度赠送

### 4. 运行应用

```bash
streamlit run app.py
```

应用将在浏览器中打开，默认地址：`http://localhost:8501`

### 5. 输入 API Key

在侧边栏输入你的智谱 AI API Key，点击确认后即可开始对话。

## 使用说明

1. 在侧边栏输入智谱 AI API Key
2. 在输入框中输入你的问题
3. 按 Enter 或点击发送按钮
4. 等待 GLM-4 生成回复
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

## 注意事项

- 请保管好你的 API Key，不要泄露给他人
- 新用户有免费额度，用完后需充值
- API 调用会产生费用，注意控制使用量
- 建议设置 API 使用限额提醒

## 许可证

MIT License

## 贡献

欢迎提交 Issue 和 Pull Request！
