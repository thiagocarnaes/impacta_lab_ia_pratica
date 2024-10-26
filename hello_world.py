import streamlit as st
import platform
import subprocess


def get_pyenv_version():
    """Gets the currently active Python version managed by Pyenv."""
    result = subprocess.run(['pyenv', 'version'],
                            capture_output=True, text=True)
    if result.returncode == 0:
        return result.stdout.strip()
    else:
        return None


# Example usage:
pyenv_version = get_pyenv_version()

st.title("Automação de Atas")

st.write("Criando uma ferramenta de automação de atas")

st.write("Python version: " + platform.python_version())

st.write("Virtual env: " + pyenv_version)
