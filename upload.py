import os

def upload_arquivo(user_nickname):
    """Faz upload de arquivo no perfil"""

    file_path = input("Forneça o caminho do arquivo: ")
    
    # Verificar se o arquivo existe
    if not os.path.exists(file_path):
        print('Arquivo não encontrado.')
        return None

    # Diretório de destino para salvar os arquivos
    upload_dir = os.path.join('RePros', user_nickname)

    # Criar o diretório de upload se não existir
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)

    # Obter o nome do arquivo
    file_name = os.path.basename(file_path)

    # Caminho de destino do arquivo
    destination_path = os.path.join(upload_dir, file_name)

    # Copiar o arquivo para o diretório de upload
    with open(file_path, 'rb') as src_file, open(destination_path, 'wb') as dest_file:
        dest_file.write(src_file.read())

    # Salvar informações do arquivo
    file_info = {
        'file_name': file_name,
        'file_path': destination_path,
        'uploaded_by': user_nickname
    }

    print(file_info)

