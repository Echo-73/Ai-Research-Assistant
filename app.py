import streamlit as st
import os
from dotenv import load_dotenv
from crew import research_crew

load_dotenv()

def check_api_keys():
    required_vars = ["SERPER_API_KEY", "GROQ_API_KEY"]
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    return missing_vars

def main():
    st.set_page_config(
        page_title="AI Research Assistant",
        page_icon="🔍",
        layout="wide"
    )

    st.title("🔍 AI Research Assistant")
    st.markdown("*Powered by CrewAI + Groq*")

    if "research_completed" not in st.session_state:
        st.session_state.research_completed = False

    if "research_result" not in st.session_state:
        st.session_state.research_result = None

    if "research_error" not in st.session_state:
        st.session_state.research_error = None

    with st.sidebar:
        st.header("Configuration")

        missing_vars = check_api_keys()

        if missing_vars:
            st.error("Missing API Keys")
            for var in missing_vars:
                st.code(f"{var}=your_api_key_here")
        else:
            st.success("API Keys Configured")

        st.header("Research Agent")

        st.markdown("""
        **Research Specialist**
        - Searches latest information
        - Collects reliable sources
        - Creates structured research reports
        """)

    col1, col2 = st.columns([2, 1])

    with col1:
        st.header("Research Topic")

        topic = st.text_input(
            "Enter a topic:",
            placeholder="e.g. AI Agents, Computer Vision, Quantum Computing"
        )

        if st.button(
            "Start Research",
            type="primary",
            disabled=bool(missing_vars)
        ):
            if not topic.strip():
                st.error("Please enter a topic.")
            else:
                try:
                    with st.spinner("Researching..."):
                        result = research_crew.kickoff(
                            inputs={"topic": topic}
                        )

                    st.session_state.research_result = result
                    st.session_state.research_completed = True
                    st.session_state.research_error = None

                except Exception as e:
                    st.session_state.research_error = str(e)
                    st.session_state.research_completed = True

    with col2:
        st.header("Status")

        if st.session_state.research_completed:
            if st.session_state.research_error:
                st.error(st.session_state.research_error)
            else:
                st.success("Research Completed")
        else:
            st.info("Waiting for research request")

    if st.session_state.research_result:
        st.divider()
        st.header("Research Results")

        result = st.session_state.research_result

        try:
            st.markdown(str(result))
        except:
            st.write(result)

        st.download_button(
            label="📥 Download Report",
            data=str(result),
            file_name="research_report.md",
            mime="text/markdown"
        )

if __name__ == "__main__":
    main()