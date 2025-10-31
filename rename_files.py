import os

def rename_files_simple(directory):
    """
    Versão simplificada: renomeia arquivos com prefixo 'log' + número incremental
    """
    # Lista todos os arquivos no diretório
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    
    if not files:
        print("Nenhum arquivo encontrado!")
        return
    
    print(f"Arquivos originais: {files}")
    
    # Renomeia cada arquivo
    new_files = []
    for i, filename in enumerate(files, 1):
        # Separa nome e extensão
        name, ext = os.path.splitext(filename)
        
        # Cria novo nome
        new_name = f"log{i:03d}{ext}"
        
        # Caminhos completos
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_name)
        
        # Renomeia o arquivo
        os.rename(old_path, new_path)
        new_files.append(new_name)
        print(f"Renomeado: {filename} -> {new_name}")
    
    print(f"\nNovos arquivos: {sorted(new_files)}")

# Exemplo de uso
if __name__ == "__main__":
    directory = input("Digite o diretório (ou Enter para diretório atual): ").strip() or "."
    rename_files_simple(directory)