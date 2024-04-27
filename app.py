import os

base_path = './final_model'
os.system(f'git clone https://code.openxlab.org.cn/bitEEdh/internlm2-chat-1.8b-qlora-myAssistant.git {base_path}')
os.system(f'cd {base_path} && git lfs pull')
os.system('streamlit run web_demo.py --server.address=0.0.0.0 --server.port 7968')
