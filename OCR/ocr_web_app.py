import gradio as gr
from transformers import pipeline

ocr_pipeline = pipeline("image-to-text", model="microsoft/trocr-base-handwritten")

def extract_text(image):
    result = ocr_pipeline(image)
    extracted_text = result[0]["generated_text"]
    return extracted_text

def search_text(extracted_text, keyword):
    matches = [line for line in extracted_text.split("\n") if keyword.lower() in line.lower()]
    if matches:
        return "\n".join(matches)
    else:
        return "No matches found."

with gr.Blocks() as demo:
    gr.Markdown("## OCR Web Application with Keyword Search")
    
    image_input = gr.Image(type="filepath", label="Upload Image")
    
    extract_btn = gr.Button("Extract Text")

    extracted_output = gr.Textbox(label="Extracted Text")
    
    keyword_input = gr.Textbox(label="Search Keyword")
    
    search_btn = gr.Button("Search")
    
    search_output = gr.Textbox(label="Search Results")

    extract_btn.click(fn=extract_text, inputs=image_input, outputs=extracted_output)
    search_btn.click(fn=search_text, inputs=[extracted_output, keyword_input], outputs=search_output)

demo.launch()
