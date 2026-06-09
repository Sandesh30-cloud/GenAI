
import streamlit as st
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

# Load environment variables
load_dotenv()

# ===================== CONFIG =====================
st.set_page_config(page_title="AI Chatbot", page_icon="🎃", layout="centered")

st.title("👽 AI Assistant")
st.caption("Powered by LangChain • Multi-Model Support")

# Sidebar for configuration
with st.sidebar:
    st.header("⚙️ Configuration")
    
    model_options = {
        "Mistral Code Latest": "mistralai:mistral-code-latest",
        "Gemini 2.5 Flash Lite": "google_genai:gemini-2.5-flash-lite",
        "Qwen3 32B": "groq:qwen/qwen3-32b",
        "Llama 3.3 70B": "groq:llama-3.3-70b-versatile",
        "GPT-4o Mini": "openai:gpt-4o-mini",
    }
    
    selected_model_name = st.selectbox(
        "Choose Model",
        options=list(model_options.keys()),
        index=0
    )
    
    MODEL = model_options[selected_model_name]
    
    system_prompt = st.text_area(
        "System Prompt",
        value="You are a helpful professional assistant.",
        height=150
    )
    
    if st.button("🔄 Reset Conversation", type="secondary"):
        st.session_state.messages = []
        st.session_state.langchain_messages = [SystemMessage(content=system_prompt)]
        st.rerun()

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []  # For Streamlit UI display

if "langchain_messages" not in st.session_state:
    st.session_state.langchain_messages = [SystemMessage(content=system_prompt)]

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Type your message here..."):
    # Add user message to UI
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Add to LangChain history
    st.session_state.langchain_messages.append(HumanMessage(content=prompt))
    
    # Show assistant thinking
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                llm = init_chat_model(MODEL)
                response = llm.invoke(st.session_state.langchain_messages)
                ai_response = response.content
                
                # Add to LangChain history
                st.session_state.langchain_messages.append(AIMessage(content=ai_response))
                
                # Add to UI history
                st.session_state.messages.append({"role": "assistant", "content": ai_response})
                
                st.markdown(ai_response)
                
            except Exception as e:
                error_msg = f"❌ Error: {str(e)}"
                st.error(error_msg)
                st.session_state.messages.append({"role": "assistant", "content": error_msg})

# Optional: Show raw LangChain messages (for debugging)
with st.expander("🔍 Debug: LangChain Messages"):
    for msg in st.session_state.langchain_messages:
        st.write(f"**{type(msg).__name__}**: {msg.content[:200]}...")