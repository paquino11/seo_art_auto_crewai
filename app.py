#app.py
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
                # Initialize session state for this file if not exists
                file_key = str(md_file.stem)
                if f"edit_mode_{file_key}" not in st.session_state:
                    st.session_state[f"edit_mode_{file_key}"] = False
                
                with st.expander(f"📄 {md_file.stem}", expanded=False):
                    st.caption(f"Last modified: {time.ctime(md_file.stat().st_mtime)}")
                    
                    # Read the current content
                    content = read_article(md_file)
                    
                    # Display content as markdown initially
                    if not st.session_state[f"edit_mode_{file_key}"]:
                        st.markdown(content)
                    
                    # Toggle edit mode
                    if st.button(
                        "Close Editor" if st.session_state[f"edit_mode_{file_key}"] else "Edit Article", 
                        key=f"edit_{file_key}"
                    ):
                        st.session_state[f"edit_mode_{file_key}"] = not st.session_state[f"edit_mode_{file_key}"]
                        st.rerun()
                    
                    if st.session_state[f"edit_mode_{file_key}"]:
                        # Show editing interface only when edit button is clicked
                        edited_content = st.text_area(
                            "Edit Article Content",
                            value=content,
                            height=300,
                            key=f"editor_{file_key}"
                        )
                        
                        if st.button("Save Changes", key=f"save_{file_key}"):
                            try:
                                with open(md_file, 'w') as file:
                                    file.write(edited_content)
                                st.success("Changes saved successfully!")
                                # Turn off edit mode after saving
                                st.session_state[f"edit_mode_{file_key}"] = False
                                st.rerun()
                            except Exception as e:
                                st.error(f"Error saving changes: {str(e)}")
                    
                    st.download_button(
                        label="Download Article",
                        data=content if not st.session_state[f"edit_mode_{file_key}"] else edited_content,
                        file_name=md_file.name,
                        mime="text/markdown"
                    )
                st.markdown("---")
