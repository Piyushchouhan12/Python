import streamlit as st
import pandas as pd
import re
from io import StringIO
from docx import Document
from PyPDF2 import PdfReader

st.set_page_config(page_title="Test Case Generator", page_icon="✅", layout="wide")

st.title("🧪 Test Case Generator from Document")
st.write("Upload a document (TXT, DOCX, or PDF) and automatically generate test cases.")

uploaded_file = st.file_uploader("📂 Upload your file", type=["txt", "docx", "pdf"])

def extract_text(file):
    if file.name.endswith(".txt"):
        return file.read().decode("utf-8")
    elif file.name.endswith(".docx"):
        doc = Document(file)
        return "\n".join([para.text for para in doc.paragraphs])
    elif file.name.endswith(".pdf"):
        reader = PdfReader(file)
        return "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
    return ""

def generate_test_cases(text):
    sentences = re.split(r'[\.\n]', text)
    test_cases = []
    count = 1
    for s in sentences:
        s = s.strip()
        if len(s.split()) > 4:  # meaningful sentence
            test_cases.append({
                "Test Case ID": f"TC_{count:03}",
                "Title": s[:80],
                "Precondition": "System should be up and running.",
                "Steps": f"1. {s}",
                "Expected Result": f"{s} should work as expected."
            })
            count += 1
    return pd.DataFrame(test_cases)

if uploaded_file is not None:
    text = extract_text(uploaded_file)
    st.subheader("📜 Extracted Text Preview")
    st.text_area("Text from document:", text[:1500], height=200)

    if st.button("🚀 Generate Test Cases"):
        if text.strip():
            df = generate_test_cases(text)
            st.success(f"✅ Generated {len(df)} test cases!")
            st.dataframe(df, use_container_width=True)

            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="💾 Download as CSV",
                data=csv,
                file_name="generated_test_cases.csv",
                mime="text/csv"
            )
        else:
            st.warning("⚠️ Could not extract text from the document.")
