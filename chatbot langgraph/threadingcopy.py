import streamlit as st
from langgraph_backend import chatbot
from langchain_core.messages import HumanMessage
import uuid


st.sidebar.title("LangGraph Chatbot")
st.sideebar.button("new chat")