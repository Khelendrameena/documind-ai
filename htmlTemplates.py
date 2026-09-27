css = """
<style>

.stApp {
    background: #0f1117;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    background: transparent !important;
}

/* DOCUMIND HEADER */

.documind-header {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 14px 0 20px 0;
    border-bottom: 1px solid #262a33;
    margin-bottom: 20px;
}

.documind-logo {
    width: 42px;
    height: 42px;
    border-radius: 12px;
    background: linear-gradient(135deg, #6366f1, #8b5cf6);
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-size: 22px;
    font-weight: 700;
}

.documind-title {
    font-size: 22px;
    font-weight: 700;
    color: #f8fafc;
}

.documind-subtitle {
    font-size: 12px;
    color: #8b93a7;
    margin-top: 3px;
}

/* CHAT */

.chat-message {
    display: flex;
    width: 100%;
    padding: 18px 0;
    margin-bottom: 4px;
    gap: 14px;
}

.chat-message.user {
    background: transparent;
}

.chat-message.bot {
    background: #171a21;
    border-radius: 12px;
    padding: 18px 14px;
}

/* AVATAR */

.chat-message .avatar {
    width: 36px;
    min-width: 36px;
    height: 36px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.bot-avatar {
    width: 34px;
    height: 34px;
    border-radius: 9px;
    background: linear-gradient(135deg, #6366f1, #8b5cf6);
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 17px;
    font-weight: 700;
}

.user-avatar {
    width: 34px;
    height: 34px;
    border-radius: 9px;
    background: #303642;
    color: #e5e7eb;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 15px;
    font-weight: 600;
}

/* MESSAGE */

.chat-message .message {
    flex: 1;
    color: #e5e7eb;
    font-size: 15px;
    line-height: 1.65;
    padding: 5px 8px 0 2px;
    overflow-wrap: anywhere;
}

.chat-message .message p {
    margin-top: 0;
    margin-bottom: 10px;
}

.chat-message .message strong {
    color: #ffffff;
}

.chat-message .message code {
    background: #252936;
    padding: 2px 6px;
    border-radius: 5px;
}

/* WELCOME */

.welcome {
    text-align: center;
    padding: 70px 20px 30px 20px;
}

.welcome-icon {
    width: 60px;
    height: 60px;
    margin: auto;
    border-radius: 16px;
    background: linear-gradient(135deg, #6366f1, #8b5cf6);
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-size: 28px;
    font-weight: 700;
}

.welcome h1 {
    color: #f8fafc;
    font-size: 30px;
    margin-top: 18px;
    margin-bottom: 8px;
}

.welcome p {
    color: #8b93a7;
    font-size: 14px;
}

/* INPUT */

.stChatInput textarea {
    background: #1b1f27 !important;
    color: #f8fafc !important;
    border: 1px solid #303642 !important;
    border-radius: 14px !important;
}

.stChatInput textarea:focus {
    border-color: #6366f1 !important;
    box-shadow: 0 0 0 1px #6366f1 !important;
}

/* SCROLLBAR */

::-webkit-scrollbar {
    width: 7px;
}

::-webkit-scrollbar-track {
    background: #0f1117;
}

::-webkit-scrollbar-thumb {
    background: #303642;
    border-radius: 10px;
}

/* MOBILE */

@media (max-width: 700px) {

    .documind-title {
        font-size: 20px;
    }

    .chat-message {
        padding: 14px 0;
    }

    .chat-message.bot {
        padding: 15px 10px;
    }

    .chat-message .message {
        font-size: 14px;
    }

}

</style>
"""


bot_template = """
<div class="chat-message bot">
    <div class="avatar">
        <div class="bot-avatar">D</div>
    </div>

    <div class="message">
        {{MSG}}
    </div>
</div>
"""


user_template = """
<div class="chat-message user">
    <div class="avatar">
        <div class="user-avatar">U</div>
    </div>

    <div class="message">
        {{MSG}}
    </div>
</div>
"""
