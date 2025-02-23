import streamlit as st
import subprocess
import os
import time
from pathlib import Path

def run_crewai():
    process = subprocess.Popen(['crewai', 'run'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    stdout_lines = []
    stderr_lines = []

    while True:
        stdout_line = process.stdout.readline()
        stderr_line = process.stderr.readline()

        if not stdout_line and not stderr_line and process.poll() is not None:
            break

        time.sleep(0.1)

    process.stdout.close()
    process.stderr.close()
    process.wait()

    return ''.join(stdout_lines), ''.join(stderr_lines)

def read_article(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def list_markdown_files():
    output_dir = Path('output')
    return list(output_dir.glob('*.md'))

st.title("SEO Article Auto Writer")

tab1, tab2 = st.tabs(["Generate Article", "View Articles"])

with tab1:
    website_url = st.text_input("Enter the URL of the website:")

    if st.button("Submit"):
        with open('src/seo_art_auto/main.py', 'r') as file:
            main_content = file.readlines()

        for i, line in enumerate(main_content):
            if "'website':" in line:
                main_content[i] = f"        'website': '{website_url}',\n"

        with open('src/seo_art_auto/main.py', 'w') as file:
            file.writelines(main_content)

        with st.spinner("Running CrewAI..."):
            stdout, stderr = run_crewai()

        if stderr:
            st.error("Error running crewai. Check the logs above for details.")
        else:
            st.success("CrewAI run completed successfully!")

        article_content = read_article('output/article.md')
        st.markdown(article_content)

with tab2:
    st.header("Generated Articles")
    
    markdown_files = list_markdown_files()
    
    if not markdown_files:
        st.info("No articles found in the output directory.")
    else:
        with st.container():
            for md_file in markdown_files:
                with st.expander(f"📄 {md_file.stem}", expanded=False):
                    st.caption(f"Last modified: {time.ctime(md_file.stat().st_mtime)}")
                    
                    content = read_article(md_file)
                    st.markdown(content)
                    
                    st.download_button(
                        label="Download Article",
                        data=content,
                        file_name=md_file.name,
                        mime="text/markdown"
                    )
                st.markdown("---")
