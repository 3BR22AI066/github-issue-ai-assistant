import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8000/analyze-issue"

# ---------- Page Config ----------
st.set_page_config(
    page_title="AI GitHub Issue Assistant",
    page_icon="🤖",
    layout="centered"
)

# ---------- Custom CSS ----------
st.markdown(
    """
    <style>
        .title-text {
            font-size: 36px;
            font-weight: 700;
            text-align: center;
        }
        .subtitle-text {
            text-align: center;
            font-size: 16px;
            color: #6b7280;
        }
        .card {
            background-color: #0f172a;
            padding: 18px;
            border-radius: 12px;
            margin-bottom: 15px;
            color: white;
        }
        .label-pill {
            display: inline-block;
            background-color: #2563eb;
            color: white;
            padding: 4px 10px;
            border-radius: 20px;
            margin-right: 6px;
            font-size: 13px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------- Header ----------
st.markdown('<div class="title-text">🤖 AI GitHub Issue Assistant</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle-text">Turn GitHub issues into structured insights instantly</div>',
    unsafe_allow_html=True
)

st.divider()

# ---------- Input Section ----------
with st.container():
    st.subheader("🔍 Analyze an Issue")

    repo_url = st.text_input(
        "GitHub Repository URL",
        placeholder="https://github.com/facebook/react"
    )

    issue_number = st.number_input(
        "Issue Number",
        min_value=1,
        step=1
    )

    analyze_btn = st.button("🚀 Analyze Issue", use_container_width=True)

# ---------- API Call ----------
if analyze_btn:
    if not repo_url or not issue_number:
        st.warning("⚠ Please provide both repository URL and issue number.")
    else:
        with st.spinner("Analyzing issue with AI..."):
            try:
                response = requests.post(
                    BACKEND_URL,
                    params={
                        "repo_url": repo_url,
                        "issue_number": int(issue_number)
                    },
                    timeout=30
                )

                if response.status_code == 200:
                    data = response.json()
                    st.success("✅ Analysis Complete")

                    # ---------- Results ----------
                    st.markdown("### 📌 Issue Summary")
                    st.markdown(
                        f"<div class='card'>{data.get('summary', 'N/A')}</div>",
                        unsafe_allow_html=True
                    )

                    col1, col2 = st.columns(2)

                    with col1:
                        st.markdown("### 🗂 Type")
                        st.markdown(
                            f"<div class='card'>{data.get('type', 'N/A')}</div>",
                            unsafe_allow_html=True
                        )

                    with col2:
                        st.markdown("### ⚠ Priority")
                        st.markdown(
                            f"<div class='card'>{data.get('priority_score', 'N/A')}</div>",
                            unsafe_allow_html=True
                        )

                    st.markdown("### 🏷 Suggested Labels")
                    labels = data.get("suggested_labels", [])
                    if labels:
                        label_html = "".join(
                            [f"<span class='label-pill'>{label}</span>" for label in labels]
                        )
                        st.markdown(label_html, unsafe_allow_html=True)
                    else:
                        st.write("No labels suggested")

                    st.markdown("### 📈 Potential Impact")
                    st.markdown(
                        f"<div class='card'>{data.get('potential_impact', 'N/A')}</div>",
                        unsafe_allow_html=True
                    )

                else:
                    st.error(f"Backend Error ({response.status_code})")
                    st.code(response.text)

            except requests.exceptions.RequestException as e:
                st.error("❌ Failed to connect to backend")
                st.code(str(e))

# ---------- Footer ----------
st.divider()
st.caption("Built as part of an AI-Native Product Engineering Case Study 🚀")
