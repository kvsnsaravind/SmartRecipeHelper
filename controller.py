from model.model import analyze_text_and_generate_recipe

def handle_image_upload(image_file):
    return analyze_text_and_generate_recipe(image_file)

def handle_text_query(query):
    return analyze_text_and_generate_recipe(query)
