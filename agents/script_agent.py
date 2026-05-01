from tools.llm import call_llm
from tools.gdrive_tool import get_data

def generate_script(insights):
    data = get_data()
    prompt = f"""
    Based on:
    Insights: {insights}
    Product Data: {data}

    Create a 60-second high converting ad script.
    """
    script = call_llm(prompt)

    with open("outputs/script.txt", "w") as f:
        f.write(script)

    return script
