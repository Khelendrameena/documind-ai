css = """
<style>

/* =========================================================
   GLOBAL
========================================================= */

.stApp {
    background-color: #0f1117;
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
   DOCUMIND HEADER
========================================================= */

.documind-header {
    display: flex;
    align-items: center;
    gap: 12px;

    padding: 12px 0 18px 0;

    border-bottom: 1px solid #272b35;

    margin-bottom: 20px;
}

.documind-logo {
    width: 42px;
    height: 42px;

    border-radius: 12px;

    background: linear-gradient(
        135deg,
        #6366f1,
        #8b5cf6
    );

    display: flex;
    align-items: center;
    justify-content: center;

    color: white;

    font-size: 22px;
    font-weight: 700;

    box-shadow:
        0 4px 20px
        rgba(99, 102, 241, 0.25);
}

.documind-title {
    color: #f8fafc;

    font-size: 22px;
    font-weight: 700;

    line-height: 1.1;
}

.documind-subtitle {
    color: #8b93a7;

    font-size: 12px;

    margin-top: 4px;
}


/* =========================================================
   WELCOME SCREEN
========================================================= */

.welcome {
    text-align: center;

    padding-top: 90px;
    padding-bottom: 40px;
}

.welcome-icon {
    width: 64px;
    height: 64px;

    margin: auto;

    border-radius: 17px;

    background: linear-gradient(
        135deg,
        #6366f1,
        #8b5cf6
    );

    display: flex;
    align-items: center;
    justify-content: center;

    color: white;

    font-size: 30px;
    font-weight: 700;

    box-shadow:
        0 8px 30px
        rgba(99, 102, 241, 0.25);
}

.welcome h1 {
    color: #f8fafc;

    font-size: 28px;

    margin-top: 20px;
    margin-bottom: 8px;
}

.welcome p {
    color: #8b93a7;

    font-size: 14px;
}


/* =========================================================
   CHAT
========================================================= */

[data-testid="stChatMessage"] {

    border-radius: 12px;

    padding-top: 12px;
    padding-bottom: 12px;
}


/* Assistant message */

[data-testid="stChatMessage"]:has(
    [data-testid="chatAvatarIcon-assistant"]
) {

    background-color: #171a21;
}


/* Message text */

[data-testid="stChatMessageContent"] {

    color: #e5e7eb;

    font-size: 15px;

    line-height: 1.65;
}


/* Bold text */

[data-testid="stChatMessageContent"] strong {

    color: #ffffff;
}


/* Code */

[data-testid="stChatMessageContent"] code {

    background-color: #252936;

    border-radius: 5px;

    padding: 2px 6px;
}


/* =========================================================
   CHAT INPUT
========================================================= */

[data-testid="stChatInput"] {

    background-color: transparent;
}

[data-testid="stChatInput"] textarea {

    background-color: #1b1f27 !important;

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

    background-color: #11141a;
}

[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {

    color: #f8fafc;
}


/* =========================================================
   BUTTON
========================================================= */

.stButton > button {

    border-radius: 10px;

    border: 1px solid #303642;

    background-color: #1b1f27;

    color: #f8fafc;
}

.stButton > button:hover {

    border-color: #6366f1;

    color: white;
}


/* =========================================================
   FILE UPLOADER
========================================================= */

[data-testid="stFileUploader"] {

    border-radius: 10px;
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

::-webkit-scrollbar-thumb:hover {

    background: #454c5c;
}


/* =========================================================
   MOBILE
========================================================= */

@media (max-width: 700px) {

    .documind-title {
        font-size: 20px;
    }

    .welcome {
        padding-top: 50px;
    }

    .welcome h1 {
        font-size: 23px;
    }

    [data-testid="stChatMessageContent"] {
        font-size: 14px;
    }

}

</style>
"""
