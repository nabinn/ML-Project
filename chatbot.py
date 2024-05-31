import os
from PIL import Image
import streamlit as st
from transformers import BlipProcessor, BlipForQuestionAnswering
from transformers import ViLTProcessor, ViLTForQuestionAnswering

# Create the models directory if it doesn't exist
if not os.path.exists("models"):
    os.makedirs("models")

# Streamlit layout
st.title('Picture Chatbot')

# Sidebar for model selection and picture upload
model = st.sidebar.selectbox("Select VQA Model", ("BLIP", "ViLT"))

# Maintaining session state for the uploaded image
if 'uploaded_image' not in st.session_state:
    st.session_state['uploaded_image'] = None

# Picture upload in the sidebar
uploaded_file = st.sidebar.file_uploader("Upload an image", type=['jpg', 'png', 'jpeg'])

# Clear chat history if no image is uploaded
if uploaded_file is None and st.session_state['uploaded_image'] is not None:
    st.session_state['messages'] = []
    st.session_state['uploaded_image'] = None

if uploaded_file is not None:
    st.session_state['uploaded_image'] = Image.open(uploaded_file).convert('RGB')
    st.sidebar.image(st.session_state['uploaded_image'], caption='Uploaded Image', use_column_width=True)

# Function to generate a response from a selected model
def get_response(model_name, question, image):
    if model_name == "BLIP" and image is not None:
        # Load the BLIP processor and model with cache_dir
        processor = BlipProcessor.from_pretrained("Salesforce/blip-vqa-capfilt-large", cache_dir="models")
        model = BlipForQuestionAnswering.from_pretrained("Salesforce/blip-vqa-capfilt-large", cache_dir="models")
        
        inputs = processor(image, question, return_tensors="pt").to("cpu")
        outputs = model.generate(**inputs)
        answer = processor.decode(outputs[0], skip_special_tokens=True)
    
    elif model_name == "ViLT":
        #answer = "ViLT model is not implemented yet. Please select BLIP."
        # Load the ViLT processor and model
        processor = ViLTProcessor.from_pretrained("dandelin/vilt-b32-finetuned-vqa", cache_dir="models")
        model = ViLTForQuestionAnswering.from_pretrained("dandelin/vilt-b32-finetuned-vqa", cache_dir="models")
        
        # Prepare the inputs
        inputs = processor(image, question, return_tensors="pt").to("cpu")
        
        # Generate the answer
        outputs = model.generate(**inputs)
        answer = processor.decode(outputs[0], skip_special_tokens=True)
    return answer

# Maintaining session state for chat messages
if 'messages' not in st.session_state:
    st.session_state['messages'] = []

# Check if an image is uploaded
if st.session_state['uploaded_image'] is None:
    st.write("Please upload an image to start the chat.")
else:
    # Displaying chat messages
    for author, message in st.session_state['messages']:
        with st.chat_message(author):
            st.write(message)
    
    # Chat interface
    prompt = st.chat_input("Your message", key="chat_input")

    if prompt:
        st.session_state['messages'].append(("human", prompt))  # Capture user input
        st.rerun()

    # Check if the last message is from the user and no response yet
    if len(st.session_state['messages']) > 0 and st.session_state['messages'][-1][0] == "human":
        with st.spinner("Generating response..."):
            bot_response = get_response(model_name=model, question=st.session_state['messages'][-1][1], image=st.session_state['uploaded_image'])
            st.session_state['messages'].append(("assistant", bot_response))  # Get bot response
            st.rerun()
