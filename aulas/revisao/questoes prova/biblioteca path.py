from pathlib import Path

# criar a pasta
pasta = Path("exemplo_pasta")
pasta.mkdir(exist_ok=True)
# mostrar caminho da pasta
print("Caminho da pasta: ", pasta.resolve())
# criando um arquivo
arquivo = pasta / "arquivo.txt"
arquivo.open("w")