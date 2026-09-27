css = """
<style>

/* =========================================================
   GLOBAL
========================================================= */

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


/* =========================================================
   DOCUMIND LOGO
========================================================= */

.logo-box {

    width: 42px;
    height: 42px;

    border-radius: 12px;

    background: linear-gradient(
        135deg,
        #6366f1,
        #8b5cf6
    );

    color: white;

    display: flex;
    align-items: center;
    justify-content: center;

    font-size: 21px;
    font-weight: 700;

    box-shadow:
        0 5px 20px
        rgba(99, 102, 241, 0.25);
}


/* =========================================================
   TITLE
========================================================= */

.app-title {

    color: #f8fafc;

    font-size: 24px;

    font-weight: 700;

    line-height: 1.1;
}

.app-subtitle {

    color: #8b93a7;

    font-size: 13px;

    margin-top: 4px;
}


/* =========================================================
   WELCOME
========================================================= */

.welcome-box {

    text-align: center;

    padding-top: 100px;

    padding-bottom: 50px;
}

.welcome-icon {

    font-size: 42px;

    width: 70px;
    height: 70px;

    margin: auto;

    display: flex;
    align-items: center;
    justify-content: center;

    border-radius: 18px;

    background: #1b1f27;

    border: 1px solid #303642;
}

.welcome-box h2 {

    color: #f8fafc;

    font-size: 27px;

    margin-top: 20px;

    margin-bottom: 8px;
}

.welcome-box p {

    color: #8b93a7;

    font-size: 14px;
}


/* =========================================================
   CHAT
========================================================= */

[data-testid="stChatMessage"] {

    border-radius: 12px;

    padding-top: 10px;
    padding-bottom: 10px;
}


/* Assistant background */

[data-testid="stChatMessage"]:has(
    [data-testid="chatAvatarIcon-assistant"]
) {

    background: #171a21;
}


/* Message content */

[data-testid="stChatMessageContent"] {

    color: #e5e7eb;

    font-size: 15px;

    line-height: 1.65;
}


/* Links */

[data-testid="stChatMessageContent"] a {

    color: #8b9cff;
}


/* Code */

[data-testid="stChatMessageContent"] code {

    background: #252936;

    padding: 2px 6px;

    border-radius: 5px;
}


/* =========================================================
   CHAT INPUT
========================================================= */

[data-testid="stChatInput"] textarea {

    background: #1b1f27 !important;

    color: #f8fafc !important;

    border: 1px solid #303642 !important;

    border-radius: 14px !important;
}

[data-testid="stChatInput"] textarea:focus {

    border-color: #6366f1 !important;

    box-shadow:
        0 0 0 1px #6366f1 !important;
}


/* =========================================================
   SIDEBAR
========================================================= */

[data-testid="stSidebar"] {

    background: #11141a;
}


/* =========================================================
   BUTTONS
========================================================= */

.stButton > button {

    border-radius: 10px;

    background: #1b1f27;

    color: #f8fafc;

    border: 1px solid #303642;
}

.stButton > button:hover {

    border-color: #6366f1;

    color: white;
}


/* =========================================================
   SCROLLBAR
========================================================= */

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


/* =========================================================
   MOBILE
========================================================= */

@media (max-width: 700px) {

    .app-title {
        font-size: 20px;
    }

    .welcome-box {
        padding-top: 60px;
    }

    .welcome-box h2 {
        font-size: 23px;
    }

    [data-testid="stChatMessageContent"] {
        font-size: 14px;
    }

}

</style>
"""
